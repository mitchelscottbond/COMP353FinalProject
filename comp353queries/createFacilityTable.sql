USE ubc353_4;
Create TABLE Facility (
facilityID int auto_increment,
facilityName VARCHAR(75),
facilityWebAddress VARCHAR(200),
facilityType VARCHAR(30),
facilityPhone VARCHAR(15),
facilityAddress VARCHAR(50),
facilityPostalCode VARCHAR(10),
capacity int,
PRIMARY KEY(facilityID)
);
