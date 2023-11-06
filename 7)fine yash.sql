CREATE DATABASE ps7;
USE ps7;

CREATE TABLE borrower (
  rollno INT PRIMARY KEY,
  date_of_issue DATE,
  name_of_book VARCHAR(100),
  status VARCHAR(10)
);

CREATE TABLE fine (
  rollno INT,
  Date DATE,
  amt DECIMAL(10,2)
);

INSERT INTO borrower VALUES
(1, "2023-07-11", "DBMS", "I"),
(2, "2023-09-15", "AI", "I"),
(3, "2023-10-30", "CN", "I"),
(4, "2023-10-01", "HCI", "I");

DELIMITER //
CREATE PROCEDURE calfine2(IN rno INT, IN bookName VARCHAR(100))
BEGIN
  DECLARE dateofIssue DATE;
  DECLARE stat VARCHAR(10);
  DECLARE days_late INT;
  DECLARE fine_amt DECIMAL(10,2);

  DECLARE EXIT HANDLER FOR SQLEXCEPTION SELECT "Record not found";

  SELECT date_of_issue, status INTO dateofIssue, stat FROM borrower WHERE rollno = rno AND name_of_book = bookName;

  SET days_late = DATEDIFF(CURDATE(), dateofIssue);

  IF days_late > 30 THEN
    SET fine_amt = days_late * 50;
  ELSE
    SET fine_amt = days_late * 5;
  END IF;

  INSERT INTO fine VALUES(rno, dateofIssue, fine_amt);

  UPDATE borrower
  SET status = 'R'
  WHERE rollno = rno AND name_of_book = bookName;
END //
DELIMITER ;

CALL calfine2(1, "DBMS");

select * from fine;
