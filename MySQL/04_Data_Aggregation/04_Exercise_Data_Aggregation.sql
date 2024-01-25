USE gringotts;

/* 1. Records' Count */
SELECT COUNT(*) AS 'count' FROM wizzard_deposits;
-- END

/* 02. Longest Magic Wand */
SELECT MAX(magic_wand_size) AS 'longest_magic_wand' FROM wizzard_deposits;
-- END

/* 03. Longest Magic Wand per Deposit Groups */
SELECT
	deposit_group,
    MAX(magic_wand_size) AS 'longest_magic_wand'
FROM wizzard_deposits
GROUP BY deposit_group
ORDER BY `longest_magic_wand`, deposit_group;
-- END

/* 04. Smallest Deposit Group per Magic Wand Size */
SELECT deposit_group
FROM wizzard_deposits
GROUP BY deposit_group
ORDER BY AVG(magic_wand_size)
LIMIT 1;
-- END

/* 05. Deposits Sum */
SELECT
	deposit_group,
    SUM(deposit_amount) AS 'total_sum'
FROM wizzard_deposits
GROUP BY deposit_group
ORDER BY `total_sum`;
-- END

/* 06. Deposits Sum for Ollivander Family */
SELECT
	deposit_group,
    SUM(deposit_amount) AS 'total_sum'
FROM wizzard_deposits
WHERE magic_wand_creator = 'Ollivander family'
GROUP BY deposit_group
ORDER BY deposit_group;
-- END

/* 07. Deposits Filter */
SELECT
	deposit_group,
    SUM(deposit_amount) AS 'total_sum'
FROM wizzard_deposits
WHERE magic_wand_creator = 'Ollivander family'
GROUP BY deposit_group
HAVING `total_sum` < 150000
ORDER BY `total_sum` DESC;
-- END

/* 8. Deposit Charge */
SELECT
	deposit_group,
    magic_wand_creator,
    MIN(deposit_charge)
FROM wizzard_deposits
GROUP BY
	deposit_group, 
    magic_wand_creator
ORDER BY magic_wand_creator, deposit_group;
-- END

/* 09. Age Groups */
SELECT
	CASE
		WHEN age <= 10 THEN '[0-10]'
		WHEN age <= 20 THEN '[11-20]'
		WHEN age <= 30 THEN '[21-30]'
		WHEN age <= 40 THEN '[31-40]'
		WHEN age <= 50 THEN '[41-50]'
		WHEN age <= 60 THEN '[51-60]'
        ELSE '[61+]'
    END AS 'age_group',
    COUNT(*) AS 'wizard_count'
FROM wizzard_deposits
GROUP BY `age_group`
ORDER BY `age_group`;
-- END

/* 10. First Letter */
SELECT
	LEFT(first_name, 1) AS 'first_letter'
FROM wizzard_deposits
WHERE deposit_group = 'Troll Chest'
GROUP BY `first_letter`
ORDER BY `first_letter`;
-- END

/* 11. Average Interest */
SELECT 
	deposit_group,
    is_deposit_expired,
    AVG(deposit_interest) AS 'average_interest'
FROM wizzard_deposits
WHERE deposit_start_date > '1985-01-01'
GROUP BY deposit_group, is_deposit_expired
ORDER BY deposit_group DESC, is_deposit_expired;
-- END

/* 12. Employees Minimum Salaries */
USE soft_uni;
-- below is for Judge
SELECT
	department_id,
    MIN(salary) AS 'minimum_salary'
FROM employees
WHERE department_id in (2, 5, 7)
GROUP BY department_id
ORDER BY department_id;
-- END

/* 13. Employees Average Salaries */
SELECT
	department_id,
    CASE
		WHEN department_id = 1 THEN AVG(salary) + 5000
        ELSE AVG(salary)
    END AS 'avg_salary'
FROM employees
WHERE salary > 30000 and manager_id != 42
GROUP BY department_id
ORDER BY department_id;

-- other solution
CREATE TABLE highest_paid_employees AS
SELECT * FROM employees
WHERE salary > 30000;

DELETE FROM highest_paid_employees
WHERE manager_id = 42;

UPDATE highest_paid_employees
SET salary = salary + 5000
WHERE department_id = 1;

SELECT
	department_id,
	AVG(salary) AS 'avg_salary'
FROM highest_paid_employees
GROUP BY department_id
ORDER BY department_id;
-- END

/* 14. Employees Maximum Salaries */
SELECT 
	department_id,
    MAX(salary) AS 'max_salary'
FROM employees
GROUP BY department_id
HAVING `max_salary` NOT BETWEEN 30000 AND 70000
ORDER BY department_id;
-- END

/* 15. Employees Count Salaries */
SELECT COUNT(salary) AS ''
FROM employees
WHERE manager_id IS NULL;
-- END

/* 16. 3rd Highest Salary */
SELECT 
	e.department_id,
    (
		SELECT DISTINCT salary
		FROM employees
		WHERE e.department_id = department_id
		ORDER BY salary DESC
		LIMIT 1 OFFSET 2 -- OFFSET skip number of lines
    ) AS 'third_highest_salary'
FROM employees AS e
GROUP BY e.department_id
HAVING `third_highest_salary` IS NOT NULL
ORDER BY e.department_id;
-- END

/* 17. Salary Challenge */
SELECT
	e.first_name,
    e.last_name,
    e.department_id
FROM employees e
WHERE salary > (SELECT AVG(salary)
				FROM employees
                WHERE e.department_id = department_id
                )
-- GROUP BY department_id
ORDER BY department_id, employee_id
LIMIT 10;
-- END

/* 18. Departments Total Salaries */
SELECT
	department_id,
    SUM(salary) AS 'total_salary'
FROM employees
GROUP BY department_id
ORDER BY department_id;
-- END
