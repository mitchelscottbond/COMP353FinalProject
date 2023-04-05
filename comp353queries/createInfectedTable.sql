USE ubc353_4;
CREATE TABLE Infected (
infectionNumber int(20),
infectionDate DATE,
infectionType VARCHAR(30),
employeeID int NOT NULL,
PRIMARY KEY (infectionNumber, employeeID),
FOREIGN KEY (employeeID) REFERENCES Employee(employeeID) ON DELETE CASCADE
);
