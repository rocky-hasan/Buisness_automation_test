from django.db import models

# Create your models here.
class Car(models.Model):
    name=models.CharField(max_length=100)
    car_model=models.CharField(max_length=100)
    year=models.CharField(max_length=100)

class ElectricCar(Car):
    battery_capacity=models.IntegerField(default=0)
    
class GasCar(Car):
    fuel_efficiency=models.IntegerField(default=0)
