USE ubc353_4;
CREATE TABLE EmployeeRole (
occupationID int,
employeeID int,
Primary KEY (occupationID, employeeID),
FOREIGN KEY (employeeID) REFERENCES Employee(employeeID) ON DELETE CASCADE,
FOREIGN KEY (occupationID) REFERENCES Occupation(occupationID) ON DELETE CASCADE
);