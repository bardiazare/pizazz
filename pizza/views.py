from django.shortcuts import render
from rest_framework.views import Response
from rest_framework import status
from .models import pizza
from .serializer import pizzaserializer
from rest_framework.decorators import api_view
from django.http import JsonResponse

# Create your views here.
@api_view(['GET'])

def pizza_list(req):
    data = pizza.objects.all()
    serializer = pizzaserializer(data,many=True)
    return JsonResponse(serializer.data,status=status.HTTP_200_OK,safe=False)

