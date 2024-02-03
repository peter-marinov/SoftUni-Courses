CREATE SCHEMA `real_estate` DEFAULT CHARACTER SET utf8 ;

USE real_estate;

CREATE TABLE cities(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE property_types(
	id INT PRIMARY KEY AUTO_INCREMENT,
    type VARCHAR(40) NOT NULL UNIQUE,
    description TEXT
);

CREATE TABLE properties(
	id INT PRIMARY KEY AUTO_INCREMENT,
    address VARCHAR(80) NOT NULL UNIQUE,
    price DECIMAL(19,2) NOT NULL,
    area DECIMAL(19,2),
    property_type_id INT,
    city_id INT,
    
    FOREIGN KEY (property_type_id) REFERENCES property_types(id),
    FOREIGN KEY (city_id) REFERENCES cities(id)
);

CREATE TABLE agents(
	id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(40) NOT NULL,
    phone VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(50) NOT NULL UNIQUE,
    city_id INT,
    
    FOREIGN KEY (city_id) REFERENCES cities(id)
);

CREATE TABLE buyers(
	id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(40) NOT NULL,
    phone VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(50) NOT NULL UNIQUE,
    city_id INT,
    
    FOREIGN KEY (city_id) REFERENCES cities(id)
);

CREATE TABLE property_offers(
	property_id INT NOT NULL,
    agent_id INT NOT NULL,
    price DECIMAL(19,2) NOT NULL,
    offer_datetime DATETIME,
    
    KEY(property_id, agent_id),
    FOREIGN KEY (property_id) REFERENCES properties(id),
    FOREIGN KEY (agent_id) REFERENCES agents(id)
);

CREATE TABLE property_transactions(
	id INT PRIMARY KEY AUTO_INCREMENT,
    property_id INT NOT NULL,
    buyer_id INT NOT NULL,
    transaction_date DATE,
    bank_name VARCHAR(30),
    iban VARCHAR(40) UNIQUE,
    is_successful TINYINT(1),
    
    FOREIGN KEY (property_id) REFERENCES properties(id),
    FOREIGN KEY (buyer_id) REFERENCES buyers(id)
);

/* 02. Insert */
INSERT INTO property_transactions(property_id, buyer_id, transaction_date, bank_name, iban, is_successful)
SELECT 
	agent_id + DAY(offer_datetime),
	agent_id + MONTH(offer_datetime),
    DATE(offer_datetime),
    CONCAT('Bank ', agent_id),
    CONCAT('BG', price, agent_id),
    1
FROM property_offers
WHERE agent_id <= 2;

/* 03. Update */
UPDATE properties
SET price = price - 50000
WHERE price >= 800000;

/* 04. Delete */
DELETE FROM property_transactions WHERE is_successful = 0;

/* 05. Agents */
SELECT id, first_name, last_name, phone, email, city_id 
FROM agents
ORDER BY city_id DESC, phone DESC;

/* 06. Offers from 2021 */
SELECT property_id, agent_id, price, offer_datetime
FROM property_offers
WHERE YEAR(offer_datetime) = 2021
ORDER BY price
LIMIT 10;

/* 07. Properties without offers */
SELECT
	SUBSTRING(address, 1, 6) AS agent_name,
    CHAR_LENGTH(address) * 5430 AS `price`
FROM properties
WHERE id NOT IN (SELECT property_id FROM property_offers)
ORDER BY agent_name DESC, `price` DESC;

/* 08. Best Banks */
SELECT 
	bank_name,
    COUNT(iban) AS count
FROM property_transactions
GROUP BY bank_name
HAVING count >= 9
ORDER BY count DESC, bank_name;

/* 09. Size of the area */
SELECT
	address,
    area,
    CASE
		WHEN area <= 100 THEN 'small'
        WHEN area <= 200 THEN 'medium'
        WHEN area <= 500 THEN 'large'
        ELSE 'extra large'
    END AS size
FROM properties
ORDER BY area, address DESC;

/* 10. Offers count in a city */
DELIMITER $
CREATE FUNCTION udf_offers_from_city_name (cityName VARCHAR(50))
RETURNS INT
DETERMINISTIC
BEGIN
	DECLARE result INT;
    SET result = (
			SELECT COUNT(*)
			FROM cities c
			JOIN properties p ON c.id = p.city_id
			JOIN property_offers po ON p.id = po.property_id
			WHERE c.name = cityName);
	RETURN result;
END $
DELIMITER ;

SELECT udf_offers_from_city_name('Vienna') AS 'offers_count';

/* 11. Special Offer */
DELIMITER $
CREATE PROCEDURE udp_special_offer(first_name VARCHAR(50))
BEGIN
	UPDATE property_offers po
    JOIN agents a ON po.agent_id = a.id
    SET po.price = po.price * 0.9
    WHERE a.first_name = first_name;
END $

DELIMITER ;
SELECT * FROM agents;
SELECT * FROM property_offers;

SELECT * 
FROM agents a
JOIN property_offers po ON a.id = po.agent_id
WHERE a.first_name = 'Hans';
