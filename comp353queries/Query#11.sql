USE ubc353_4;
SET @FID = 1;
-- Query 11
-- For a given facility get the list of doctors or nurses on schedule past 2 weeks, firstname, lastname and role.
-- sorted in ascending order by role then first name

SELECT DISTINCT  E.firstname, E.lastname, O.occupationName
FROM Facility AS F INNER JOIN Schedules AS S ON F.facilityID = S.facilityID INNER JOIN Employee AS E ON E.employeeID = S.employeeID INNER JOIN EmployeeRole AS ER ON ER.employeeID = E.employeeID INNER JOIN Occupation AS O ON ER.occupationID = O.occupationID 
WHERE S.scheduleID IN ( SELECT DISTINCT S.scheduleID
						FROM Schedules AS S INNER JOIN Employee AS E ON E.employeeID = S.employeeID INNER JOIN EmployeeRole AS ER ON ER.employeeID = E.employeeID
						WHERE S.scheduleDate >= DATE_SUB(NOW(), INTERVAL 2 WEEK) AND (ER.occupationID=2 OR ER.occupationID = 1)
                        ) AND F.facilityID = @FID
ORDER BY O.occupationName ASC, E.firstname ASC