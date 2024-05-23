create database resturant_reservation;
use resturant_reservation;
create table Customers
(
	customerID int primary key not null unique auto_increment,
    customerName VARCHAR(45) not null,
    contactInfo VARCHAR(200) 
 );
 
 create table Reservation
 (
	reservationID int primary key not null unique auto_increment,
    customerID int not null,
    reservationTime DATETIME NOT NULL,
    numberOfGuests int not null,
    specialRequests varchar(200),
    foreign key (customerID) references Customers(customerID)
    );

create table DiningPreferences
(
	preferenceID int primary key unique auto_increment,
    customerID int not null,
    favoriteTable VARCHAR(45),
    dietaryRestrictions VARCHAR(200),
    foreign key (customerID) references Customers(customerID)
);

SELECT * FROM Reservation WHERE customerID = customerID;

SET SQL_SAFE_UPDATES = 0; -- Disable safe mode temporarily

UPDATE Reservation
SET specialRequests = 'requests'
WHERE reservationID = reservationID;

SET SQL_SAFE_UPDATES = 1; -- Enable safe mode again

-- Step 1: Check if the customer exists
SELECT customerID FROM Customers WHERE customerID = 'customerId';

-- Step 2: If the customer exists, retrieve the customerId; otherwise, insert a new customer
INSERT INTO Customers (customerName) 
VALUES ('customerName')
ON DUPLICATE KEY UPDATE customerID = LAST_INSERT_ID(customerID);

-- Step 3: Retrieve the customerId
SET @customerId = LAST_INSERT_ID();

-- Step 4: Add the reservation
INSERT INTO Reservation (customerID, reservationTime,numberOfGuests,specialRequests)
VALUES (2,"2024-02-14 19:30:44",4,"window seat"), (3,"2024-03-23 22:30:34",7,"large table"),(4,"2024-02-19 18:00:00",2,"Roses");

SELECT * FROM Reservation;


INSERT INTO Customers(customerName, contactInfo)
Value ("Jane Smith","janesmith@gmaail.com (123)-456-7689" ),
("Alfred Jones","alfredjones@gmail.comn (232)-345-1234"), ('Chondi Touray',"chonditouray@gmail.com (245)-444-4732");

select * from Customers;






