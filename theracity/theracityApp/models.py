from django.db import models
from django.contrib.gis.db import models as gismodels


# Create your models here.
class Pharmacy(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=45)
    pharmacy_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    location = gismodels.PointField()


class Medicine(models.Model):
    medicine_name = models.CharField(max_length=45)
    manufacturer_name = models.CharField(max_length=200)
    manufacturer_country = models.CharField(max_length=45)


class Stock(models.Model):
    store = models.ForeignKey('Pharmacy', on_delete=models.CASCADE)
    medicine = models.ForeignKey('Medicine', on_delete=models.CASCADE) 
    amount = models.PositiveIntegerField(null=True)
    price = models.PositiveIntegerField(null=True)
    available = models.CharField(max_length=3)