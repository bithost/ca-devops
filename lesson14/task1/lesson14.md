# Write basic SQL query and create Students table

Required fields

* ID
* Age
* Name

create database
```sql
CREATE DATABASE school;
```


select database to use
```sql
USE school;
```

```sql

CREATE TABLE Students (
    ID INT PRIMARY KEY,
    Age INT,
    Name VARCHAR(255)
);

```

Insert 10 fake records
```sql
INSERT INTO Students (ID, Age, Name)
VALUES
    (1, 20, 'John Doe'),
    (2, 22, 'Jane Smith'),
    (3, 21, 'Alice Johnson'),
    (4, 23, 'Bob Wilson'),
    (5, 19, 'Emily Brown'),
    (6, 20, 'David Taylor'),
    (7, 22, 'Sophia Miller'),
    (8, 21, 'Michael Davis'),
    (9, 23, 'Olivia Harris'),
    (10, 19, 'Daniel Robinson');
```

List students
```sql
SELECT * FROM Students;
```