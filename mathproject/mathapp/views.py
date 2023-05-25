from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def demo(request):
    name="welcome"
    return render(request,"index.html",{'obj':name})

def addition(request):

    return render(request,"math.html")