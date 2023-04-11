USE ubc353_4;

-- Query 9
-- Get details of all doctors who have been infected by covid 19 in the past 2 weeks, details include doctors first name, lastname, date of infection, name of the facility doctor is currently working for. 
-- sorted in ascending order by facility name, then by firstname. 

SELECT E.firstname, E.lastname, I.infectionDate, F.facilityName
FROM Employee AS E INNER JOIN Infected AS I ON E.employeeID = I.employeeID INNER JOIN WorkAt AS W ON E.employeeID = W.employeeID INNER JOIN Facility AS F ON W.facilityID = F.facilityID
WHERE E.employeeID in ( SELECT Infected.employeeID
						FROM Infected INNER JOIN EmployeeRole ON Infected.employeeID = EmployeeRole.employeeID
						WHERE infectionDate >= DATE_SUB(NOW(), INTERVAL 2 WEEK) AND EmployeeRole.occupationID = 2
                        )
ORDER BY F.facilityName ASC, E.firstname ASC;
