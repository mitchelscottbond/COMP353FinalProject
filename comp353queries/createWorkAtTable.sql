USE ubc353_4;
CREATE TABLE WorkAt (
facilityID int,
employeeID int,
startdate DATE,
enddate DATE,
PRIMARY KEY (employeeID, facilityID, startdate),
FOREIGN KEY (facilityID) REFERENCES Facility(facilityID) ON DELETE cascade,
FOREIGN KEY (employeeID) REFERENCES Employee(employeeID) ON DELETE CASCADE
);