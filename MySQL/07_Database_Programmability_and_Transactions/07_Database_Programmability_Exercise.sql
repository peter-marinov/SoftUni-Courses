USE soft_uni;

/* 01. Employees with Salary Above 35000 */
DELIMITER $

CREATE PROCEDURE usp_get_employees_salary_above_35000()
BEGIN
	SELECT first_name, last_name
	FROM employees
	WHERE salary > 35000
	ORDER BY first_name, last_name, employee_id;
END $

DELIMITER ;

CALL usp_get_employees_salary_above_35000();

-- END

/* 02. Employees with Salary Above Number */
DELIMITER $

CREATE PROCEDURE usp_get_employees_salary_above(salary DECIMAL(19, 4))
BEGIN
	SELECT e.first_name, e.last_name
    FROM employees e
    WHERE e.salary >= salary
    ORDER BY first_name, last_name, employee_id;
END $

DELIMITER ;

CALL usp_get_employees_salary_above(45000);
-- END

/* 03. Town Names Starting With */
DELIMITER $

CREATE PROCEDURE usp_get_towns_starting_with(string VARCHAR(50))
BEGIN
	SELECT name 
	FROM towns
	WHERE name LIKE CONCAT(string, '%')
    ORDER BY name;
END $

DELIMITER ;
CALL usp_get_towns_starting_with ('b');
CALL usp_get_towns_starting_with('ber');


-- END

/* 04. Employees from Town */
DELIMITER $

CREATE PROCEDURE usp_get_employees_from_town(town_name VARCHAR(50))
BEGIN
	SELECT e.first_name, e.last_name
	FROM employees e
	JOIN addresses a ON e.address_id =  a.address_id
	JOIN towns t ON a.town_id = t.town_id
	WHERE t.name = town_name
	ORDER BY e.first_name, e.last_name, e.employee_id;
END $

DELIMITER ;

CALL usp_get_employees_from_town('Sofia');

-- END

/* 05. Salary Level Function */
DELIMITER $

CREATE FUNCTION ufn_get_salary_level(target_salary DECIMAL(19,2)) RETURNS VARCHAR(50)
DETERMINISTIC
BEGIN
	DECLARE result VARCHAR(50);
	SET result := (CASE
						WHEN target_salary < 30000 THEN 'Low'
						WHEN target_salary <= 50000 THEN 'Average'
						ELSE 'High'
					END);
    RETURN result;
END $

DELIMITER ;

SELECT ufn_get_salary_level(100000);
-- END

/* 06. Employees by Salary Level */
DELIMITER $

CREATE PROCEDURE usp_get_employees_by_salary_level(salary_level VARCHAR(50))
BEGIN
	SELECT first_name, last_name
    FROM employees
    WHERE salary < 30000 AND salary_level = 'low'
		OR salary >= 30000 AND salary <= 50000 AND salary_level = 'average'
        OR salary > 50000 AND salary_level = 'high'
	ORDER BY first_name DESC, last_name DESC;
END $

CREATE PROCEDURE usp_get_employees_by_salary_level_new(salary_level VARCHAR(50))
BEGIN
	SELECT first_name, last_name
    FROM employees
    WHERE salary_level = ufn_get_salary_level(salary)
	ORDER BY first_name DESC, last_name DESC;
END $

DELIMITER ;

CALL usp_get_employees_by_salary_level_new('high');
-- END

/* 07. Define Function */
DELIMITER $

CREATE FUNCTION ufn_is_word_comprised(set_of_letters varchar(50), word varchar(50)) RETURNS BIT
DETERMINISTIC
BEGIN
	RETURN word REGEXP (CONCAT('^[', set_of_letters, ']+$'));
END $

DELIMITER ;

SELECT ufn_is_word_comprised('oistmiahf', 'Sofia');
SELECT ufn_is_word_comprised('oistmiahf', 'halves');
-- END

/* 08. Find Full Name */
SELECT * FROM accounts;
SELECT * FROM account_holders;
DELIMITER $

CREATE PROCEDURE usp_get_holders_full_name()
BEGIN
	SELECT CONCAT(first_name, ' ', last_name) AS full_name
    FROM account_holders
    ORDER BY full_name, id;
END $

DELIMITER ;

CALL usp_get_holders_full_name();

-- END

/* 9. People with Balance Higher Than */
DELIMITER $

CREATE PROCEDURE usp_get_holders_with_balance_higher_than(target_value INT)
BEGIN
	SELECT ah.first_name, ah.last_name
	FROM account_holders ah
	JOIN accounts a ON ah.id = a.account_holder_id
	GROUP BY ah.id
	HAVING SUM(a.balance) > target_value;
END $

DELIMITER ;

CALL usp_get_holders_with_balance_higher_than(7000);

-- END

/* 10. Future Value Function */
DELIMITER $

CREATE FUNCTION ufn_calculate_future_value(initial_sum DECIMAL(19, 4), yearly_interest_rate DOUBLE, years INT) RETURNS DECIMAL(19,4)
DETERMINISTIC
BEGIN
	RETURN initial_sum * POWER((1 + yearly_interest_rate), years);
END $

DELIMITER ;

SELECT ufn_calculate_future_value(1000, 0.5, 5);
-- END

/* 11. Calculating Interest */
-- ????
DELIMITER $

CREATE PROCEDURE usp_calculate_future_value_for_account(account_id INT, interest_rate DECIMAL(19, 4))
BEGIN
	SELECT 
		a.id AS account_id,
		ah.first_name,
		ah.last_name,
		a.balance AS 'current_balance',
		ufn_calculate_future_value(a.balance, interest_rate, 5) AS balance_in_5_years
	FROM accounts AS a
	JOIN account_holders AS ah ON a.account_holder_id = ah.id
	WHERE a.id = account_id;
END $


DELIMITER ;

SELECT * FROM account_holders;
SELECT * FROM accounts;

CALL usp_calculate_future_value_for_account(1, 0.1);

-- END

/* 12. Deposit Money */
DELIMITER $

CREATE PROCEDURE usp_deposit_money(account_id INT, money_amount DECIMAL(19, 4))
BEGIN
	IF money_amount > 0 THEN
		UPDATE accounts
        SET balance = balance + money_amount
        WHERE id = account_id;
        
        IF (SELECT balance
			FROM accounts
            WHERE id = account_id) < 0
            THEN ROLLBACK;
		ELSE
			COMMIT;
		END IF;
	END IF;
END $

DELIMITER ;
-- END

/* 13. Withdraw Money */
DELIMITER $

CREATE PROCEDURE usp_withdraw_money(account_id INT , money_amount DECIMAL(19,4))
BEGIN
	IF money_amount > 0 THEN
		START TRANSACTION;
        
		UPDATE accounts
        SET balance = balance - money_amount
        WHERE id = account_id;
        
        IF (SELECT balance FROM accounts WHERE id = account_id) < 0
			THEN ROLLBACK;
		ELSE
			COMMIT;
        END IF;
    END IF;
END $

DELIMITER ;

CALL usp_withdraw_money(1, 10);
select * from accounts
WHERE id = 1;
-- END

/* 14. Money Transfer */
DELIMITER $

CREATE PROCEDURE usp_transfer_money(from_account_id INT, to_account_id INT, amount DECIMAL(19,4))
BEGIN
	IF amount > 0
		AND (from_account_id IN(SELECT id FROM accounts)) 
        AND (to_account_id IN(SELECT id FROM accounts)) 
        AND from_account_id != to_account_id THEN
		START TRANSACTION;
        
        UPDATE accounts
        SET balance = balance - amount
        WHERE id = from_account_id;
        
        UPDATE accounts
        SET balance = balance + amount
        WHERE id = to_account_id;
        
        IF (SELECT amount FROM accounts WHERE id = from_account_id) < 0 THEN
			ROLLBACK;
		ELSE
			COMMIT;
        END IF;
    END IF;
END $

DELIMITER ;
-- END

/* 15. Log Accounts Trigger */
CREATE TABLE logs(
	log_id INT PRIMARY KEY AUTO_INCREMENT,
    account_id INT NOT NULL,
    old_sum DECIMAL(19, 4) NOT NULL,
    new_sum DECIMAL(19, 4) NOT NULL
);

DELIMITER $
CREATE TRIGGER balance_update_trigger
AFTER UPDATE ON accounts
FOR EACH ROW 
BEGIN
	IF OLD.balance <> NEW.balance THEN 
		INSERT INTO `logs` (account_id, old_sum, new_sum)
        VALUES (OLD.id, OLD.balance, NEW.balance);
	END IF;
END $

DELIMITER ;

CALL usp_transfer_money(1, 2, 10);
CALL usp_transfer_money(2, 1, 10);

SELECT * FROM logs;
-- END

/* 16. Emails Trigger */
CREATE TABLE notification_emails(
	id INT PRIMARY KEY AUTO_INCREMENT, 
    recipient INT NOT NULL,
    subject VARCHAR(50) NOT NULL, 
    body VARCHAR(255) NOT NULL
);

DELIMITER $

CREATE TRIGGER notification_emails_trigger
AFTER INSERT ON `logs`
FOR EACH ROW
BEGIN
	INSERT INTO notification_emails (recipient, subject, body)
    VALUES (
		NEW.account_id,
        CONCAT('Balance change for account: ', NEW.account_id),
        CONCAT('On ', DATE_FORMAT(NOW(), '%b %d %Y at %r'), ' your balance was changed from ', 
			ROUND(NEW.old_sum, 2), ' to ', ROUND(NEW.new_sum, 2), '.'));
END $

DELIMITER ;

SELECT * FROM notification_emails;
-- END




