-- Create a database and switch to it
CREATE DATABASE ps8;
USE ps8;

-- Create a table for student records
CREATE TABLE student_records (
    sid INT PRIMARY KEY AUTO_INCREMENT,
    Sname VARCHAR(100),
    class VARCHAR(50),
    address VARCHAR(50),
    grades CHAR,
    enroll_date DATE,
    subject_name VARCHAR(50),
    attendance INT
);

-- Insert data into the student_records table
INSERT INTO student_records VALUES
(1, "ABC", "9th grade", "Nashik", 'A', "2023-10-05", "DBMS", 65),
(2, "PQR", "10th grade", "Pune", 'B', "2023-05-13", "AI", 95),
(3, "XYZ", "9th grade", "Mumbai", 'A', "2023-04-15", "CN", 55);

-- Create a view to select specific columns from the student_records table
CREATE VIEW studentview AS SELECT sid, Sname, grades, attendance FROM student_records;

select * from studentview;

-- Create an index on the 'Sname' column in the student_records table
CREATE INDEX sindex ON student_records(Sname);

show index from student_records;
