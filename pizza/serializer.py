from rest_framework import serializers
from .models import pizza 
class pizzaserializer (serializers.ModelSerializer):
    class Meta: 
      model=pizza
      fields='__all__'