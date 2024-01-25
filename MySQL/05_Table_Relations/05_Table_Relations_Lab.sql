CREATE DATABASE relations;

USE relations;

DROP TABLE mountains;

CREATE TABLE mountains(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE peaks(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    mountain_id INT,
    CONSTRAINT fk_peaks_mountain_id_mountains_id
    FOREIGN KEY (mountain_id)
    REFERENCES mountains(id)
);

INSERT INTO mountains(name) VALUES ("Pirin"), ("Rila");
INSERT INTO peaks(name, mountain_id) VALUES ('Musala', 2);
INSERT INTO peaks(name, mountain_id) VALUES ('Vruh 2', 2);
INSERT INTO peaks(name) VALUES ("Vihren");

SELECT * FROM mountains;
SELECT * FROM peaks;

UPDATE peaks SET mountain_id = 1 WHERE name = 'Vihren';

SELECT * 
FROM peaks
JOIN mountains ON peaks.mountain_id = mountains.id;

SELECT 
	peaks.id, 
    peaks.name AS 'Peak name',
    mountains.name AS 'Mountain name'
FROM peaks
JOIN mountains ON peaks.mountain_id = mountains.id;

SELECT * FROM peaks WHERE name = 'Musala';
SELECT * FROM mountains WHERE id = 2;

USE relations;
DELETE FROM mountains WHERE id = 1;

DROP TABLE peaks;

CREATE TABLE peaks(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    mountain_id INT,
    CONSTRAINT fk_peaks_mountain_id_mountains_id
		FOREIGN KEY (mountain_id)
		REFERENCES mountains(id)
        ON DELETE CASCADE
);

INSERT INTO mountains(name) VALUES ("Pirin"), ("Rila");
INSERT INTO peaks(name, mountain_id) VALUES ('Musala', 2);
INSERT INTO peaks(name, mountain_id) VALUES ('Vruh 2', 2);
INSERT INTO peaks(name, mountain_id) VALUES ("Vihren", 3);

SELECT * FROM peaks;
SELECT * FROM mountains;

DELETE FROM peaks WHERE id = 4;
DELETE FROM mountains WHERE id = 2;

/* 1. Mountains and Peaks */
CREATE TABLE mountains(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE peaks(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    mountain_id INT,
    CONSTRAINT fk_peaks_mountain_id_mountains_id
    FOREIGN KEY (mountain_id)
    REFERENCES mountains(id)
);
-- END

/* 2. Trip Organization */
USE camp;
-- below is for Judge
SELECT
	vehicles.driver_id,
    vehicles.vehicle_type,
    CONCAT_WS(' ', campers.first_name, campers.last_name) AS 'driver_name'
FROM vehicles
JOIN campers ON vehicles.driver_id = campers.id;
-- END

/* 3. SoftUni Hiking */
SELECT 
	routes.starting_point AS 'route_starting_point',
	routes.end_point AS 'route_ending_point',
    routes.leader_id,
    CONCAT_WS(' ', campers.first_name, campers.last_name) AS 'leader_name'
FROM routes
JOIN campers ON routes.leader_id = campers.id;
-- END

/* 4. Delete Mountains */
DROP TABLE peaks;
-- below is the code for Judge
CREATE TABLE mountains(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE peaks(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    mountain_id INT,
    CONSTRAINT fk_peaks_mountain_id_mountains_id
		FOREIGN KEY (mountain_id)
		REFERENCES mountains(id)
        ON DELETE CASCADE
);
-- END