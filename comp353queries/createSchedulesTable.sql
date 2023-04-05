USE ubc353_4;
CREATE TABLE Schedules(
scheduleID int,
facilityID INT,
employeeID INT,
startTime DATE,
endTime DATE,
scheduleDate DATE,
occupationName VARCHAR(30),
PRIMARY KEY(scheduleID),
FOREIGN KEY (facilityID) REFERENCES Facility(facilityID) ON DELETE cascade,
FOREIGN KEY (employeeID) REFERENCES Employee(employeeID) ON DELETE CASCADE
);