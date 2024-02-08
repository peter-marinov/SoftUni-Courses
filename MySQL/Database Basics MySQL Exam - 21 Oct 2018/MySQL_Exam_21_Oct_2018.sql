CREATE SCHEMA `colonial_journey` DEFAULT CHARACTER SET utf8 ;

USE colonial_journey;

CREATE TABLE planets(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL
);

CREATE TABLE spaceports(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    planet_id INT,
    
    FOREIGN KEY (planet_id) REFERENCES planets(id)
);

CREATE TABLE spaceships(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    manufacturer VARCHAR(30) NOT NULL,
    light_speed_rate INT DEFAULT 0
);

CREATE TABLE colonists(
	id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    ucn CHAR(10) NOT NULL UNIQUE,
    birth_date DATE NOT NULL
);

CREATE TABLE journeys(
	id INT PRIMARY KEY AUTO_INCREMENT,
    journey_start DATETIME NOT NULL,
    journey_end DATETIME NOT NULL,
    purpose ENUM('Medical', 'Technical', 'Educational', 'Military'),
    destination_spaceport_id INT,
    spaceship_id INT,
    
    FOREIGN KEY (destination_spaceport_id) REFERENCES spaceports(id),
    FOREIGN KEY (spaceship_id) REFERENCES spaceships(id)
);

CREATE TABLE travel_cards(
	id INT PRIMARY KEY AUTO_INCREMENT,
    card_number CHAR(10) NOT NULL UNIQUE,
    job_during_journey ENUM('Pilot', 'Engineer', 'Trooper', 'Cleaner', 'Cook'),
    colonist_id INT,
    journey_id INT,
    
    FOREIGN KEY (colonist_id) REFERENCES colonists(id),
    FOREIGN KEY (journey_id) REFERENCES journeys(id)
);

/* 01. Insert */
INSERT INTO travel_cards(card_number, job_during_journey, colonist_id, journey_id)
SELECT
	CASE
		WHEN birth_date > '1980-01-01' THEN CONCAT(YEAR(birth_date), DAY(birth_date), LEFT(ucn, 4))
        ELSE CONCAT(YEAR(birth_date), MONTH(birth_date), RIGHT(ucn, 4))
    END,
    CASE
		WHEN id % 2 = 0 THEN 'Pilot'
		WHEN id % 3 = 0 THEN 'Cook'
        ELSE 'Engineer'
    END,
    id,
    LEFT(ucn, 1)
FROM colonists
WHERE id BETWEEN 96 AND 100;

/* 02. Update */
UPDATE journeys
SET purpose = CASE
				WHEN id % 2 = 0 THEN 'Medical'
				WHEN id % 3 = 0 THEN 'Technical'
				WHEN id % 5 = 0 THEN 'Educational'
				WHEN id % 7 = 0 THEN 'Military'
                ELSE purpose
            END;
			 

/* 03. Delete */
DELETE FROM colonists
WHERE id NOT IN ( SELECT colonist_id FROM travel_cards);

/* 04. Extract all travel cards */
SELECT
	card_number,
    job_during_journey
FROM travel_cards
ORDER BY card_number;

/* 05. Extract all colonists */
SELECT
	id, 
    CONCAT(first_name, ' ', last_name) AS full_name,
    ucn
FROM colonists
ORDER BY first_name, last_name, id;

/* 06. Extract all military journeys */
SELECT id, journey_start, journey_end
FROM journeys
WHERE purpose = 'Military'
ORDER BY journey_start;

/* 07. Extract all pilots */
SELECT c.id, CONCAT(first_name, ' ', last_name)
FROM colonists c
JOIN travel_cards tc ON c.id = tc.colonist_id
WHERE tc.job_during_journey = 'Pilot'
ORDER BY c.id;

/* 08. Count all colonists */
SELECT COUNT(*) AS count
FROM colonists c
JOIN travel_cards tc ON c.id = tc.colonist_id
JOIN journeys j ON tc.journey_id = j.id
WHERE j.purpose = 'Technical';

/* 09.Extract the fastest spaceship */
SELECT s.name AS spaceship_name, sp.name AS spaceport_name
FROM spaceships s
JOIN journeys j ON s.id = j.spaceship_id
JOIN spaceports sp ON j.destination_spaceport_id = sp.id
ORDER BY s.light_speed_rate DESC
LIMIT 1;

/* 10. Extract - pilots younger than 30 years */
SELECT s.name, s.manufacturer
FROM spaceships s
JOIN journeys j ON s.id = j.spaceship_id
JOIN travel_cards tc ON j.id = tc.journey_id
JOIN colonists c ON tc.colonist_id = c.id
WHERE TIMESTAMPDIFF(YEAR, c.birth_date, '2019-01-01') < 30 and tc.job_during_journey = 'Pilot'
ORDER BY s.name;

/* 11. Extract all educational mission */
SELECT p.name AS planet_name, s.name AS spaceport_name
FROM planets p
JOIN spaceports s ON p.id = s.planet_id
JOIN journeys j ON s.id = j.destination_spaceport_id
WHERE j.purpose = 'Educational'
ORDER BY s.name DESC;

/* 12. Extract all planets and their journey count */
SELECT p.name AS planet_name, COUNT(j.id) AS journeys_count
FROM planets p
JOIN spaceports s ON p.id = s.planet_id
JOIN journeys j ON s.id = j.destination_spaceport_id
GROUP BY p.name
ORDER BY journeys_count DESC, p.name;

/* 13. Extract the shortest journey */
SELECT 
	j.id, 
    p.name AS planet_name,
    s.name AS spaceport_name, 
    j.purpose AS journey_purpose
FROM journeys j
JOIN spaceports s ON j.destination_spaceport_id = s.id
JOIN planets p ON s.planet_id = p.id
WHERE TIMESTAMPDIFF(MINUTE, j.journey_start, j.journey_end) = (
													SELECT MIN(TIMESTAMPDIFF(MINUTE, journey_start, journey_end)) 
                                                    FROM journeys);

/* 14. Extract the less popular job */
SELECT tc.job_during_journey AS job_name
FROM travel_cards tc
JOIN journeys j ON tc.journey_id = j.id
WHERE TIMESTAMPDIFF(MINUTE, j.journey_start, j.journey_end) = (
													SELECT MAX(TIMESTAMPDIFF(MINUTE, journey_start, journey_end)) 
                                                    FROM journeys)
GROUP BY tc.job_during_journey
ORDER BY count(tc.job_during_journey)
LIMIT 1;

/* 15. Get colonists count */
DELIMITER $
CREATE FUNCTION udf_count_colonists_by_destination_planet (planet_name VARCHAR (30))
RETURNS INT
BEGIN
	RETURN (
		SELECT COUNT(*)
		FROM colonists c
        JOIN travel_cards tc ON c.id = tc.colonist_id
	JOIN journeys j ON tc.journey_id = j.id
	JOIN spaceports s ON j.destination_spaceport_id = s.id
	JOIN planets p ON s.planet_id = p.id
	WHERE p.name = planet_name);
END $
DELIMITER ;

/* 16. Modify spaceship */
DELIMITER $
CREATE PROCEDURE udp_modify_spaceship_light_speed_rate(
	spaceship_name VARCHAR(50), light_speed_rate_increse INT(11))
BEGIN
	IF (SELECT COUNT(name) FROM spaceships WHERE name = spaceship_name > 0) THEN
		UPDATE spaceships
        SET light_speed_rate = light_speed_rate + light_speed_rate_increse
        WHERE name = spaceship_name;
    ELSE 
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'Spaceship you are trying to modify does not exists.';
		ROLLBACK;
    END IF;
END $
DELIMITER ;
