from django.shortcuts import render
from django.http import HttpResponse
# from django.template import render
# Create your views here.
import psycopg2
from psycopg2 import extras
def index(request):
    connection = psycopg2.connect(database="goats", user="lion", password="lion", host="localhost", port=5432)
    cursor = connection.cursor()
    curr = connection.cursor(cursor_factory = psycopg2.extras.DictCursor)

    q = "Select damwbw.*, ww.alpha_value as wean_weight from damwbw left join ww on damwbw.animal_id=ww.animal_id where tag <> '' order by dob;"
    curr.execute(q)
    dam2 = curr.fetchall()
    dam2={dam['tag']:dam for dam in dam2}
    winweights = {}

    # print(dam)
    cursor.execute(q)
    dams = cursor.fetchall()
    q = "select animal_id, alpha_value, extract(month from when_measured), extract(year from when_measured) from winterweights order by animal_id,when_measured;"
    curr.execute(q)
    wws = curr.fetchall()
    for ww in wws:
        if not (ww[0] in winweights.keys()):
            winweights[ww[0]] = [(ww[1],ww[2],ww[3])]
        else:
            winweights[ww[0]].append((ww[1],ww[2],ww[3]))
    damsnkids = {}
    for dam in dams:
        tmp = dam[2]
        damsnkids[tmp] =[]
        if not (dam[0] in winweights.keys()):
            winweights[dam[0]] = [('no','data','found')]
    colnames = [desc[0] for desc in cursor.description]
    q = 'Select kidwbw.*, ww.alpha_value as wean_weight from kidwbw left join ww on kidwbw.animal_id=ww.animal_id order by dob, animal_id;'
    cursor.execute(q)
    kids = cursor.fetchall()
    # damskids = {}
    # kidsdict = {}
    for kid in kids:
        id = kid[2]
        did = kid[4]
        if not (kid[0] in winweights.keys()):
            winweights[kid[0]] = [('no','data','found')]
        if did in damsnkids.keys():
            damsnkids[did].append([x for x in kid])

    #     i = 0
    #     id = kid[0]
    #     did = kid[4]
    #     if not did in damskids:
    #         damskids[did] = [id]
    #     else:
    #         damskids[did].append(id)
    # print(damskids)

    return render(request,'progeny/index.html',{'dam2':winweights,'dams':dams,'colnames':colnames,'dk':damsnkids})