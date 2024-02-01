from django.urls import path
from . import views
urlpatterns = [
    path('add_elec_car/', views.elec_car,name='add_elec_car'),
    path('add_gas_car/', views.gas_car,name='add_gas_car'),

    path('', views.car_list,name='carlist'),
]
