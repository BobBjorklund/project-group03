from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
from psycopg2 import extras
# Create your views here.
def index(request):
    connection = psycopg2.connect(database="goats", user="lion", password="lion", host="localhost", port=5432)
    curr = connection.cursor(cursor_factory = psycopg2.extras.DictCursor)
    q = 'create or replace view maxweight as select animal_id, when_measured, max(alpha_value) as max_weight from weight group by animal_id, when_measured order by animal_id;'
    curr.execute(q)
    q = "Create or replace view adg as SELECT mw.animal_id, ((cast(mw.max_weight as double precision) - cast(coalesce(g.birth_weight, '0') as double precision)) / (datetoint(mw.when_measured)- datetoint(g.dob))) AS adg, g.dob FROM maxweight as mw inner join damwbw as g on g.animal_id = mw.animal_id;"
    curr.execute(q)
    q = 'Create or replace view adgbyseason as select a.animal_id, a.adg, sm.season from adg as a inner join season_month as sm on extract(month from a.dob) = sm.month;'
    curr.execute(q)
    q = 'create or replace view withsn as select a.animal_id, a.adg, s.seasonname from adgbyseason as a natural join season as s;'
    curr.execute(q)
    q = 'Create or replace view almost as Select seasonname, avg(adg) as averageADG from withsn group by seasonname;'
    curr.execute(q)
    q = 'Select s.seasonname, a.averageADG from season as s natural join almost as a;'
    curr.execute(q)
    

    s = curr.fetchall()
    s = [season for season in s]
    context={'s':s }
    return render(request,'seasons/index.html',context)
# Create your views here.

