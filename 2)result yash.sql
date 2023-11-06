CREATE DATABASE StudentDB;
USE StudentDB;

-- Create the procedure to categorize students
CREATE TABLE IF NOT EXISTS Result (
    Roll INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255),
    Class VARCHAR(255)
);
DELIMITER //
CREATE PROCEDURE proc_Grade(IN student_name VARCHAR(255), IN total_marks INT)
BEGIN
    DECLARE student_class VARCHAR(255);
    
    IF total_marks <= 1500 AND total_marks >= 990 THEN
        SET student_class = 'Distinction';
    ELSEIF total_marks >= 900 AND total_marks <= 989 THEN
        SET student_class = 'First Class';
    ELSEIF total_marks >= 825 AND total_marks <= 899 THEN
        SET student_class = 'Higher Second Class';
    ELSE
        SET student_class = 'Other';
    END IF;

    -- Insert the result into the Result table
    INSERT INTO Result(Roll, Name, Class) VALUES(NULL, student_name, student_class);
END //
DELIMITER ;

-- Call the stored procedure with sample data
CALL proc_Grade('John', 1200);
CALL proc_Grade('Alice', 950);
CALL proc_Grade('Bob', 850);

SELECT * FROM Result;