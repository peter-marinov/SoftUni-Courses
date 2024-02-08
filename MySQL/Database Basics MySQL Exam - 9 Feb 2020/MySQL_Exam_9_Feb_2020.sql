CREATE SCHEMA `football_scout` DEFAULT CHARACTER SET utf8 ;

USE football_scout;

CREATE TABLE skills_data(
	id INT PRIMARY KEY AUTO_INCREMENT,
    dribbling INT DEFAULT 0,
    pace INT DEFAULT 0,
    passing INT DEFAULT 0,
    shooting INT DEFAULT 0,
    speed INT DEFAULT 0,
    strength INT DEFAULT 0
);

CREATE TABLE coaches(
	id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(10) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    salary DECIMAL(10,2) DEFAULT 0 NOT NULL,
    coach_level INT DEFAULT 0 NOT NULL
);

CREATE TABLE countries(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(45) NOT NULL
);

CREATE TABLE towns(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(45) NOT NULL,
    country_id INT NOT NULL,
    
    FOREIGN KEY (country_id) REFERENCES countries(id)
);

CREATE TABLE stadiums(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(45) NOT NULL,
    capacity INT NOT NULL,
    town_id INT NOT NULL,
    
    FOREIGN KEY (town_id) REFERENCES towns(id)
);

CREATE TABLE teams(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(45) NOT NULL,
    established DATE NOT NULL,
    fan_base BIGINT DEFAULT 0 NOT NULL,
    stadium_id INT NOT NULL,
    
    FOREIGN KEY (stadium_id) REFERENCES stadiums(id)
);


CREATE TABLE players(
	id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(10) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    age INT DEFAULT 0 NOT NULL,
    position CHAR(1) NOT NULL,
    salary DECIMAL(10,2) DEFAULT 0 NOT NULL,
    hire_date DATETIME,
    skills_data_id INT NOT NULL,
    team_id INT,
    
    FOREIGN KEY (skills_data_id) REFERENCES skills_data(id),
    FOREIGN KEY (team_id) REFERENCES teams(id)
);

CREATE TABLE players_coaches(
	player_id INT,
    coach_id INT,
    
    KEY (player_id, coach_id),
    FOREIGN KEY (player_id) REFERENCES players(id),
    FOREIGN KEY (coach_id) REFERENCES coaches(id)
);

/* 02. Insert */
INSERT INTO coaches(first_name, last_name, salary, coach_level)
SELECT
	first_name,
    last_name,
    salary * 2,
    CHAR_LENGTH(first_name)
FROM players
WHERE age >= 45;

/* 03. Update */
UPDATE coaches c
SET c.coach_level = c.coach_level + 1
WHERE LEFT(c.first_name, 1) = 'A' AND (SELECT COUNT(*) FROM players_coaches WHERE coach_id = c.id) >= 1;

/* 04. Delete */
DELETE p FROM players p
JOIN coaches c ON p.first_name = c.first_name AND p.last_name = c.last_name
WHERE p.age >= 45;

/* 05. Players */
SELECT first_name, age, salary
FROM players
ORDER BY salary DESC;

/* 06. Young offense players without contract */
SELECT
	p.id,
    CONCAT(p.first_name, ' ', p.last_name) AS full_name,
    p.age,
    p.position,
    p.hire_date
FROM players p
JOIN skills_data sd ON p.skills_data_id = sd.id
WHERE p.age < 23 AND p.position = 'A' AND p.hire_date IS NULL AND sd.strength > 50
ORDER BY p.salary, p.age;

/* 07. Detail info for all teams */
SELECT
	t.name AS team_name,
    t.established,
    t.fan_base,
    COUNT(p.id) AS players_count
FROM teams t
LEFT JOIN players p ON t.id = p.team_id
GROUP BY t.id
ORDER BY players_count DESC, t.fan_base DESC;

/* 08. The fastest player by towns */
SELECT
	MAX(sd.speed) AS max_speed,
    t.name AS town_name
FROM players p
JOIN teams t ON p.team_id = t.id
JOIN stadiums s ON t.stadium_id = s.id
JOIN towns town ON s.town_id = town.id
JOIN skills_data sd ON p.skills_data_id = sd.id
WHERE t.name <> 'Devify'
GROUP BY town.id
ORDER BY max_speed DESC, t.name;

/* 09. Total salaries and players by country */
SELECT
	c.name,
    COUNT(p.id) AS 'total_count_of_players',
    SUM(p.salary) AS 'total_sum_of_salaries'
FROM players AS p
	RIGHT JOIN skills_data AS sd ON p.skills_data_id = sd.id
    RIGHT JOIN teams AS t ON p.team_id = t.id
    RIGHT JOIN stadiums AS s ON t.stadium_id = s.id
	RIGHT JOIN towns AS ts ON s.town_id = ts.id
	RIGHT JOIN countries AS c ON ts.country_id = c.id
GROUP BY c.name
ORDER BY total_count_of_players DESC, c.name;

/* 10. Find all players that play on stadium */
DELIMITER $
CREATE FUNCTION udf_stadium_players_count (stadium_name VARCHAR(30))
RETURNS INT
DETERMINISTIC
BEGIN
	DECLARE result INT;
    SET result = (
				SELECT COUNT(*)
				FROM players p
				JOIN teams t ON p.team_id = t.id
				JOIN stadiums s ON t.stadium_id = s.id
				WHERE s.name = stadium_name);
    RETURN result;
END $
DELIMITER ;

/* 11. Find good playmaker by teams */
DELIMITER $
CREATE PROCEDURE udp_find_playmaker(min_dribble_points INT, team_name VARCHAR(45))
BEGIN
	SELECT
		CONCAT(p.first_name, ' ', last_name) AS full_name,
		p.age,
		p.salary,
		sd.dribbling,
		sd.speed,
		t.name AS team_name
		FROM players p
		JOIN teams t ON p.team_id = t.id
		JOIN skills_data sd ON p.skills_data_id = sd.id
		WHERE t.name = team_name AND sd.dribbling > min_dribble_points AND sd.speed > (SELECT AVG(speed) FROM skills_data)
		ORDER BY sd.speed DESC
		LIMIT 1;
END $
DELIMITER ;

SELECT
	CONCAT(p.first_name, ' ', last_name) AS full_name,
    p.age,
    p.salary,
    sd.dribbling,
    sd.speed,
    t.name AS team_name
FROM players p
JOIN teams t ON p.team_id = t.id
JOIN skills_data sd ON p.skills_data_id = sd.id
WHERE t.name = 'Skyble' AND sd.dribbling > 20 AND sd.speed > (SELECT AVG(speed) FROM skills_data)
ORDER BY sd.speed DESC
LIMIT 1;


