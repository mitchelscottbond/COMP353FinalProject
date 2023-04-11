USE ubc353_4;
-- QUERY#15
-- Get nurse with most hours on the schedule, return firstname, lastname, first day of work as a nurse ever, DOB, email, Total hourse scheduled. 
SELECT E.firstname, E.lastname, E.dateOfBirth,E.email, ABS(SUM(TIME_TO_SEC(TIMEDIFF(endTime, startTime))) / 3600) as total_hours, W.startdate
FROM Schedules AS S INNER JOIN Employee AS E ON E.employeeID = S.employeeID INNER JOIN EmployeeRole AS ER ON E.employeeID = ER.employeeID INNER JOIN WorkAt AS W ON W.employeeID = E.employeeID
WHERE  ER.occupationID = 1
GROUP BY S.employeeID
ORDER BY total_hours DESC
LIMIT 1;
