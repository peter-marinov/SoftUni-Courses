CREATE SCHEMA `royal_united_kingsman` DEFAULT CHARACTER SET utf8 ;

USE royal_united_kingsman;

CREATE TABLE branches(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL UNIQUE
);

CREATE TABLE employees(
	id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    started_on DATE NOT NULL,
    branch_id INT NOT NULL,
    
    FOREIGN KEY (branch_id) REFERENCES branches(id)
);

CREATE TABLE clients(
	id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(50) NOT NULL,
    age INT NOT NULL
);

CREATE TABLE employees_clients(
	employee_id INT,
    client_id INT,
    
    KEY (employee_id, client_id),
    FOREIGN KEY (employee_id) REFERENCES employees(id),
    FOREIGN KEY (client_id) REFERENCES clients(id)
);

CREATE TABLE bank_accounts(
	id INT PRIMARY KEY AUTO_INCREMENT,
    account_number VARCHAR(10) NOT NULL,
    balance DECIMAL(10,2) NOT NULL,
    client_id INT NOT NULL UNIQUE,
    
	FOREIGN KEY (client_id) REFERENCES clients(id)
);

CREATE TABLE cards(
	id INT PRIMARY KEY AUTO_INCREMENT,
    card_number VARCHAR(19) NOT NULL,
    card_status VARCHAR(7) NOT NULL,
    bank_account_id INT NOT NULL,
    
    FOREIGN KEY (bank_account_id) REFERENCES bank_accounts(id)
);


/* 02. Insert */
INSERT INTO cards(card_number, card_status, bank_account_id)
SELECT
	REVERSE(full_name),
    'Active',
    id
FROM clients
WHERE id BETWEEN 191 and 200;

/* 03. Update */
UPDATE employees_clients AS ec
    JOIN
    (SELECT ec1.employee_id, COUNT(ec1.client_id) AS 'count'
     FROM employees_clients AS ec1
     GROUP BY ec1.employee_id
     ORDER BY count, ec1.employee_id) AS s
SET ec.employee_id = s.employee_id
WHERE ec.employee_id = ec.client_id;

/* 04. Delete */
DELETE FROM employees
WHERE id NOT IN (SELECT employee_id FROM employees_clients);

/* 05. Clients */
SELECT id, full_name
FROM clients
ORDER by id;

/* 06. Newbies */
SELECT
	id,
    CONCAT(first_name, ' ', last_name) AS full_name,
    CONCAT('$', salary) AS salary,
    started_on
FROM employees
WHERE salary >= 100000 AND started_on >= '2018-01-01'
ORDER BY salary DESC, id;

/* 07. Cards against Humanity */
SELECT
	c.id,
	CONCAT(c.card_number, ' : ', cl.full_name) AS card_token
FROM cards c
JOIN bank_accounts ba ON c.bank_account_id = ba.id
JOIN clients cl ON ba.client_id = cl.id
ORDER BY c.id DESC;

/* 08. Top 5 Employees */
SELECT 
	CONCAT(e.first_name, ' ', e.last_name) AS `name`,
	e.started_on,
    COUNT(*) AS count_of_clients
FROM employees e
JOIN employees_clients ec ON e.id = ec.employee_id
GROUP BY e.id
ORDER BY count_of_clients DESC, e.id
LIMIT 5;

/* 09. Branch cards */
SELECT
	b.name, 
	COUNT(ca.id) AS count_of_cards
FROM branches b
LEFT JOIN employees e ON b.id = e.branch_id
LEFT JOIN employees_clients ec ON e.id = ec.employee_id
LEFT JOIN clients c ON ec.client_id = c.id
LEFT JOIN bank_accounts ba ON c.id = ba.client_id
LEFT JOIN cards ca ON ba.id = ca.bank_account_id
GROUP BY b.name
ORDER BY count_of_cards DESC, b.name;

SELECT * FROM branches WHERE id NOT IN ( SELECT branch_id FROM employees);

/* 10. Extract card's count */
DELIMITER $
CREATE FUNCTION udf_client_cards_count(name VARCHAR(30))
RETURNS INT
BEGIN
	RETURN (
		SELECT COUNT(*)
        FROM clients c
        JOIN bank_accounts ba ON c.id = ba.client_id
        JOIN cards ca ON ba.id = ca.bank_account_id
        WHERE c.full_name = name
    );
END $
DELIMITER ;

/* 11. Client Info */
DELIMITER $
CREATE PROCEDURE udp_clientinfo(full_name VARCHAR(50))
BEGIN
	SELECT
		c.full_name,
        c.age,
        ba.account_number,
        CONCAT('$', ba.balance) AS balance
	FROM clients c
    JOIN bank_accounts ba ON c.id = ba.client_id
    WHERE c.full_name = full_name;
END $
DELIMITER ;


