from django.shortcuts import render
from django.http import HttpResponse
# from django.template import render
# Create your views here.
import psycopg2
def index(request):
    connection = psycopg2.connect(database="goats", user="lion", password="lion", host="localhost", port=5432)
    cursor = connection.cursor()
    q = "Select damwbw.*, ww.alpha_value as wean_weight from damwbw left join ww on damwbw.animal_id=ww.animal_id where tag <> '' order by dob;"
    cursor.execute(q)
    dams = cursor.fetchall()
    damsnkids = {}
    for dam in dams:
        tmp = dam[2]
        damsnkids[tmp] =[]
    colnames = [desc[0] for desc in cursor.description]
    q = 'Select kidwbw.*, ww.alpha_value as wean_weight from kidwbw left join ww on kidwbw.animal_id=ww.animal_id order by dob, animal_id;'
    cursor.execute(q)
    kids = cursor.fetchall()
    # damskids = {}
    # kidsdict = {}
    for kid in kids:
        id = kid[2]
        did = kid[4]
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

    return render(request,'progeny/index.html',{'dams':dams,'colnames':colnames,'dk':damsnkids})