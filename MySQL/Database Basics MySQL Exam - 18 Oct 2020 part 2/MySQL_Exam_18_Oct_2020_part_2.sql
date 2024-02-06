CREATE SCHEMA `triple_s` DEFAULT CHARACTER SET utf8 ;

USE triple_s;


CREATE TABLE pictures(
	id INT PRIMARY KEY AUTO_INCREMENT,
    url VARCHAR(100) NOT NULL,
    added_on DATETIME NOT NULL
);

CREATE TABLE categories(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL UNIQUE
);

CREATE TABLE products(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL UNIQUE,
    best_before DATE,
    price DECIMAL(10,2) NOT NULL,
    description TEXT,
    category_id INT NOT NULL,
    picture_id INT NOT NULL,
    
    FOREIGN KEY (category_id) REFERENCES categories(id),
    FOREIGN KEY (picture_id) REFERENCES pictures(id)
);

CREATE TABLE towns(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE addresses(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE,
    town_id INT NOT NULL,
    
    FOREIGN KEY (town_id) REFERENCES towns(id)
);

CREATE TABLE stores(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL UNIQUE,
    rating FLOAT NOT NULL,
    has_parking TINYINT(1) DEFAULT 0,
    address_id INT NOT NULL,
    
    FOREIGN KEY (address_id) REFERENCES addresses(id)
);

CREATE TABLE products_stores(
	product_id INT NOT NULL,
    store_id INT NOT NULL,
    
    PRIMARY KEY (product_id, store_id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (store_id) REFERENCES stores(id)
);

CREATE TABLE employees(
	id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(15) NOT NULL,
    middle_name CHAR(1),
    last_name VARCHAR(20) NOT NULL,
    salary DECIMAL(19,2) DEFAULT 0,
    hire_date DATE NOT NULL,
    manager_id INT,
    store_id INT NOT NULL,
    
    FOREIGN KEY (manager_id) REFERENCES employees(id),
    FOREIGN KEY (store_id) REFERENCES stores(id)
);

/* 02. Insert */
INSERT INTO products_stores(product_id, store_id)
SELECT
	id,
    1
FROM products
WHERE id NOT IN(SELECT product_id FROM products_stores);

/* 03. Update */
UPDATE employees
SET manager_id = 3,
	salary = salary - 500
WHERE YEAR(hire_date) > 2003 AND store_id NOT IN (SELECT id FROM stores WHERE name IN ('Cardguard', 'Veribet'));

/* 04. Delete */
DELETE e FROM employees e
JOIN employees m ON e.manager_id = m.id
WHERE e.manager_id IS NOT NULL AND e.salary > 6000;

/* 05. Employees */
SELECT first_name, middle_name, last_name, salary, hire_date
FROM employees
ORDER BY hire_date DESC;

/* 06. Products with old pictures */
SELECT
	p.name,
    p.price,
    p.best_before,
    CONCAT(SUBSTRING(p.description, 1, 10), '...') AS short_description,
	pic.url
FROM products p
JOIN pictures pic ON p.picture_id = pic.id
WHERE CHAR_LENGTH(p.description) > 100 AND YEAR(pic.added_on) < 2019 AND p.price > 20
ORDER BY p.price DESC;

/* 07. Counts of products in stores */
SELECT
	s.name,
    COUNT(p.id) AS product_count,
    ROUND(AVG(p.price), 2) AS `avg`
FROM stores s 
LEFT JOIN products_stores ps ON s.id = ps.store_id
LEFT JOIN products p ON ps.product_id = p.id
GROUP BY s.id
ORDER BY product_count DESC, `avg` DESC, s.id;


SELECT * FROM stores WHERE id NOT IN (SELECT store_id FROM products_stores);

/* 08. Specific employee */
SELECT
	CONCAT(e.first_name, ' ', e.last_name) AS Full_name,
    s.name AS Store_name,
    a.name AS address,
    e.salary
FROM employees e
JOIN stores s ON e.store_id = s.id
JOIN addresses a ON s.address_id = a.id
WHERE e.salary < 4000 AND a.name LIKE '%5%' AND CHAR_LENGTH(s.name) > 8 AND e.last_name LIKE '%n';

/* 09. Find all information of stores */
SELECT
	REVERSE(s.name) AS `reveresd_name`,
    CONCAT(UPPER(t.name), '-', a.name) AS full_address,
    COUNT(e.id) AS employees_count
FROM stores s
JOIN addresses a ON s.address_id = a.id
JOIN towns t ON a.town_id = t.id
JOIN employees e ON s.id = e.store_id
GROUP BY s.name
ORDER BY full_address;

/* 10. Find name of top paid employee by store name */
DELIMITER $
CREATE FUNCTION udf_top_paid_employee_by_store(store_name VARCHAR(50))
RETURNS VARCHAR(255)
DETERMINISTIC
BEGIN
	DECLARE result VARCHAR(255);
    SET result = (
				SELECT CONCAT(e.first_name, ' ', e.middle_name,'. ', e.last_name, ' works in store for ', TIMESTAMPDIFF(year, e.hire_date, '2020-10-18'),' years')
				FROM stores s
				JOIN employees e ON s.id = e.store_id
				WHERE s.name = store_name AND e.salary = (SELECT MAX(salary) FROM employees WHERE store_id = s.id));
    RETURN result;
END $
DELIMITER ;

/* 11. Update product price by address */
DELIMITER $
CREATE PROCEDURE udp_update_product_price(address_name VARCHAR (50))
BEGIN
	DECLARE amount INT;
    IF LEFT(address_name, 1) = '0' THEN
		SET amount = 100;
	ELSE
		SET amount = 200;
	END IF;
    
	UPDATE products p
    JOIN products_stores ps ON p.id = ps.product_id
    JOIN stores s ON ps.store_id = s.id
    JOIN addresses a ON s.address_id = a.id
    SET p.price = p.price + amount
	WHERE a.name = address_name;
    
END $
DELIMITER ;




