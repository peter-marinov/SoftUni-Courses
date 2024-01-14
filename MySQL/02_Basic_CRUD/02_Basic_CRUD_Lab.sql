CREATE DATABASE IF NOT EXISTS `hotel`; 
USE `hotel`;

CREATE TABLE departments (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(50)
);

INSERT INTO departments(name) VALUES('Front Office'), ('Support'), ('Kitchen'), ('Other');

CREATE TABLE employees (
	id INT PRIMARY KEY AUTO_INCREMENT,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	job_title VARCHAR(50) NOT NULL,
	department_id INT NOT NULL,
	salary DOUBLE NOT NULL,
	CONSTRAINT `fk_department_id` FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`)
);

INSERT INTO `employees` (`first_name`,`last_name`, `job_title`,`department_id`,`salary`) VALUES
	('John', 'Smith', 'Manager',1, 900.00),
	('John', 'Johnson', 'Customer Service',2, 880.00),
	('Smith', 'Johnson', 'Porter', 4, 1100.00),
	('Peter', 'Petrov', 'Front Desk Clerk', 1, 1100.00),
	('Peter', 'Ivanov', 'Sales', 2, 1500.23),
	('Ivan' ,'Petrov', 'Waiter', 3, 990.00),
	('Jack', 'Jackson', 'Executive Chef', 3, 1800.00),
	('Pedro', 'Petrov', 'Front Desk Supervisor', 1, 2100.00),
	('Nikolay', 'Ivanov', 'Housekeeping', 4, 1600.00);
	

	
CREATE TABLE rooms (
	id INT PRIMARY KEY AUTO_INCREMENT,
	`type` VARCHAR(30)
);

INSERT INTO rooms(`type`) VALUES('apartment'), ('single room');

CREATE TABLE clients (
	id INT PRIMARY KEY AUTO_INCREMENT,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	room_id INT NOT NULL,
    CONSTRAINT fk_clients_rooms
    FOREIGN KEY (room_id)
    REFERENCES rooms(id)
);

INSERT INTO clients(`first_name`,`last_name`,`room_id`) 
VALUES('Pesho','Petrov', 1),('Gosho','Georgiev', 2),
('Mariya','Marieva', 2), ('Katya','Katerinova', 1), ('Nikolay','Nikolaev', 2);

-- This was the DB from Judge

SELECT id, first_name, last_name, job_title
FROM employees
ORDER BY first_name, last_name;

/* 01. Select Employee Information */
SELECT id, first_name, last_name, job_title
FROM employees
ORDER BY id;
-- END

SELECT 
	e.id AS "No. ", 
    e.first_name AS "First Name", 
    e.last_name AS "Last Name", 
    e.job_title AS "Job title"
FROM hotel.employees AS e
ORDER BY id;

SELECT CONCAT("#", id, " -> ", first_name, " ", last_name) AS "Full name"
FROM employees;

-- Adds a separater between each element
SELECT CONCAT_WS('-', first_name, last_name, job_title) AS "Details"
FROM employees;

SELECT
	CONCAT(first_name, " ", last_name) AS "CONCAT", -- If there is NULL the return for this line will be NULL
    CONCAT_WS(" ", first_name, last_name) AS "CONCAT_WS" -- If there is NULL it will skip it and return the rest
FROM clients;



/* 02. Select Employees with Filter */
SELECT
	id,
    CONCAT(first_name, ' ', last_name) AS 'full_name',
    job_title,
    salary
FROM employees
WHERE salary > 1000
ORDER BY id;
-- END

SELECT DISTINCT first_name
FROM employees;

SELECT *
FROM employees
WHERE department_id <> 1; -- <> is the same as != ( not equal )

SELECT *
FROM employees
WHERE department_id = 1 OR (salary > 1100 AND salary < 2000);

SELECT *
FROM employees
WHERE salary BETWEEN 1100 and 2000; -- include the min and max value

SELECT
	DISTINCT department_id
FROM employees
WHERE salary < 1500;

SELECT * 
FROM departments
WHERE id IN (1, 2, 3, 4);

SELECT * 
FROM departments
WHERE id NOT IN (1, 2, 3);

SELECT * 
FROM employees
WHERE NOT department_id = 1;

SELECT *
FROM employees
WHERE salary > 1100 && salary < 2000;

SELECT * 
FROM clients
WHERE first_name IS NOT NULL;

CREATE VIEW v_employee_summary AS
    SELECT 
        id,
        CONCAT(first_name, ' ', last_name) AS 'Full name',
        job_title,
        salary
    FROM
        employees
    WHERE
        salary > 1000
    ORDER BY first_name , last_name;
    
SELECT `Full name`
FROM v_employee_summary
WHERE salary > 1500;

CREATE OR REPLACE VIEW v_employee_summary AS
    SELECT 
        id,
        CONCAT(first_name, ' ', last_name) AS 'Updated Full name',
        job_title,
        salary
    FROM
        employees
    WHERE
        salary > 1000
    ORDER BY first_name , last_name;
    
DROP VIEW v_employee_summary;

SELECT *
FROM v_employee_summary
WHERE salary > 1500;

CREATE TABLE test_clients AS
	SELECT id, first_name, room_id
    FROM clients
    WHERE first_name IS NOT NULL;
    
SELECT * FROM test_clients;

INSERT INTO test_clients(first_name, room_id)
	SELECT first_name, room_id
    FROM clients
    WHERE first_name IS NOT NULL;


UPDATE test_clients
SET 
	id = 3,
    first_name = CONCAT('Updated ', first_name)
WHERE first_name = 'Gosho';

SELECT * FROM test_clients;

/* 03. Update Salary and Select */
UPDATE employees
SET
	salary = salary + 100
WHERE 
	job_title = 'Manager';
    
SELECT salary
FROM employees;
-- END

SET SQL_SAFE_UPDATES = 0;

/* 04. Top Paid Employee */
CREATE VIEW v_top_paid_employee AS
    SELECT *
    FROM employees
    ORDER BY salary DESC
    LIMIT 1;
    
SELECT * FROM v_top_paid_employee;
-- END

/* 05. Select Employees by Multiple Filters */
SELECT *
FROM employees
WHERE department_id = 4 AND salary >= 1000
ORDER BY id;
-- END

/* 06. Delete from Table */
DELETE FROM employees
WHERE department_id = 1 OR department_id = 2;

SELECT *
FROM employees
ORDER BY id;
-- END
