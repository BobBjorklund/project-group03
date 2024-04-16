from django.shortcuts import render
from django.http import HttpResponse
# from django.template import render
# Create your views here.
def index(request):
    return render(request,'progeny/index.html',{})