from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    blah = 'blah'
    return render(request,'seasons/index.html',{'blah':blah})
# Create your views here.
