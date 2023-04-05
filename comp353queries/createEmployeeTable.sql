USE ubc353_4;
Create table Employee (
employeeID int, 
medicare VARCHAR(12) NOT NULL UNIQUE,
firstName VARCHAR (25),
lastName VARCHAR(25),
dateOfBirth DATE,
phone VARCHAR(15),
address VARCHAR(50),
postal VARCHAR(7), 
email VARCHAR(50),
citzenship VARCHAR(30),
PRIMARY KEY (employeeID)
);
