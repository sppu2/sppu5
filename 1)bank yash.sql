sudo apt update
sudo apt install mysql-server

--Start MySQL Server:
sudo service mysql start

--Access MySQL:
mysql -u root -p

--Create a Database:
CREATE DATABASE bank;
USE bank;




-- 1. Create tables with appropriate constraints

-- Account Table
CREATE TABLE Account (
    Acc_no INT PRIMARY KEY,
    branch_name VARCHAR(50),
    balance DECIMAL(10, 2),
    FOREIGN KEY (branch_name) REFERENCES branch(branch_name)
);

-- Branch Table
CREATE TABLE Branch (
    branch_name VARCHAR(50) PRIMARY KEY,
    branch_city VARCHAR(50),
    assets_amt DECIMAL(12, 2)
);

-- Customer Table
CREATE TABLE Customer (
    cust_name VARCHAR(50) PRIMARY KEY,
    cust_street VARCHAR(100),
    cust_city VARCHAR(50)
);

-- Depositor Table
CREATE TABLE Depositor (
    cust_name VARCHAR(50),
    acc_no INT,
    FOREIGN KEY (cust_name) REFERENCES Customer(cust_name),
    FOREIGN KEY (acc_no) REFERENCES Account(Acc_no)
);

-- Loan Table
CREATE TABLE Loan (
    Acc_no INT,
    loan_no INT PRIMARY KEY,
    branch_name VARCHAR(50),
    amount DECIMAL(10, 2),
    FOREIGN KEY (Acc_no) REFERENCES Account(Acc_no),
    FOREIGN KEY (branch_name) REFERENCES Branch(branch_name)
);

-- Borrower Table
CREATE TABLE Borrower (
    cust_name VARCHAR(50),
    loan_no INT,
    FOREIGN KEY (cust_name) REFERENCES Customer(cust_name),
    FOREIGN KEY (loan_no) REFERENCES Loan(loan_no)
);


INSERT INTO branch (branch_name, branch_city, assets_amt)
VALUES ('Pimpri', 'Pune', 1000000),
       ('Akurdi', 'Pune', 800000),
       ('Chinchwad', 'Pune', 1200000);

INSERT INTO customer (cust_name, cust_street, cust_city)
VALUES ('John Doe', '123 Main St', 'Pune'),
       ('Jane Smith', '456 Elm St', 'Pune'),
       ('Bob Johnson', '789 Oak St', 'Pune');

INSERT INTO Account (Acc_no, branch_name, balance)
VALUES (1, 'Pimpri', 5000),
       (2, 'Akurdi', 7500),
       (3, 'Chinchwad', 6000);

INSERT INTO Depositor (cust_name, acc_no)
VALUES ('John Doe', 1),
       ('Jane Smith', 2),
       ('Bob Johnson', 3);

INSERT INTO Loan (Acc_no, loan_no, branch_name, amount)
VALUES (1, 101, 'Pimpri', 15000),
       (2, 102, 'Akurdi', 13000),
       (3, 103, 'Chinchwad', 14000);

INSERT INTO Borrower (cust_name, loan_no)
VALUES ('John Doe', 101),
       ('Jane Smith', 102),
       ('Bob Johnson', 103);



-- 2. Find the names of all branches in the Loan relation
SELECT DISTINCT branch_name FROM Loan;

-- 3. Find all loan numbers for loans made at Pimpri Branch with loan amount > 12000
SELECT loan_no FROM Loan WHERE branch_name = 'Pimpri' AND amount > 12000;

-- 4. Find all customers who have a loan from the bank. Find their names, loan_no, and loan amount.
SELECT c.cust_name, l.loan_no, l.amount
FROM Customer c
JOIN Borrower b ON c.cust_name = b.cust_name
JOIN Loan l ON b.loan_no = l.loan_no;

-- 5. List all customers in alphabetical order who have a loan from Akurdi branch.
SELECT c.cust_name
FROM Customer c
JOIN Borrower b ON c.cust_name = b.cust_name
JOIN Loan l ON b.loan_no = l.loan_no
WHERE l.branch_name = 'Akurdi'
ORDER BY c.cust_name;

-- 6. Find all customers who have an account or loan or both at the bank.
SELECT DISTINCT c.cust_name
FROM Customer c
LEFT JOIN Depositor d ON c.cust_name = d.cust_name
LEFT JOIN Borrower b ON c.cust_name = b.cust_name
WHERE d.cust_name IS NOT NULL OR b.cust_name IS NOT NULL;

-- 7. Find all customers who have both account and loan at the bank.
SELECT DISTINCT c.cust_name
FROM Customer c
JOIN Depositor d ON c.cust_name = d.cust_name
JOIN Borrower b ON c.cust_name = b.cust_name;

-- 8. Find average account balance at Pimpri branch.
SELECT AVG(a.balance)
FROM Account a
WHERE a.branch_name = 'Pimpri';

-- 9. Find the average account balance at each branch
SELECT branch_name, AVG(balance) as avg_balance
FROM Account
GROUP BY branch_name;

-- 10. Find the branches where average account balance > 12000
SELECT branch_name
FROM (
    SELECT branch_name, AVG(balance) as avg_balance
    FROM Account
    GROUP BY branch_name
) AS branch_avg
WHERE avg_balance > 12000;

-- 11. Calculate total loan amount given by the bank
SELECT SUM(amount) as total_loan_amount
FROM Loan;


--Exit MySQL:
Exit MySQL: