from django.db import models

# Create your models here.

class People(models.Model):
    id = models.AutoField(primary_key=True,default="1")
    name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=510)
    email = models.EmailField()
    

class Address(models.Model):
    id = models.AutoField(primary_key=True,default="1")
    userName = models.CharField(max_length=510)
    lga = models.ManyToManyField(People, through="Doctors")
    city = models.CharField(max_length=510)
    state = models.CharField(max_length=510) 
   
class Doctor(models.Model):
    id = models.AutoField(primary_key=True,default="1")
    name = models.CharField(max_length=510)
    patient = models.ManyToManyField(People, through="Doctors")
    hospital = models.CharField(max_length=510)
    speciality = models.CharField(max_length=510)
    

class Product(models.Model):
    id = models.AutoField(primary_key=True,default="1")
    product_name = models.ManyToManyField(People, )
    product_price = models.CharField(max_length=510)
    product_cat = models.CharField(max_length=510)
    postedby = models.CharField(max_length=510)

    
class Bio(models.Model):
    userName = models.CharField(max_length=510)
    bio = models.CharField(max_length=50)
    datetime = models.DateField(auto_now_add=True)
    
    
    

 