USE ubc353_4;

SELECT E.employeeID, O.occupationName
FROM Employee AS E INNER JOIN EmployeeRole AS ER on ER.employeeID =E.employeeID INNER JOIN Occupation AS O on O.occupationID = ER.occupationID;
