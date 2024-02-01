from django.shortcuts import render,redirect
from .forms import ElectricCarForm,GasCarForm
from .models import Car,ElectricCar,GasCar
# Create your views here.

def elec_car(request):
    if request.method=='POST':
        form=ElectricCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carlist')
    else:
        form=ElectricCarForm()
    return render(request,'addcar.html',{'form':form})
def gas_car(request):
    if request.method=='POST':
        form=GasCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carlist')
    else:
        form=GasCarForm()
    return render(request,'addcar.html',{'form':form})




def car_list(request):
    Ecars = ElectricCar.objects.all()
    Gcars = GasCar.objects.all()
    context={
        'Ecars':Ecars,
        'Gcars':Gcars,
    }
    return render(request, 'listcar.html', context)