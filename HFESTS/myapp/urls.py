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
    path('Query8page/', views.Query8, name='Query8'),
    path('Query9page/', views.Query9, name='Query9'),
    path('Query10page/', views.Query10, name='Query10'),
    path('Query11page/', views.Query11, name='Query11'),
    path('Query12page/', views.Query12, name='Query12'),
    path('Query13page/', views.Query13, name='Query13'),
    path('Query14page/', views.Query14, name='Query14'),
    path('Query15page/', views.Query15, name='Query15'),
    path('Query16page/', views.Query16, name='Query16'),
    path('Query17page/', views.Query17, name='Query17'),
]