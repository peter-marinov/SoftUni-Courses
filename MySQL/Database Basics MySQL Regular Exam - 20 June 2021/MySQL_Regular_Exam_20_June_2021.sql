CREATE SCHEMA `taxi_company` DEFAULT CHARACTER SET utf8 ;

USE taxi_company;

CREATE TABLE addresses(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE categories(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(10) NOT NULL
);

CREATE TABLE clients(
	id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20) NOT NULL
);

CREATE TABLE drivers(
	id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    age INT NOT NULL,
    rating FLOAT DEFAULT 5.5
);

CREATE TABLE cars(
	id INT PRIMARY KEY AUTO_INCREMENT,
    make VARCHAR(20) NOT NULL,
    model VARCHAR(20),
    year INT DEFAULT 0 NOT NULL,
    mileage INT DEFAULT 0,
    `condition` CHAR(1) NOT NULL,
    category_id INT NOT NULL,
    
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

CREATE TABLE courses(
	id INT PRIMARY KEY AUTO_INCREMENT,
    from_address_id INT NOT NULL,
    start DATETIME NOT NULL,
    bill DECIMAL(10,2) DEFAULT 10,
    car_id INT NOT NULL,
    client_id INT NOT NULL,
    
    FOREIGN KEY (from_address_id) REFERENCES addresses(id),
    FOREIGN KEY (car_id) REFERENCES cars(id),
    FOREIGN KEY (client_id) REFERENCES clients(id)
);

CREATE TABLE cars_drivers(
	car_id INT NOT NULL,
    driver_id INT NOT NULL,
    
    PRIMARY KEY(car_id, driver_id),
    FOREIGN KEY (car_id) REFERENCES cars(id),
    FOREIGN KEY (driver_id) REFERENCES drivers(id)
);

/* 02. Insert */
INSERT INTO clients(full_name, phone_number)
SELECT
	CONCAT(first_name, ' ', last_name),
    CONCAT('(088) 9999', id * 2)
FROM drivers
WHERE id BETWEEN 10 and 20;

/* 03. Update */
UPDATE cars
SET `condition` = 'C'
WHERE (mileage >= 800000 OR mileage IS NULL) AND `year` <= 2010 AND make <> 'Mercedes-Benz';

/* 04. Delete */
DELETE FROM clients
WHERE id NOT IN (SELECT client_id FROM courses)AND CHAR_LENGTH(full_name) > 3;

/* 05. Cars */
SELECT make, model, `condition`
FROM cars
ORDER BY id;

/* 06. Drivers and Cars */
SELECT
	d.first_name, 
    d.last_name,
    c.make,
    c.model,
    c.mileage
FROM drivers d
JOIN cars_drivers cd ON d.id = cd.driver_id
JOIN cars c ON cd.car_id = c.id
WHERE c.mileage IS NOT NULL
ORDER BY c.mileage DESC, d.first_name;

/* 07. Number of courses */
SELECT 
	c.id AS car_id,
    c.make,
    c.mileage,
    COUNT(co.bill) AS count_of_courses,
    ROUND(AVG(co.bill), 2) AS avg_bill
FROM cars c
LEFT JOIN courses co ON c.id = co.car_id
GROUP BY c.id
HAVING count_of_courses <> 2
ORDER BY count_of_courses DESC, car_id;

SELECT * FROM cars;

/* 08. Regular clients */
SELECT
	c.full_name,
    COUNT(co.car_id) AS count_of_cars,
    SUM(co.bill) AS total_sum
FROM clients c
JOIN courses co ON c.id = co.client_id
WHERE SUBSTRING(c.full_name, 2, 1) = 'a'
GROUP BY c.id
HAVING count_of_cars > 1
ORDER BY c.full_name;

/* 09. Full info for courses */
SELECT
	a.name,
    CASE
		WHEN HOUR(c.`start`) BETWEEN 6 AND 20 THEN 'Day'
        ELSE 'Night'
    END AS day_time,
    c.bill,
    cl.full_name,
    ca.make,
    ca.model,
    cat.name AS category_name
FROM courses c
JOIN addresses a ON c.from_address_id = a.id
JOIN clients cl ON c.client_id = cl.id
JOIN cars ca ON c.car_id = ca.id
JOIN categories cat ON ca.category_id = cat.id
ORDER BY c.id;


/* 10. Find all courses by client’s phone number */
DELIMITER $
CREATE FUNCTION udf_courses_by_client (phone_num VARCHAR (20))
RETURNS INT
DETERMINISTIC
BEGIN
	DECLARE result INT;
    SET result = (
				SELECT COUNT(*)
                FROM clients c
                JOIN courses co ON c.id = co.client_id
                WHERE c.phone_number = phone_num);
    RETURN result;
END $

DELIMITER ;

/* 11. Full info for address */
DELIMITER $
CREATE PROCEDURE udp_courses_by_address(address_name VARCHAR(100))
BEGIN
	SELECT 
	a.name,
    cl.full_name,
    CASE
		WHEN c.bill <= 20 THEN 'Low'
		WHEN c.bill <= 30 THEN 'Medium'
        ELSE 'High'
    END AS level_of_bill,
    ca.make,
    ca.`condition`,
    cat.name AS cat_name
	FROM addresses a
	JOIN courses c ON a.id = c.from_address_id
	JOIN clients cl ON c.client_id = cl.id
	JOIN cars ca ON c.car_id = ca.id
	JOIN categories cat ON ca.category_id = cat.id
	WHERE a.name = address_name
	ORDER BY ca.make, cl.full_name;
END $
DELIMITER ;
