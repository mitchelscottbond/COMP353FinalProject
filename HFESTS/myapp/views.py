from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse

from myapp.models import Employee

from django.db import connection, transaction
#import models

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def Query1(request):

    employeeIDs = Employee.objects.raw("SELECT E.employeeID, O.occupationName FROM Employee AS E INNER JOIN EmployeeRole AS ER on ER.employeeID =E.employeeID INNER JOIN Occupation AS O on O.occupationID = ER.occupationID")

    df = pd.DataFrame([item.__dict__ for item in employeeIDs])
    df = df[df.columns[1:]]
    print(df)

    return render (request, 'query1.html', {'employees':df})
	