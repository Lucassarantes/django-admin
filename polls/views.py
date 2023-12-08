from django.shortcuts import render
from django.http import HttpResponse
from .models import Dog

def detail(request, dog_id):
    return HttpResponse("You're looking at dog %s." % dog_id)

def results(request, dog_id):
    response = "You're looking at the results of dog %s."
    return HttpResponse(response % dog_id)

def index(request):
    latest_dogs_list = Dog.objects.order_by("id")[:5]
    output = ", ".join([dog.name for dog in latest_dogs_list])
    return HttpResponse(output)

# Create your views here.
