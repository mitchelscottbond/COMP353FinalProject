from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse

from myapp.models import Employee
from myapp.models import Facility
import myapp.models
from myapp.models import Infected
from myapp.models import Received
from django.db import connections, transaction
#import models

# Create your views here.
def home(request):
    return render(request, 'home.html', {})


#This function returns all the employees in the system partially satisfying criteria 2 in the project.
def Employees(request):
    result = ""
    textbox = ""
    employeeIDs = Employee.objects.raw("SELECT * FROM Employee")
    df = pd.DataFrame([item.__dict__ for item in employeeIDs])
    df = df[df.columns[1:]]
    if request.method == 'POST':
        button_pressed = request.POST.get('button_pressed')
        if button_pressed == 'delete':
            employeeIDforEditing = request.POST.get('employeeIDforEditing')
            with connections['default'].cursor() as cursor:
                cursor.execute("DELETE FROM Employee WHERE employeeID = %s", [employeeIDforEditing])
            
            print(employeeIDforEditing)
            #This is a delete query to the employee table
        elif button_pressed == 'edit':
            rand = "rand"
            # This is going to be an update to the employee table
        elif button_pressed == "insert":
            employeeID = request.POST['employeeID']
            medicare = request.POST['medicare']
            medicare = f"'{medicare}'"
            firstname = request.POST['firstname']
            firstname = f"'{firstname}'"
            lastname = request.POST['lastname']
            lastname = f"'{lastname}'"
            dateofbirth = request.POST['dateofbirth']
            dateofbirth = f"'{dateofbirth}'"
            phone = request.POST['phone']
            phone = f"'{phone}'"
            address = request.POST['address']
            address = f"'{address}'"
            postal = request.POST['postal']
            postal = f"'{postal}'"
            email = request.POST['email']
            email = f"'{email}'"
            citizienship = request.POST['citizenship']
            citizienship = f"'{citizienship}'"
            strings = [employeeID, medicare, firstname, lastname, dateofbirth, phone, address, postal, email, citizienship] 
            result = ', '.join(strings)
            print(result)
            insertquery = f"INSERT INTO Employee(employeeID, medicare, firstName, lastName, dateOfBirth, phone, address, postal, email, citzenship) VALUES({employeeID}, {medicare}, {firstname}, {lastname}, {dateofbirth}, {phone}, {address}, {postal}, {email}, {citizienship})"
            with connections['default'].cursor() as cursor:
                cursor.execute(insertquery)
            
            context = {
            'employees': df,
            'result': result
            }
            return render(request, 'employees.html', {'context':context})
        context = {
            'employees': df,
            'result': result
            }
        return render(request, 'employees.html', {'context':context})
    else:
        context = {
        'employees': df,
        'result': result
        }
        return render (request, 'employees.html', {'context':context})
	

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

#This function returns a page to display the results of query #6
def Query6(request):

    result = ""
    df = ""

    query6 = f"SELECT F.facilityID, F.facilityName, F.facilityAddress, P.city, P.Province, F.facilityPhone, F.facilityWebAddress, F.facilityType, F.capacity, COUNT(W.employeeID) AS numEmployees FROM Facility AS F LEFT JOIN WorkAt AS W ON F.facilityID = W.facilityID INNER JOIN PostalCode AS P ON P.postalCode = F.facilityPostalCode GROUP BY F.facilityID ORDER BY P.province DESC, P.city DESC, F.facilityType DESC, numEmployees DESC"
    queryresults = Facility.objects.raw(query6)
    df = pd.DataFrame([item.__dict__ for item in queryresults])
    df = df[df.columns[1:]]

    context = {
    'query': df,
    'result': result
    }
    print("This is running the get request")
    return render (request, 'Query6.html', {'context':context})



#This function returns a page to display the results of query #7
def Query7(request):

    result = ""
    df = ""
    if request.method == 'POST':
        facilityID = request.POST['Query7Facility']
        query7 = f"SELECT E.employeeID, E.firstname, E.lastname, W.startdate, E.dateOfBirth, E.medicare, E.phone, E.address,  P.city, P.province, E.postal, E.citzenship, E.email, O.occupationName FROM Employee AS E INNER JOIN EmployeeRole AS ER on ER.employeeID =E.employeeID INNER JOIN Occupation AS O on O.occupationID = ER.occupationID INNER JOIN PostalCode AS P on E.postal = P.postalCode INNER JOIN WorkAt as W on W.employeeID = E.employeeID  WHERE E.employeeiD in (SELECT W.employeeID FROM WorkAt as W WHERE W.facilityID = {facilityID}) AND W.enddate IS NULL ORDER BY O.occupationName ASC, E.firstname ASC, E.lastname ASC"
        queryresults = Employee.objects.raw(query7)
        df = pd.DataFrame([item.__dict__ for item in queryresults])
        df = df[df.columns[1:]]
        result = facilityID
        context = {
        'query': df,
        'result': result
        }
        return render(request, 'Query7.html', {'context':context})
    else:
        context = {
        'query': df,
        'result': result
        }
        print("This is running the get request")
        return render (request, 'Query7.html', {'context':context})



