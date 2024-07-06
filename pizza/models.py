from django.db import models

from uuid import uuid4

# Create your models here.
class pizza(models.Model):
    id= models.UUIDField(null=False,unique=True,editable=False,default=uuid4,primary_key=True)
    name= models.CharField(null=False,max_length=200,)
    price= models.IntegerField(null=False,)
    def __str__(self) -> str:
        return self.name