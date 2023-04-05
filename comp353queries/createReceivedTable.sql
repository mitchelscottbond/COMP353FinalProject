USE ubc353_4;
CREATE TABLE Received(
vaccineID INT,
employeeID INT,
doseNum INT,
dateReceived DATE,
facilityID INT,
PRIMARY KEY (employeeID, doseNum),
FOREIGN KEY (employeeID) REFERENCES Employee(employeeID) ON DELETE CASCADE,
FOREIGN KEY (facilityID) REFERENCES Facility(facilityID) ON DELETE CASCADE,
FOREIGN KEY (vaccineID) REFERENCES Vaccine(vaccineID) ON DELETE CASCADE
);
