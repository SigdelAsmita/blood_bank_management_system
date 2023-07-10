DROP TABLE IF EXISTS SURGERIES;
DROP TABLE IF EXISTS IMMUNIZATIONS;
DROP TABLE IF EXISTS DISEASES;
DROP TABLE IF EXISTS RECEPTION;
DROP TABLE IF EXISTS BLOOD;
DROP TABLE IF EXISTS BLOOD_BANK;
DROP TABLE IF EXISTS RELATIONSHIP;
DROP TABLE IF EXISTS PERSON;

CREATE TYPE blood_group AS ENUM ('O+', '0-', 'A+', 'A-', 'AB+', 'AB-', 'B+', 'B-');

CREATE TABLE IF NOT EXISTS PERSON (
    National_ID bigint PRIMARY KEY,
    Name varchar(50) NOT NULL,
    Address varchar(50) NOT NULL,
    Phone_Number varchar NOT NULL,
	Blood_Group blood_group NOT NULL	 
);

CREATE TABLE IF NOT EXISTS RELATIONSHIP (
    Person1_ID bigint,
    Person2_ID bigint,
    Relation varchar,

    PRIMARY KEY (Person1_ID, Person2_ID),
    FOREIGN KEY (Person1_ID) REFERENCES PERSON (National_ID),
    FOREIGN KEY (Person2_ID) REFERENCES PERSON (National_ID)
);

CREATE TABLE IF NOT EXISTS BLOOD_BANK (
    Bank_ID bigint PRIMARY KEY,
    Blood_Bank_Name varchar(50),
    Address varchar(50),
    Phone_Number varchar
);

CREATE TABLE IF NOT EXISTS BLOOD (
    Blood_ID bigint PRIMARY KEY,
    Bank_ID bigint,
    Donor_ID bigint,
    Donation_Date date NOT NULL,
    Blood_Group blood_group NOT NULL,
    Quantity DECIMAL(5, 4),
    FOREIGN KEY (Bank_ID) REFERENCES BLOOD_BANK (Bank_ID),
    FOREIGN KEY (Donor_ID) REFERENCES PERSON (National_ID)
);

CREATE TABLE IF NOT EXISTS RECEPTION (
    Receiver_ID bigint,
    Blood_ID bigint,
    Reception_ID date NOT NULL,
    Blood_Group blood_group NOT NULL,
    Quantity DECIMAL(5, 4),
    PRIMARY KEY (Receiver_ID, Blood_ID),
    FOREIGN KEY (Receiver_ID) REFERENCES PERSON (National_ID),
    FOREIGN KEY (Blood_ID) REFERENCES BLOOD (Blood_ID)
);

CREATE TABLE IF NOT EXISTS DISEASES(
	National_ID bigint,
	Disease_Name varchar(20) DEFAULT NULL,
	From_ date DEFAULT NULL,
	To_ date DEFAULT NULL,
	PRIMARY KEY (National_ID, Disease_Name),
	FOREIGN KEY (National_ID) REFERENCES PERSON (National_ID)
);

CREATE TABLE IF NOT EXISTS IMMUNIZATIONS(
	National_ID bigint, 
	Vaccine_Name varchar(20) DEFAULT NULL,
	Date_of_vaccination date DEFAULT NULL,
	PRIMARY KEY (National_ID, Vaccine_Name),
	FOREIGN KEY (National_ID) REFERENCES PERSON (National_ID)
);

CREATE TABLE IF NOT EXISTS SURGERIES(
	National_ID bigint,
	Surgery_Name varchar(30) DEFAULT NULL,
	Part_Of_Body varchar(20) DEFAULT NULL,
	Recovery_time int DEFAULT NULL,
	PRIMARY KEY (National_ID, Surgery_Name),
	FOREIGN KEY (National_ID) REFERENCES PERSON (National_ID)
);
