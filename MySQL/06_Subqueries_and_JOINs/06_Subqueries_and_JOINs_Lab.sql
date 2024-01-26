USE hotel;

SELECT * 
FROM employees
	JOIN departments ON employees.department_id = departments.id;
    
SELECT * 
FROM employees
	JOIN departments;
    
SELECT employee_id, first_name FROM employees

UNION

SELECT department_id, name FROM departments;

SELECT * FROM departments;

SELECT
	CONCAT(first_name, ' ', last_name) AS 'full_name'
FROM departments AS d
	JOIN employees AS e ON e.employee_id = d.manager_id
WHERE name IN ('Sales', 'Marketing');


SELECT
	CONCAT(first_name, ' ', last_name) AS 'full_name'
FROM departments AS d
	JOIN employees AS e ON e.employee_id = d.manager_id
WHERE d.department_id IN (
	SELECT department_id FROM departments
    WHERE name in ('Sales', 'Marketing')
);

SELECT AVG(address_id)
FROM employees
WHERE employee_id > (SELECT AVG(address_id) FROM employees);

SELECT 
	e.employee_id,
    e.first_name,
    e.last_name,
    ep.project_id
FROM employees AS e
	JOIN employees_projects AS ep ON e.employee_id = ep.employee_id
    JOIN projects AS p on ep.project_id = p.project_id
ORDER BY e.employee_id;

/* 1. Managers */
SELECT
	employee_id,
   CONCAT_WS(' ', first_name, last_name) AS `full_name`,
   departments.department_id,
    name AS `department_name`
FROM departments
	JOIN employees ON departments.manager_id = employees.employee_id
ORDER BY employee_id
LIMIT 5;
-- END

/* 2. Towns and Addresses */
SELECT 
	t.town_id,
    t.name AS `town_name`,
    a.address_text
FROM towns AS t
	JOIN addresses AS a ON t.town_id = a.town_id
WHERE t.name in ('San Francisco', 'Sofia', 'Carnation')
ORDER BY t.town_id, a.address_id;
--
SELECT 
	t.town_id,
    t.name AS `town_name`,
    a.address_text
FROM towns AS t
	JOIN addresses AS a 
    ON t.town_id = a.town_id AND t.name in ('San Francisco', 'Sofia', 'Carnation')
ORDER BY t.town_id, a.address_id;
-- END

/* 3. Employees Without Managers */
SELECT 
	e.employee_id,
    e.first_name,
    e.last_name,
    e.department_id,
    e.salary
FROM employees AS e
WHERE e.manager_id IS NULL;
-- END

/* 4. High Salary */
SELECT COUNT(*) AS 'count'
FROM employees
WHERE salary > (
	SELECT AVG(salary) FROM employees
);
-- END