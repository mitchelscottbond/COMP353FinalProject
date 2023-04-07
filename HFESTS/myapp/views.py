from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse

from myapp.models import Employee
from myapp.models import Facility
import myapp.models
from myapp.models import Infected
from myapp.models import Received
from django.db import connection, transaction
#import models

# Create your views here.
def home(request):
    return render(request, 'home.html', {})


#This function returns all the employees in the system partially satisfying criteria 2 in the project.
def Employees(request):

    employeeIDs = Employee.objects.raw("SELECT E.employeeID, O.occupationName FROM Employee AS E INNER JOIN EmployeeRole AS ER on ER.employeeID =E.employeeID INNER JOIN Occupation AS O on O.occupationID = ER.occupationID")

    df = pd.DataFrame([item.__dict__ for item in employeeIDs])
    df = df[df.columns[1:]]
    print(df)

    return render (request, 'employees.html', {'employees':df})
	

#This function returns all the facilities in the system partially satisfying criteria 1 in the project.
def Facilities(request):

    facilities = Facility.objects.raw("SELECT * FROM Facility")

    df = pd.DataFrame([item.__dict__ for item in facilities])
    df = df[df.columns[1:]]
    print(df)

    return render (request, 'facilities.html', {'facilities':df})


#This function returns all the employees vaccination records in the system partially satisfying criteria 3 in the project.
def Vaccinations(request):

    vaccinations = Received.objects.raw("SELECT * FROM Received")

    df = pd.DataFrame([item.__dict__ for item in vaccinations])
    df = df[df.columns[1:]]
    print(df)

    return render (request, 'vaccinations.html', {'received':df})



#This function returns all the infection records in the system partially satisfying criteria 4 in the project.
def Infections(request):

    infections = Infected.objects.raw("SELECT * FROM Infected")

    df = pd.DataFrame([item.__dict__ for item in infections])
    df = df[df.columns[1:]]
    print(df)

    return render (request, 'Infections.html', {'infections':df})


