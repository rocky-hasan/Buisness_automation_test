from django.contrib import admin
from .models import Car,ElectricCar,GasCar
# Register your models here.
admin.site.register(Car)
admin.site.register(ElectricCar)
admin.site.register(GasCar)