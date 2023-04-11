USE ubc353_4;
-- Query 6
-- Get all facility info and workers working there 
-- sorted in ascending order by province, city, then type, then number of employees working at the facility

SELECT F.facilityID, F.facilityName, F.facilityAddress, P.city, P.Province, F.facilityPhone, F.facilityWebAddress, F.facilityType, F.capacity, COUNT(W.employeeID) AS numEmployees
FROM Facility AS F LEFT JOIN WorkAt AS W ON F.facilityID = W.facilityID INNER JOIN PostalCode AS P ON P.postalCode = F.facilityPostalCode 
GROUP BY F.facilityID
ORDER BY P.province DESC, P.city DESC, F.facilityType DESC, numEmployees DESC

-- MY test case.
-- INNER JOIN Employee AS E ON W.employeeID = E.employeeID INNER JOIN EmployeeRole AS ER ON E.employeeID = ER.employeeID