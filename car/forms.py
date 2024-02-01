from django import forms
from .models import ElectricCar, GasCar

class ElectricCarForm(forms.ModelForm):
    class Meta:
        model = ElectricCar
        fields = ['name', 'car_model', 'year', 'battery_capacity']

class GasCarForm(forms.ModelForm):
    class Meta:
        model = GasCar
        fields = ['name', 'car_model', 'year', 'fuel_efficiency']

