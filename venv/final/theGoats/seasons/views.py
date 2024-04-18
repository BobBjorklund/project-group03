from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
from psycopg2 import extras
# Create your views here.
def index(request):
    connection = psycopg2.connect(database="goats", user="lion", password="lion", host="localhost", port=5432)
    curr = connection.cursor(cursor_factory = psycopg2.extras.DictCursor)
    q = 'select * from season;'
    curr.execute(q)
    s = curr.fetchall()
    s = [season for season in s]
    context={
        's':s
    }
    return render(request,'seasons/index.html',context)
# Create your views here.
