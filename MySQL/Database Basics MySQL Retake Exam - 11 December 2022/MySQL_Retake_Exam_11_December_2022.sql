CREATE SCHEMA `airplanes` DEFAULT CHARACTER SET utf8 ;

USE airplanes;

CREATE TABLE countries(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL UNIQUE,
    description TEXT,
    currency VARCHAR(5) NOT NULL
);

CREATE TABLE airplanes(
	id INT PRIMARY KEY AUTO_INCREMENT,
    model VARCHAR(50) NOT NULL UNIQUE,
    passengers_capacity INT NOT NULL,
    tank_capacity DECIMAL(19,2) NOT NULL,
    cost DECIMAL(19,2) NOT NULL
);

CREATE TABLE passengers(
	id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    country_id INT NOT NULL,
    
    FOREIGN KEY (country_id) REFERENCES countries(id)
);

CREATE TABLE flights(
	id INT PRIMARY KEY AUTO_INCREMENT,
    flight_code VARCHAR(30) NOT NULL UNIQUE,
    departure_country INT NOT NULL,
    destination_country INT NOT NULL,
    airplane_id INT NOT NULL,
    has_delay TINYINT(1),
    departure DATETIME,
    
    FOREIGN KEY (departure_country) REFERENCES countries(id),
    FOREIGN KEY (destination_country) REFERENCES countries(id),
    FOREIGN KEY (airplane_id) REFERENCES airplanes(id)
);

CREATE TABLE flights_passengers(
	flight_id INT,
    passenger_id INT,
    
    KEY(flight_id, passenger_id),
    FOREIGN KEY (flight_id) REFERENCES flights(id),
    FOREIGN KEY (passenger_id) REFERENCES passengers(id)
);

/* 02. Insert */ 
INSERT INTO airplanes(model, passengers_capacity, tank_capacity, cost)
SELECT 
	CONCAT(REVERSE(first_name), '797'),
    CHAR_LENGTH(last_name) * 17,
    id * 790,
    CHAR_LENGTH(first_name) * 50.6
FROM passengers
WHERE id <= 5;

/* 03. Update */ 
UPDATE flights
SET airplane_id = airplane_id + 1
WHERE departure_country = 22;

/* 04. Delete */ 
DELETE FROM flights 
WHERE id NOT IN (SELECT flight_id FROM flights_passengers);

/* 05. Airplanes */ 
SELECT * FROM airplanes ORDER BY cost DESC, id DESC;

/* 06. Flights from 2022 */ 
SELECT flight_code, departure_country, airplane_id, departure
FROM flights
WHERE YEAR(departure) = 2022
ORDER BY airplane_id, flight_code
LIMIT 20;

/* 07. Private flights */ 
SELECT 
	CONCAT(UPPER(SUBSTRING(last_name, 1, 2)), country_id) AS flight_code,
	CONCAT(first_name, ' ', last_name),
    country_id
FROM passengers
WHERE id NOT IN (SELECT passenger_id FROM flights_passengers)
ORDER BY country_id;

/* 08. Leading destinations */ 
SELECT
	c.name,
    c.currency,
    COUNT(*) AS booked_flights
FROM countries c
JOIN flights f ON c.id = f.destination_country
JOIN flights_passengers fp ON f.id = fp.flight_id
GROUP BY c.name
HAVING booked_flights >= 20
ORDER BY booked_flights DESC;


/* 09. Parts of the day */ 
SELECT 
	flight_code,
    departure,
	CASE
		WHEN TIME(departure) >= '05:00:00' AND TIME(departure) < '12:00:00' THEN 'Morning'
		WHEN TIME(departure) >= '12:00:00' AND TIME(departure) < '17:00:00' THEN 'Afternoon'
		WHEN TIME(departure) >= '17:00:00' AND TIME(departure) < '21:00:00' THEN 'Evening'
        ELSE 'Night'
    END AS day_part
FROM flights
ORDER BY flight_code DESC;

/* 10. Number of flights */ 
DELIMITER $
CREATE FUNCTION udf_count_flights_from_country(country VARCHAR(50)) 
RETURNS INT
DETERMINISTIC
BEGIN
	DECLARE result INT;
    SET result := (
					SELECT COUNT(*)
					FROM countries c
					JOIN flights f ON c.id = f.departure_country
					WHERE c.name = country);
	RETURN result;
END $
DELIMITER ;

SELECT udf_count_flights_from_country('Brazil') AS 'flights_count';
SELECT udf_count_flights_from_country('Philippines') AS 'flights_count';

/* 11. Delay flight */ 
DELIMITER $
CREATE PROCEDURE udp_delay_flight(code VARCHAR(50))
BEGIN
	UPDATE flights
    SET departure = DATE_ADD(departure, INTERVAL 30 MINUTE),  
		has_delay = 1
    WHERE flight_code = code;
END $
DELIMITER ;

SELECT NOW(), 


