/* 01. Find Names of All Employees by First Name */
USE soft_uni;
-- below is for Judge
SELECT first_name, last_name
FROM employees
WHERE first_name LIKE 'Sa%'
ORDER BY employee_id;
-- End

/* 02. Find Names of All Employees by Last Name */
SELECT first_name, last_name
FROM employees
WHERE LOCATE('ei', last_name) > 0
ORDER BY employee_id;
-- End

/* 03. Find First Names of All Employess */
SELECT first_name
FROM employees
WHERE department_id IN (3, 10) AND YEAR(hire_date) BETWEEN 1995 AND 2005
ORDER BY employee_id;
-- End

/* 04. Find All Employees Except Engineers */
SELECT first_name, last_name
FROM employees
WHERE LOCATE('engineer', job_title) = 0
ORDER by employee_id;
-- End

/* 05. Find Towns with Name Length */
SELECT name
FROM towns
WHERE CHAR_LENGTH(name) BETWEEN 5 AND 6
ORDER BY name;
-- End

/* 06. Find Towns Starting With */
SELECT *
FROM towns
WHERE name REGEXP '^[MmKkBbEe]'
ORDER BY name;
-- End

/* 07. Find Towns Not Starting With */
SELECT *
FROM towns
WHERE name REGEXP '^[RrBbDd]' = 0
ORDER BY name;
-- End

/* 08. Create View Employees Hired After */
CREATE VIEW v_employees_hired_after_2000 AS
	SELECT first_name, last_name
    FROM employees
    WHERE YEAR(hire_date) > 2000;
    
SELECT * FROM v_employees_hired_after_2000;
-- End

/* 09. Length of Last Name */
SELECT first_name, last_name
FROM employees
WHERE CHAR_LENGTH(last_name) = 5;
-- End

/* 10. Countries Holding 'A' */
USE geography;
-- below is for Judge
SELECT country_name, iso_code
FROM countries
WHERE country_name LIKE '%a%a%a%'
ORDER BY iso_code;
-- End

/* 11. Mix of Peak and River Names */
SELECT
	peak_name,
    river_name,
    LOWER(CONCAT(peak_name, SUBSTRING(river_name, 2))) AS 'mix'
FROM
	peaks,
    rivers
WHERE LOWER(RIGHT(peak_name, 1)) = LOWER(LEFT(river_name, 1))
ORDER BY `mix`;
-- End

/* 12. Games From 2011 and 2012 Year */
USE diablo;
-- below is for Judge
SELECT 
	name, 
    DATE_FORMAT(`start`, '%Y-%m-%d') AS 'start'
FROM games
WHERE YEAR(`start`) BETWEEN 2011 and 2012
ORDER BY `start`
LIMIT 50;
-- End

/* 13. User Email Providers */
-- Option one with nested functions
SELECT 
	user_name,
    SUBSTRING(email, INSTR(email, '@') + 1) AS 'email provider'
FROM users
ORDER BY `email provider`, user_name;

-- Option two with single function
SELECT 
	user_name,
    SUBSTRING_INDEX(email, '@', -1) AS 'email provider' -- negative returns the right side of the delimiter
FROM users
ORDER BY `email provider`, user_name;
-- End

/* 14. Get Users with IP Address Like Pattern */
SELECT user_name, ip_address
FROM users
WHERE ip_address LIKE "___.1%.%.___"
ORDER BY user_name;
-- End

/* 15. Show All Games with Duration */
SELECT
	name AS 'game',
    CASE
		WHEN HOUR(`start`) BETWEEN 0 AND 11 THEN 'Morning'
		WHEN HOUR(`start`) BETWEEN 12 AND 17 THEN 'Afternoon'
        ELSE 'Evening'
    END AS 'Part of the Day',
    CASE
		WHEN duration <= 3 THEN 'Extra Short'
        WHEN duration BETWEEN 4 AND 6 THEN 'Short'
        WHEN duration BETWEEN 7 and 10 THEN 'Long'
        ELSE 'Extra Long'
    END AS 'Duration'
FROM games;
-- End

/* 16. Orders Table */
USE orders;
-- below is for Judge
SELECT 
	product_name,
    order_date,
    DATE_ADD(order_date, INTERVAL 3 DAY) AS 'pay_due',
    DATE_ADD(order_date, INTERVAL 1 MONTH) AS 'deliver_due'
FROM orders;
-- End
