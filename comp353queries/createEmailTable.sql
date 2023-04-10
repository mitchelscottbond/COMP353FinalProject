USE ubc353_4;
CREATE TABLE Emails(
emailID INT auto_increment,
emailTo VARCHAR(40),
emailFrom VARCHAR(40),
emailDate DATE,
emailSubject VARCHAR(100),
emailBody VARCHAR(1000),
PRIMARY KEY (emailID)
);