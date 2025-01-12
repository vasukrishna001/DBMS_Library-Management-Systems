--Creating Author Table
DROP TABLE IF EXISTS Author ;
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



-- Queries used in this project

--Finds the genre which was burrowed by nost of users
select TT.genre from
(select genre, count (distinct (transactions.user_id)) as cnt
from transactions inner join books on transactions.book_id = books.book_id
group by genre) TT
where TT.cnt =
(select max(T.cnt) from
(select genre, count (distinct (transactions.user_id)) as cnt
from transactions inner join books on transactions.book_id = books.book_id
group by genre) T);



-- Find the age,gender,occupation of users who takes more than 5 days to return the book and the number of times they did 
-- this was greater than 2 times
select users.age,users.gender,users.occupation from transactions,users 
where users.user_id = transactions.user_id and (return_date ::date - borrowed_date::date)>5
group by users.user_id having count(users.user_id)>2;


--- Inserting Author details----
INSERT INTO Author values ((select max(author_id ) from author) + 1,  'Stephen','ABC')


---- Delete transactions that are too old----
DELETE FROM transactions WHERE ((SELECT CURRENT_DATE) - return_date) > 10;


----update country of author using name----
update author
set author_country = 'CHINA'
where 
author_name = 'stephen'


---Inserting Publisher details----
INSERT INTO publishers values ((select max(publisher_id ) from publishers) + 1,  'SD',8,5.5,6)


----update ratings of publisher using id----
update publishers
set ratings = 4
where 
publisher_id = 3



---Delete books with less ratings and also remove transcations invovled with those books---
DELETE FROM transactions WHERE 
exists (
select book_id from books where ratings < 1 and books.book_id = transactions.book_id
);
DELETE FROM books where ratings<1


-- Finds the users who didn't return the book
select users.user_name
from transactions,users
where users.user_id = transactions.user_id and transactions.return_date is null
group by
transactions.user_id,users.user_name

--For each genre find the average rating
select books.genre, AVG(books.ratings)
from
books
group by books.genre


--For each price find the average rating
select books.book_price ,AVG(books.ratings)
from 
books
group by books.book_price


-- This query determines how frequently each author's books are borrowed throughout three dynamic time periods--
WITH CTE_date AS     (
    SELECT MAX(Borrowed_date) AS last_borrowed FROM Transactions)
SELECT Aut.Author_name,     
COUNT(CASE  WHEN Ts.Borrowed_date>=(SELECT  DATE(last_borrowed)-INTERVAL'10 years'  FROM CTE_date) 
	        THEN 1 END) AS last_10Y ,
COUNT(CASE WHEN Ts.Borrowed_date>=(SELECT  DATE(last_borrowed) -INTERVAL'3 years'  FROM CTE_date) 
	  THEN 1 END) AS  last_3Y ,
COUNT(CASE  WHEN Ts.Borrowed_date>=(SELECT  DATE(last_borrowed)- INTERVAL'1 year'  FROM CTE_date) 
	  THEN 1 END) AS  last_Y
FROM Transactions Ts
JOIN Books  ON Ts.Book_id = Books.Book_id JOIN Author Aut ON Books.Book_authorid = Aut.Author_id
GROUP BY Aut.Author_name ORDER BY last_10Y DESC, last_3Y DESC, last_Y DESC;




	
