USE soft_uni;

SELECT * FROM employees;

DELIMITER $ 

CREATE FUNCTION ufn_count_employees_by_town_lab() RETURNS INT
DETERMINISTIC
BEGIN
	DECLARE result INT;
	SET @result := (SELECT COUNT(*) FROM employees);
    RETURN @result;
END $

DELIMITER ;

SELECT ufn_count_employees_by_town_lab();

DELIMITER $ 

CREATE PROCEDURE ups_select_employees_by_seniority()
BEGIN
	SELECT * FROM employees
    WHERE DATE(hire_date) > '2002-01-01';
    
    SELECT employee_id, first_name FROM employees
    WHERE ROUND(DATEDIFF(NOW(), DATE(hire_date)) / 365.25, 0) < 20;
END $

DELIMITER ;

CALL ups_select_employees_by_seniority();
DROP PROCEDURE ups_select_employees_by_seniority;

/* 1. Count Employees by Town */
DELIMITER $ 

CREATE FUNCTION ufn_count_employees_by_town(town_name VARCHAR(50)) RETURNS INT
DETERMINISTIC
BEGIN
	DECLARE result INT;
	SET result := (SELECT COUNT(*) FROM employees e
					JOIN addresses a 
                    ON e.address_id = a.address_id
                    JOIN towns t
                    ON a.town_id = t.town_id
                    WHERE t.name = town_name);
    RETURN result;
END $

DELIMITER ;
SELECT ufn_count_employees_by_town('Sofia');
-- END

/* 2. Employees Promotion */
DELIMITER $ 

CREATE PROCEDURE usp_raise_salaries(department_name VARCHAR(50))
BEGIN
	UPDATE employees e 
    JOIN departments d
    ON e.department_id = d.department_id
    SET e.salary = e.salary * 1.05
    WHERE d.name = department_name;
END $

DELIMITER ;

SELECT e.employee_id, e.first_name, e.salary 
FROM employees e
JOIN departments d
    ON e.department_id = d.department_id
WHERE d.name = 'Finance'
ORDER BY first_name, salary;
CALL usp_raise_salaries('Finance');
-- END

/* 3. Employees Promotion By ID */
DELIMITER $
CREATE PROCEDURE usp_raise_salary_by_id(id INT)
BEGIN
	START TRANSACTION;
    IF((SELECT COUNT(*) FROM employees WHERE employee_id = id) <> 1) THEN
		ROLLBACK;
	ELSE
		UPDATE employees 
        SET salary = salary * 1.05 
        WHERE employee_id = id;
        COMMIT;
    END IF;
END $ 

DELIMITER ;

SELECT * FROM employees WHERE employee_id = 17;
CALL usp_raise_salary_by_id(17);
-- END

/* 4. Triggered */
CREATE TABLE deleted_employees(
employee_id INT PRIMARY KEY AUTO_INCREMENT,
first_name VARCHAR(20),
last_name VARCHAR(20),
middle_name VARCHAR(20),
job_title VARCHAR(50),
department_id INT,
salary DOUBLE
);

CREATE TRIGGER delete_employees_triger
AFTER DELETE 
ON employees
FOR EACH ROW
	INSERT INTO deleted_employees (first_name, last_name, middle_name, job_title, department_id, salary)
    VALUES (OLD.first_name, OLD.last_name, OLD.middle_name, OLD.job_title, OLD.department_id, OLD.salary);

DELETE FROM employees WHERE employee_id > 200;
SELECT * FROM deleted_employees;
-- END

