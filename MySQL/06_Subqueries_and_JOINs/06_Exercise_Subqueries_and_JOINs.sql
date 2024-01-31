USE soft_uni;

/* 01. Employee Address */
SELECT
	e.employee_id,
    e.job_title,
    e.address_id,
    a.address_text
FROM employees AS e
	JOIN addresses AS a ON e.address_id = a.address_id
ORDER BY e.address_id
LIMIT 5;
-- END

/* 02. Addresses with Towns */
SELECT 
	e.first_name,
    e.last_name,
    t.name AS 'town',
    a.address_text
FROM employees AS e
	JOIN addresses AS a ON e.address_id = a.address_id
    JOIN towns AS t ON a.town_id = t.town_id
ORDER BY e.first_name, e.last_name
LIMIT 5;
-- END

/* 03. Sales Employee */
SELECT
	e.employee_id,
    e.first_name,
    e.last_name,
    d.name AS 'department_name'
FROM employees AS e
	JOIN departments AS d ON e.department_id = d.department_id AND d.name = 'Sales'
ORDER BY e.employee_id DESC;
-- END

/* 04. Employee Departments */
SELECT 
	e.employee_id,
    e.first_name,
    e.salary,
    d.name AS 'department_name'
FROM employees AS e
JOIN departments AS d ON e.department_id = d.department_id
WHERE e.salary > 15000
ORDER BY d.department_id DESC
LIMIT 5;
-- END

/* 05. Employees Without Project */
SELECT
	e.employee_id,
    e.first_name
FROM employees AS e
	LEFT JOIN employees_projects AS ep ON e.employee_id = ep.employee_id
WHERE ep.project_id IS NULL
ORDER BY e.employee_id DESC
LIMIT 3;
-- other solution
SELECT
	e.employee_id,
    e.first_name
FROM employees AS e
WHERE e.employee_id NOT IN (SELECT ep.employee_id FROM employees_projects AS ep )
ORDER BY e.employee_id DESC
LIMIT 3;
-- END

/* 06. Employees Hired After */
SELECT 
	e.first_name,
    e.last_name,
    e.hire_date,
    d.name AS 'dept_name'
FROM employees AS e
	JOIN departments AS d ON e.department_id = d.department_id
WHERE e.hire_date > '1999-01-01' AND d.name IN ('Sales', 'Finance')
ORDER BY e.hire_date;
-- END

/* 07. Employees with Project */
SELECT
	e.employee_id,
    e.first_name,
    p.name AS 'project_name'
FROM employees AS e
	JOIN employees_projects AS ep ON e.employee_id = ep.employee_id
    JOIN projects AS p ON ep.project_id = p.project_id
WHERE DATE(p.start_date) > '2002-08-13' AND p.end_date IS NULL
ORDER BY e.first_name, project_name
LIMIT 5;
-- END

/* 08. Employee 24 */
SELECT 
	e.employee_id,
    e.first_name,
    CASE
		WHEN YEAR(p.start_date) >= '2005' THEN NULL
        ELSE p.name
    END AS 'project_name'
FROM employees AS e
	JOIN employees_projects AS ep ON e.employee_id = ep.employee_id
    JOIN projects AS p ON ep.project_id = p.project_id
WHERE e.employee_id = 24
ORDER BY p.name;
-- END

/* 09. Employee Manager */
SELECT 
	e.employee_id,
    e.first_name,
    e.manager_id,
    em.first_name AS 'manager_name'
FROM employees AS e
	JOIN employees AS em ON e.manager_id = em.employee_id
WHERE e.manager_id IN (3, 7)
ORDER BY e.first_name;
-- END

/* 10. Employee Summary */
SELECT 
	e.employee_id,
    CONCAT_WS(' ', e.first_name, e.last_name) AS 'employee_name',
    CONCAT_WS(' ', em.first_name, em.last_name) AS 'manager_name',
    d.name AS 'department_name'
FROM employees AS e
	JOIN employees AS em ON e.manager_id = em.employee_id
	JOIN departments AS d ON e.department_id = d.department_id
ORDER BY e.employee_id
LIMIT 5;
-- END

/* 11. Min Average Salary */
SELECT
	AVG(salary) AS 'min_average_salary'
FROM employees AS e
GROUP BY e.department_id
ORDER BY min_average_salary
LIMIT 1;
-- END

USE geography;

/* 12. Highest Peaks in Bulgaria */
SELECT
	c.country_code,
    m.mountain_range,
    p.peak_name,
    p.elevation
FROM countries AS c
	JOIN mountains_countries AS mc ON c.country_code = mc.country_code
    JOIN mountains AS m ON mc.mountain_id = m.id
    JOIN peaks AS p ON m.id = p.mountain_id
WHERE c.country_name = 'Bulgaria' AND p.elevation > 2835
ORDER BY p.elevation DESC;
-- END

/* 13. Count Mountain Ranges */
SELECT
	c.country_code,
    COUNT(*) AS 'mountain_range'
FROM countries AS c
	JOIN mountains_countries AS mc ON c.country_code = mc.country_code
    JOIN mountains AS m ON mc.mountain_id = m.id
WHERE c.country_name IN ('United States', 'Russia', 'Bulgaria')
GROUP BY c.country_code
ORDER BY `mountain_range` DESC;
-- END

/* 14. Countries with Rivers */
SELECT
	c.country_name,
    r.river_name
FROM countries AS c
	JOIN continents AS con ON c.continent_code = con.continent_code
	LEFT JOIN countries_rivers AS cr ON c.country_code = cr.country_code
    LEFT JOIN rivers AS r ON cr.river_id = r.id
WHERE con.continent_name = 'Africa'
ORDER BY c.country_name
LIMIT 5;
-- END

/* 15. *Continents and Currencies */
SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
SELECT @@sql_mode;
SELECT 
    c.continent_code,
    c.currency_code,
    COUNT(*) AS currency_usage
FROM
    countries AS c
GROUP BY c.continent_code , c.currency_code
HAVING currency_usage > 1 AND currency_usage = (SELECT 
        COUNT(*) AS max_usage
    FROM
        countries
    WHERE
        continent_code = c.continent_code
    GROUP BY currency_code
    ORDER BY max_usage DESC
    LIMIT 1)
ORDER BY c.continent_code;
-- END

/* 16. Countries without any Mountains */
SELECT 
	COUNT(*) AS country_count
FROM countries AS c
	LEFT JOIN mountains_countries AS mc ON c.country_code = mc.country_code
WHERE mc.country_code IS NULL;
-- END

/* 17. Highest Peak and Longest River by Country */
SELECT
	c.country_name,
    MAX(p.elevation) AS highest_peak_elevation,
    MAX(r.length) AS longest_river_length
FROM countries AS c
	JOIN mountains_countries AS mc ON c.country_code = mc.country_code
    JOIN mountains AS m ON mc.mountain_id = m.id
    JOIN peaks AS p ON m.id = p.mountain_id
    JOIN countries_rivers AS cr ON c.country_code = cr.country_code
    JOIN rivers AS r ON cr.river_id = r.id
GROUP BY c.country_name
ORDER BY highest_peak_elevation DESC, longest_river_length DESC
LIMIT 5;
-- END

