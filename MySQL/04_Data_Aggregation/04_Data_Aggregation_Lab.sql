USE restaurant;

SELECT * FROM departments;

SELECT *
FROM employees
GROUP BY department_id;

SELECT department_id, SUM(salary)
FROM employees
GROUP BY department_id;

SELECT COUNT(id) FROM employees;

SELECT * FROM hotel.clients;

-- COUNT skip if there is NULL, because it's not a valid info
SELECT COUNT(id) FROM hotel.clients;
SELECT COUNT(first_name) FROM hotel.clients;
SELECT COUNT(*) FROM hotel.clients; -- checks how many lines there is in a table

SELECT * FROM restaurant.test_null_values;

SELECT department_id, SUM(int_value) 
FROM test_null_values
GROUP BY department_id;

SELECT department_id, MAX(salary)
FROM employees
GROUP BY department_id;

SELECT department_id, MAX(salary)
FROM test_null_values
GROUP BY department_id;

SELECT department_id, MIN(salary)
FROM test_null_values
GROUP BY department_id;

SELECT department_id, AVG(salary)
FROM employees
GROUP BY department_id;

SELECT department_id, AVG(salary)
FROM test_null_values
GROUP BY department_id;

SELECT department_id, ROUND(MIN(salary), 2) AS 'Min Salary'
FROM employees
GROUP BY department_id
HAVING `Min Salary` > 800; -- HAVING is done after the grouping, while WHERE is before ( with it we can remove some values before the grouping )

SELECT COUNT(DISTINCT category_id)
FROM products;

/* 1. Departments Info */
SELECT 
	department_id, 
    COUNT(id) AS 'Number of employees'
FROM employees
GROUP BY department_id
ORDER BY department_id;
-- END

/* 2. Average Salary */
SELECT department_id, ROUND(AVG(salary), 2)
FROM employees
GROUP BY department_id;
-- END

/* 3. Minimum Salary */
SELECT department_id, ROUND(MIN(salary), 2) AS 'Min Salary'
FROM employees
GROUP BY department_id
HAVING `Min Salary` > 800;
-- END

/* 4. Appetizers Count */
-- SELECT * FROM categories;
SELECT COUNT(*)  
FROM products
WHERE category_id = 2 AND price > 8;
-- END

/* 5. Menu Prices */
SELECT
	category_id,
    ROUND(AVG(price), 2) AS 'Average Price',
    ROUND(MIN(price), 2) AS 'Cheapest Product',
    ROUND(MAX(price), 2) AS 'Most Expensive Product'
FROM products
GROUP BY category_id;
-- END
