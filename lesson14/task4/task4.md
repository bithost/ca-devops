# launch instance of PostgreSQL on Docker. Create a database, and oqpeciment with performing CRUD

## Tasks

(Create, Read, Update, Delete) operations using the SQL commands you learned.


CREATE DATABASE my_test_db;

switch table
\c my_test_db

create table
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(10, 2)
);


insert data
INSERT INTO employees (name, position, salary)
VALUES
('John Doe', 'Software Engineer', 75000),
('Jane Smith', 'Project Manager', 85000),
('Mark Taylor', 'DevOps Engineer', 80000);


Read
SELECT * FROM employees;


Modify
UPDATE employees
SET salary = 78000
WHERE name = 'John Doe';


Verify
SELECT * FROM employees WHERE name = 'John Doe';


Delete
DELETE FROM employees
WHERE name = 'Mark Taylor';

Verify
SELECT * FROM employees;
