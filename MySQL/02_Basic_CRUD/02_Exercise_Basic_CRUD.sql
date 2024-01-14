/* 01. Find All Information About Departments */
USE soft_uni;
-- below is for Judge
SELECT *
FROM departments
ORDER BY department_id;
-- END

/* 02. Find all Department Names */
SELECT name
FROM departments
ORDER BY department_id;
-- END

/* 03. Find Salary of Each Employee */
SELECT first_name, last_name, salary
FROM employees
ORDER BY employee_id;
-- END

/* 04. Find Full Name of Each Employee */
SELECT first_name, middle_name, last_name
FROM employees
ORDER BY employee_id;
-- END

/* 05. Find Email Address of Each Employee */
SELECT
	concat(first_name, '.', last_name, '@softuni.bg') AS 'full_email_address'
FROM employees;
-- END

/* 06. Find All Different Employee’s Salaries */
SELECT DISTINCT salary
FROM employees;
-- END

/* 07. Find all Information About Employees */
SELECT *
FROM employees
WHERE job_title = 'Sales Representative'
ORDER BY employee_id;
-- END

/* 08. Find Names of All Employees by Salary in Range */
SELECT first_name, last_name, job_title
FROM employees
WHERE salary BETWEEN 20000 and 30000
ORDER BY employee_id;
-- END

/* 9. Find Names of All Employees */
SELECT 
	CONCAT_WS(' ', first_name, middle_name, last_name) AS 'Full Name'
FROM employees
WHERE salary IN (25000, 14000, 12500, 23600);
-- END

/* 10. Find All Employees Without Manager */
SELECT first_name, last_name
FROM employees
WHERE manager_id IS NULL;
-- END

/* 11. Find All Employees with Salary More Than */
SELECT first_name, last_name, salary
FROM employees
WHERE salary > 50000
ORDER BY salary DESC;
-- END

/* 12. Find 5 Best Paid Employees */
SELECT first_name, last_name
FROM employees
ORDER BY salary DESC
LIMIT 5;
-- END

/* 13. Find All Employees Except Marketing */
SELECT first_name, last_name
FROM employees
WHERE department_id != 4;
-- END

/* 14. Sort Employees Table */
SELECT *
FROM employees
ORDER BY
	salary DESC,
    first_name,
    last_name DESC,
    middle_name;
-- END

/* 15. Create View Employees with Salaries */
CREATE VIEW v_employees_salaries AS
	SELECT first_name, last_name, salary
    FROM employees;
    
SELECT * FROM v_employees_salaries;
-- END

/* 16. Create View Employees with Job Titles */
CREATE VIEW v_employees_job_titles AS
	SELECT
		CONCAT_WS(' ', first_name, middle_name, last_name) AS 'full_name',
        job_title
	FROM employees;

SELECT * FROM v_employees_job_titles;
-- END

/* 17. Distinct Job Titles */
SELECT DISTINCT job_title
FROM employees
ORDER BY job_title;
-- END

/* 18. Find First 10 Started Projects */
SELECT *
FROM projects
ORDER BY start_date, name
LIMIT 10;
-- END

/* 19. Last 7 Hired Employees */
SELECT first_name, last_name, hire_date
FROM employees
ORDER BY hire_date DESC
LIMIT 7;
-- END

/* 20. Increase Salaries */
UPDATE employees
SET salary = salary * 1.12
WHERE department_id IN(1, 2, 4, 11);

SELECT salary FROM employees;
-- END

/* 21. All Mountain Peaks */
USE geography;
-- below is for Judge
SELECT peak_name
FROM peaks
ORDER BY peak_name;
-- END

/* 22. Biggest Countries by Population */
SELECT country_name, population
FROM countries
WHERE continent_code = 'EU'
ORDER BY
	population DESC,
    country_name
LIMIT 30;
-- END

/* 23. Countries and Currency (Euro / Not Euro) */
SELECT 
	country_name, 
    country_code, 
    CASE
		WHEN currency_code = 'EUR' THEN 'Euro'
        ELSE 'Not Euro'
	END AS 'currency'
FROM countries
ORDER BY country_name;
-- END

/* 24. All Diablo Characters */
USE diablo;
-- below is for Judge
SELECT `name`
FROM characters
ORDER BY `name`;
-- END