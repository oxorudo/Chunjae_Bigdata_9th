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

---------------------------------------------------------------

CREATE TABLE authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(50)
);

CREATE TABLE books (
    book_id INT PRIMARY KEY,
    book_title VARCHAR(100),
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

INSERT INTO authors (author_id, author_name) VALUES
(1, 'Jane Austen'),
(2, 'George Orwell'),
(3, 'Charles Dickens');

INSERT INTO books (book_id, book_title, author_id) VALUES
(101, 'Pride and Prejudice', 1),
(102, '1984', 2),
(103, 'Great Expectations', 3),
(104, 'Emma', 1);

-- 위 테이블을 기반으로, 각 책의 제목과 저자의 이름을 조회하는 쿼리를 작성해 보세요.

SELECT book_title, author_name
FROM books
INNER JOIN authors
ON books.author_id = authors.author_id;

SELECT book_title, author_name
FROM books
LEFT OUTER JOIN authors
ON books.author_id = authors.author_id;



