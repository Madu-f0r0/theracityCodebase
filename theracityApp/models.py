from django.db import models
from django.contrib.gis.db import models as gismodels
from custom_user import User


# Create your models here.
class Pharmacy(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pharmacy_name = models.CharField(max_length=100)
    address = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    location = gismodels.PointField()

    def __str__(self):
        return self.pharmacy_name


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