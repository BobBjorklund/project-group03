from django.shortcuts import render
from django.http import HttpResponse
# from django.template import render
# Create your views here.
import psycopg2
def index(request):
    connection = psycopg2.connect(database="goats", user="lion", password="lion", host="localhost", port=5432)
    cursor = connection.cursor()
    q = 'Select * from damwbw;'
    cursor.execute(q)
    dams = cursor.fetchall()
    return render(request,'progeny/index.html',{'dams':dams})