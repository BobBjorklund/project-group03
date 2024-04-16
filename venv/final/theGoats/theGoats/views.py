from django.shortcuts import render
from django.http import HttpResponse
from progeny import urls
from seasons import urls
# Create your views here.
def index(request):
    links = {'The Progeny Report':'pindex','The Seasonal Birth Cohort Report':'sindex'}
    return render(request,'theGoats/index.html',context={'links':links})