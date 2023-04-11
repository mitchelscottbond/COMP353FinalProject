from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Employees/', views.Employees, name='Employees'),
    path('Facilities/', views.Facilities, name='Facilities'),
    path('VaccinationRecords/', views.Vaccinations, name='Vaccinations'),
    path('InfectionRecords/', views.Infections, name='Infections'),
    path('Query6page/', views.Query6, name='Query6'),
    path('Query7page/', views.Query7, name='Query7'),
]