USE ubc353_4;

-- Query 13
-- For every facility get the province, facility name, capacity, and total number of infected employees by COVID-19 in the past two weeks. 
-- sorted in ascending order by province, then by total infected employees. 

SELECT P.province, F.facilityName, F.capacity,  ( SELECT COUNT(I.employeeID) FROM Infected AS I INNER JOIN Employee AS E on E.employeeID = I.employeeID INNER JOIN WorkAt AS W on E.employeeID = W.employeeID INNER JOIN Facility AS F1 ON W.facilityID = F1.facilityID 
													WHERE I.infectionDate >= DATE_SUB(NOW(), INTERVAL 2 WEEK) AND F1.facilityID = F.facilityID
                                                    ) AS EmployeesInfectedIn2Weeks
FROM Facility AS F INNER JOIN PostalCode AS P ON F.facilityPostalCode = P.postalCode
ORDER BY P.province ASC, EmployeesInfectedIn2Weeks ASC