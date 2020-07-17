from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("hello world")

def home(request):
    return HttpResponse("well come to home page")    


def sample(request):
    return render(request,'sample.html')  


def sample1(request):
    return render(request,'sample1.html')      