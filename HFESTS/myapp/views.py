from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse

from myapp.models import Employee
from myapp.models import Facility
import myapp.models
from myapp.models import Infected
from myapp.models import Received
from myapp.models import Schedules
from myapp.models import Emails
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

#This function returns a page to display the results of query #8
def Query8(request):

    result = ""
    df = ""
    if request.method == 'POST':
        startinterval = request.POST['Query8Starttime']
        startinterval = f"'{startinterval}'"
        endinterval = request.POST['Query8endtime']
        endinterval = f"'{endinterval}'"
        employee_id = request.POST['Query8empID']

        query8 = f"SELECT S.scheduleID, F.facilityName, S.scheduleDate, S.startTime, S.endTime FROM Schedules S, Facility F WHERE S.employeeID = {employee_id} AND S.facilityID = F.facilityID AND S.scheduleDate between {startinterval} and {endinterval} ORDER BY F.facilityName ASC, S.scheduleDate ASC, S.startTime ASC"
        queryresults = Schedules.objects.raw(query8)
        df = pd.DataFrame([item.__dict__ for item in queryresults])
        df = df[df.columns[2:]]
        result = startinterval + ' | ' + endinterval + ' | ' + employee_id
        context = {
        'query': df,
        'result': result
        }
        return render(request, 'Query8.html', {'context':context})
    
    else:
        context = {
        'query': df,
        'result': result
        }
        print("This is running the get request")
        return render (request, 'Query8.html', {'context':context})

#This function returns a page to display the results of query #9
def Query9(request):

    result = ""
    df = ""

    query9 = f"SELECT E.employeeID, E.firstname, E.lastname, I.infectionDate, F.facilityName FROM Employee AS E INNER JOIN Infected AS I ON E.employeeID = I.employeeID INNER JOIN WorkAt AS W ON E.employeeID = W.employeeID INNER JOIN Facility AS F ON W.facilityID = F.facilityID WHERE E.employeeID in ( SELECT Infected.employeeID FROM Infected INNER JOIN EmployeeRole ON Infected.employeeID = EmployeeRole.employeeID WHERE infectionDate >= DATE_SUB(NOW(), INTERVAL 2 WEEK) AND EmployeeRole.occupationID = 2) ORDER BY F.facilityName ASC, E.firstname ASC;"
    queryresults = Employee.objects.raw(query9)
    df = pd.DataFrame([item.__dict__ for item in queryresults])
    df = df[df.columns[2:]]

    context = {
    'query': df,
    'result': result
    }
    print("This is running the get request")
    return render (request, 'Query9.html', {'context':context})

#This function returns a page to display the results of query #10
def Query10(request):

    result = ""
    df = ""
    if request.method == 'POST':
        facilityWeb = request.POST['Query10Facility']
        facilityWeb = f"'{facilityWeb}'"
        query10 = f"SELECT * FROM Emails WHERE emailFrom = {facilityWeb}"
        queryresults = Emails.objects.raw(query10)
        df = pd.DataFrame([item.__dict__ for item in queryresults])
        df = df[df.columns[1:]]
        result = facilityWeb
        context = {
        'query': df,
        'result': result
        }
        return render(request, 'Query10.html', {'context':context})
    else:
        context = {
        'query': df,
        'result': result
        }
        print("This is running the get request")
        return render (request, 'Query10.html', {'context':context})

#This function returns a page to display the results of query #11
def Query11(request):

    result = ""
    df = ""
    if request.method == 'POST':
        facilityID_Q11 = request.POST['Query11Facility']
        facilityID_Q11 = f"'{facilityID_Q11}'"
        query11 = f"SELECT DISTINCT E.employeeID, E.firstname, E.lastname, O.occupationName FROM Facility AS F INNER JOIN Schedules AS S ON F.facilityID = S.facilityID INNER JOIN Employee AS E ON E.employeeID = S.employeeID INNER JOIN EmployeeRole AS ER ON ER.employeeID = E.employeeID INNER JOIN Occupation AS O ON ER.occupationID = O.occupationID  WHERE S.scheduleID IN ( SELECT DISTINCT S.scheduleID FROM Schedules AS S INNER JOIN Employee AS E ON E.employeeID = S.employeeID INNER JOIN EmployeeRole AS ER ON ER.employeeID = E.employeeID WHERE S.scheduleDate >= DATE_SUB(NOW(), INTERVAL 2 WEEK) AND (ER.occupationID=2 OR ER.occupationID = 1) ) AND F.facilityID = {facilityID_Q11} ORDER BY O.occupationName ASC, E.firstname ASC"
        queryresults = Employee.objects.raw(query11)
        df = pd.DataFrame([item.__dict__ for item in queryresults])
        df = df[df.columns[2:]]
        result = facilityID_Q11
        context = {
        'query': df,
        'result': result
        }
        return render(request, 'Query11.html', {'context':context})
    else:
        context = {
        'query': df,
        'result': result
        }
        print("This is running the get request")
        return render (request, 'Query11.html', {'context':context})

#This function returns a page to display the results of query #12
def Query12(request):

    result = ""
    df = ""
    if request.method == 'POST':
        facility_name = request.POST['Query12Name']
        facility_name = f"'{facility_name}'"
        startinterval = request.POST['Query12Starttime']
        startinterval = f"'{startinterval}'"
        endinterval = request.POST['Query12endtime']
        endinterval = f"'{endinterval}'"

        query12 = f"SELECT S.scheduleID, F.facilityName, O.occupationName, SUM(TIME_TO_SEC(TIMEDIFF(S.endTime, S.startTime))) / 3600 totalHours FROM Schedules S, Facility F, EmployeeRole ER, Occupation O WHERE S.facilityID = F.facilityID AND F.facilityName = {facility_name} AND S.employeeID = ER.employeeID AND ER.occupationID = O.occupationID AND S.scheduleDate between {startinterval} AND {endinterval} GROUP BY F.facilityName, O.occupationName ORDER BY occupationName ASC"
        queryresults = Schedules.objects.raw(query12)
        df = pd.DataFrame([item.__dict__ for item in queryresults])
        df = df[df.columns[1:]]
        result = facility_name + ' | ' + startinterval + ' | ' + endinterval
        context = {
        'query': df,
        'result': result
        }
        return render(request, 'Query12.html', {'context':context})
    
    else:
        context = {
        'query': df,
        'result': result
        }
        print("This is running the get request")
        return render (request, 'Query12.html', {'context':context})

#This function returns a page to display the results of query #13
def Query13(request):

    result = ""
    df = ""

    query13 = f"SELECT F.facilityID, P.province, F.facilityName, F.capacity, (SELECT COUNT(I.employeeID) FROM Infected AS I INNER JOIN Employee AS E on E.employeeID = I.employeeID INNER JOIN WorkAt AS W on E.employeeID = W.employeeID INNER JOIN Facility AS F1 ON W.facilityID = F1.facilityID WHERE I.infectionDate >= DATE_SUB(NOW(), INTERVAL 2 WEEK) AND F1.facilityID = F.facilityID) AS EmployeesInfectedIn2Weeks FROM Facility AS F INNER JOIN PostalCode AS P ON F.facilityPostalCode = P.postalCode ORDER BY P.province ASC, EmployeesInfectedIn2Weeks ASC"

    queryresults = Facility.objects.raw(query13)
    df = pd.DataFrame([item.__dict__ for item in queryresults])
    df = df[df.columns[2:]]

    context = {
    'query': df,
    'result': result
    }
    print("This is running the get request")
    return render (request, 'Query13.html', {'context':context})

#This function returns a page to display the results of query #14
def Query14(request):

    result = ""
    df = ""

    query14 = f"SELECT E.employeeID, E.firstName, E.lastName, P.city, COUNT(DISTINCT W.facilityID) FacilitiesWorkingAt FROM Employee E, PostalCode P, WorkAt W, EmployeeRole ER, Occupation O WHERE E.postal=P.postalCode AND P.province = 'Quebec' AND E.employeeID = W.employeeID AND E.employeeID = ER.employeeID  AND ER.occupationID = O.occupationID AND O.occupationName = 'Doctor' AND W.enddate IS NULL GROUP BY E.firstName, E.lastName, P.city ORDER BY P.city ASC, FacilitiesWorkingAt DESC"
    queryresults = Employee.objects.raw(query14)
    df = pd.DataFrame([item.__dict__ for item in queryresults])
    df = df[df.columns[2:]]

    context = {
    'query': df,
    'result': result
    }
    print("This is running the get request")
    return render (request, 'Query14.html', {'context':context})

#This function returns a page to display the results of query #15
def Query15(request):

    result = ""
    df = ""

    query15 = f"SELECT E.employeeID, E.firstname, E.lastname, E.dateOfBirth, E.email, ABS(SUM(TIME_TO_SEC(TIMEDIFF(endTime, startTime))) / 3600) as total_hours, W.startdate FROM Schedules AS S INNER JOIN Employee AS E ON E.employeeID = S.employeeID INNER JOIN EmployeeRole AS ER ON E.employeeID = ER.employeeID INNER JOIN WorkAt AS W ON W.employeeID = E.employeeID WHERE  ER.occupationID = 1 GROUP BY S.employeeID ORDER BY total_hours DESC LIMIT 1;"
    queryresults = Employee.objects.raw(query15)
    df = pd.DataFrame([item.__dict__ for item in queryresults])
    df = df[df.columns[2:]]

    context = {
    'query': df,
    'result': result
    }
    print("This is running the get request")
    return render (request, 'Query15.html', {'context':context})

#This function returns a page to display the results of query #16
def Query16(request):

    result = ""
    df = ""

    query16 = f"SELECT E.employeeID, E.firstName, E.lastName, MIN(S.scheduleDate) firstDayOfWork, O.occupationName, E.dateOfBirth, E.email, SUM(TIME_TO_SEC(TIMEDIFF(S.endTime, S.startTime))) / 3600 totalHours FROM Employee E, Infected I, EmployeeRole ER, Schedules S, Occupation O WHERE E.employeeID = ER.employeeID AND E.employeeID = S.employeeID AND ER.occupationID = O.occupationID AND O.occupationName IN ('Doctor', 'Nurse') AND E.employeeID = I.employeeID AND I.infectionType = 'COVID-19' AND I.infectionNumber>=3 GROUP BY  E.email ORDER BY O.occupationName ASC, E.firstName ASC, E.lastName ASC;"
    queryresults = Employee.objects.raw(query16)
    df = pd.DataFrame([item.__dict__ for item in queryresults])
    df = df[df.columns[2:]]

    context = {
    'query': df,
    'result': result
    }
    print("This is running the get request")
    return render (request, 'Query16.html', {'context':context})

#This function returns a page to display the results of query #17
def Query17(request):

    result = ""
    df = ""

    query17 = f"SELECT E.employeeID, E.firstname, E.lastname,W.startdate, O.occupationName, E.dateOfBirth, E.email, ABS(SUM(TIME_TO_SEC(TIMEDIFF(endTime, startTime))) / 3600) as total_hours FROM Schedules AS S INNER JOIN Employee AS E ON E.employeeID = S.employeeID INNER JOIN EmployeeRole AS ER ON E.employeeID = ER.employeeID INNER JOIN WorkAt AS W ON W.employeeID = E.employeeID INNER JOIN Occupation AS O ON ER.occupationID = O.occupationID WHERE  (ER.occupationID = 1 OR ER.occupationID = 2) AND E.employeeID NOT IN (SELECT I.employeeID FROM Infected AS I WHERE I.infectionType = 'COVID-19') GROUP BY S.employeeID ORDER BY O.occupationName, E.firstname, E.lastname"
    queryresults = Employee.objects.raw(query17)
    df = pd.DataFrame([item.__dict__ for item in queryresults])
    df = df[df.columns[2:]]

    context = {
    'query': df,
    'result': result
    }
    print("This is running the get request")
    return render (request, 'Query17.html', {'context':context})