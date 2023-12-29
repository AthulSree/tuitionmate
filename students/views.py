from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("Hello World")
    studs = {'first':{'name':'sreeraj SS','age':30, 'course':'EEE'}}
    return render(request,'home.html',studs)


def test(request):
    return HttpResponse("Hiii")
    
