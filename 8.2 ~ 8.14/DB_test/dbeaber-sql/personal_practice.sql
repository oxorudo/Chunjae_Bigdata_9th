-- chatgpt에게 문제를 내달라고 함.

USE db_test;

CREATE TABLE students(
id int AUTO_INCREMENT PRIMARY KEY,
name varchar(50),
age int,
major varchar(50)
);

INSERT INTO students(
id, name, age, major) VALUES (1, 'Alice', 21, 'Computer Science'),
(2, 'Bob', 22, 'Mathematics'),(3, 'Carol', 20, 'Biology');

SELECT name,major
FROM students
WHERE 1 = 1;

SELECT *
FROM students
WHERE age >= 21;

UPDATE students
SET major = 'Chemistry'
WHERE id = 3;

DELETE FROM students
WHERE id = 2;

select * FROM students;




