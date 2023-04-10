USE ubc353_4;
SET @FacilityID = 1;
-- Query 7
-- Given a specific facilityID get all details of all employees at that facility. This includes firstname, lastname, start date of work, DOB, medicare, phone, address, city province, postal code, citizienship, and email addres,
-- sorted in ascending order by role then firstname then last name. 
SELECT E.employeeID, E.firstname, E.lastname, W.startdate, E.dateOfBirth, E.medicare, E.phone, E.address,  P.city, P.province, E.postal, E.citzenship, E.email, O.occupationName
FROM Employee AS E INNER JOIN EmployeeRole AS ER on ER.employeeID =E.employeeID INNER JOIN Occupation AS O on O.occupationID = ER.occupationID INNER JOIN PostalCode AS P on E.postal = P.postalCode INNER JOIN WorkAt as W on W.employeeID = E.employeeID 
WHERE E.employeeiD in (SELECT W.employeeID
						FROM WorkAt as W
                        WHERE W.facilityID = @FacilityID) AND W.enddate IS NULL
ORDER BY O.occupationName ASC, E.firstname ASC, E.lastname ASC;

