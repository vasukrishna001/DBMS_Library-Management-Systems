--Creating Author Table
DROP TABLE IF EXISTS Author;
CREATE TABLE Author (
    Author_id INT PRIMARY KEY,
    Author_name VARCHAR(50),
    Author_country VARCHAR(50)
);
select * from Author;

DROP TABLE IF EXISTS Publishers;

CREATE TABLE Publishers (
    Publisher_id INT PRIMARY KEY,
    Publisher_name VARCHAR(100) UNIQUE,
    Experience_years INT,
    Ratings DECIMAL(3, 2),
    Books_published INT  );
Select * from Publishers;

--Creating Subscriptions table
DROP TABLE IF EXISTS Subscriptions;
CREATE TABLE Subscriptions (
    Sub_type VARCHAR(10) PRIMARY KEY,
    days_to_return INT,
    Sub_amount DECIMAL(10, 2)
);
SELECT * FROM Subscriptions;


--Creating Users Table
DROP TABLE IF EXISTS Users;
CREATE TABLE Users(
	user_id INT PRIMARY KEY,
	user_name VARCHAR(55),
	Age INT,
	Gender VARCHAR(10),
	Occupation VARCHAR(50),
	Sub_type VARCHAR(10) ,
	FOREIGN KEY (Sub_type) REFERENCES Subscriptions(Sub_type) );

select * from Users;

--Creating Books Table
DROP TABLE IF EXISTS Books;

CREATE TABLE Books (
    Book_id INT PRIMARY KEY,
    Book_Title VARCHAR(55),
    Shelf_loc VARCHAR(50),
    Ratings DECIMAL(3, 2),
    Book_price DECIMAL(10, 2),
    Genre VARCHAR(50),
    Publisher_id INT,
    Book_authorid INT,
    FOREIGN KEY (Publisher_id) REFERENCES Publishers(Publisher_id)
	  );

select * from Books;

--Creating Transactions
DROP TABLE IF EXISTS Transactions;

CREATE TABLE Transactions (
    Trans_id INT PRIMARY KEY,
    User_id INT,
    Book_id INT,
    Borrowed_date DATE,
    Return_date DATE,
    FOREIGN KEY (User_id) REFERENCES Users(user_id),
    FOREIGN KEY (Book_id) REFERENCES Books(Book_id) );
Select * from Transactions;


-- use these Insert Into subscriptions only after importing all the csv for Author,Publishers, Users,Books,Transactions.
--If these values are already inside the subscriptions table 
--Then due to foreign key constraints these data will be store inside the  Users data which will cause error while importing CSV for users.
INSERT INTO Subscriptions (Sub_type, days_to_return, Sub_amount)
        VALUES
    	('L-1', 7, 9.99),
    	('L-2', 14, 14.99),
    	('L-3', 21, 19.99),
    	('L-4', 30, 24.99),
    	('L-5', 45, 29.99);
	
SELECT * FROM Subscriptions;




	