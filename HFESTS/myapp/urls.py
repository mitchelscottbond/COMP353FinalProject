from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Query1/', views.Query1, name='Query1'),
]