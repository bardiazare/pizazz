from django.shortcuts import render
from rest_framework.views import Response
from rest_framework import status
from .models import pizza
from .serializer import pizzaserializer

# Create your views here.

def pizza_list():
    data = pizza.objects.all()
    serializer = pizzaserializer(data,many=True)
