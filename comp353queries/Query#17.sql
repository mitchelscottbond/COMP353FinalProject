USE ubc353_4;
-- QUERY#15
-- Get nurse or doctor who are working and have never been infected with COVID-19, return firstname, lastname, first day of work, occupation, DOB, email, Total hourse scheduled. 
-- Order by role, firstname, lastname
SELECT E.firstname, E.lastname,W.startdate, O.occupationName, E.dateOfBirth, E.email, ABS(SUM(TIME_TO_SEC(TIMEDIFF(endTime, startTime))) / 3600) as total_hours 
FROM Schedules AS S INNER JOIN Employee AS E ON E.employeeID = S.employeeID INNER JOIN EmployeeRole AS ER ON E.employeeID = ER.employeeID INNER JOIN WorkAt AS W ON W.employeeID = E.employeeID INNER JOIN Occupation AS O ON ER.occupationID = O.occupationID
WHERE  (ER.occupationID = 1 OR ER.occupationID = 2) AND E.employeeID NOT IN (SELECT I.employeeID
																			 FROM Infected AS I
                                                                             WHERE I.infectionType = 'COVID-19'
                                                                            )
GROUP BY S.employeeID
ORDER BY O.occupationName, E.firstname, E.lastname