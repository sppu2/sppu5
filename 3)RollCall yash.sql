CREATE DATABASE rollcall;
USE rollcall;

CREATE TABLE oldRollCall(rno INT PRIMARY KEY, name VARCHAR(20));
INSERT INTO oldRollCall VALUES(1, "ABC"), (2, "XYZ"), (3, "PQR");
CREATE TABLE newRollCall(rno INT, name VARCHAR(20));

DELIMITER //
CREATE PROCEDURE Merge()
BEGIN
  DECLARE done INT DEFAULT FALSE;
  DECLARE rollno INT;
  DECLARE Sname VARCHAR(20);
  DECLARE c1 CURSOR FOR SELECT rno, name FROM oldRollCall;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

  OPEN c1;

  read_loop: LOOP
    FETCH c1 INTO rollno, Sname;
    IF done THEN
      LEAVE read_loop;
    END IF;

    IF NOT EXISTS (SELECT 1 FROM newRollCall WHERE rno = rollno AND name = Sname) THEN
      INSERT INTO newRollCall (rno, name) VALUES (rollno, Sname);
    END IF;
  END LOOP;

  CLOSE c1;
END;
//
DELIMITER ;

CALL Merge();

-- Data in oldRollCall and newRollCall tables
SELECT * FROM oldRollCall;
SELECT * FROM newRollCall;
