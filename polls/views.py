from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Lucas you get it")

# Create your views here.
