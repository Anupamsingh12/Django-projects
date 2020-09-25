from django.db import models

# Create your models here.
class client(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField( max_length=254)
    password=models.CharField( max_length=50)
    gender=models.CharField(max_length=50)
    dob=models.DateField(auto_now=False)