from django.shortcuts import render

from django.http import HttpResponse

from myapp.models import Employee

from django.db import connection, transaction
#import models

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def Query1(request):
   # cursor = connection.cursor()
    # Data retrieval operation - no commit required
   # cursor.execute("SELECT employeeID FROM Employee")
    #row = cursor.fetchone()
    #print("This is row:" + row[0].employeeid)
    employeeIDs = Employee.objects.raw("SELECT * FROM Employee")
    for id in employeeIDs:
        print(id.firstname)
    print(employeeIDs[1].employeeid)
    #for employee in (Employee.objects.raw("SELECT employeeID, FROM myapp_Employee")):
    #    print(employee)
    #print(row)
    #print(employeeIDs)
    return render (request, 'query1.html', {'employeeID':employeeIDs})
	