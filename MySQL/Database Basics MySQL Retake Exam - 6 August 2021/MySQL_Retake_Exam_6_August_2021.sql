CREATE SCHEMA `game_dev` DEFAULT CHARACTER SET utf8 ;

USE game_dev;

CREATE TABLE addresses(
	 id INT PRIMARY KEY AUTO_INCREMENT,
     name VARCHAR(50) NOT NULL
);

CREATE TABLE categories(
	 id INT PRIMARY KEY AUTO_INCREMENT,
     name VARCHAR(10) NOT NULL
);

CREATE TABLE offices(
	 id INT PRIMARY KEY AUTO_INCREMENT,
     workspace_capacity INT NOT NULL,
     website VARCHAR(50),
     address_id INT NOT NULL,
     
     FOREIGN KEY (address_id) REFERENCES addresses(id)
);

CREATE TABLE employees(
	 id INT PRIMARY KEY AUTO_INCREMENT,
     first_name VARCHAR(30) NOT NULL,
     last_name VARCHAR(30) NOT NULL,
     age INT NOT NULL,
     salary DECIMAL(10,2) NOT NULL,
     job_title VARCHAR(20) NOT NULL,
     happiness_level CHAR(1)
);

CREATE TABLE teams(
	 id INT PRIMARY KEY AUTO_INCREMENT,
     name VARCHAR(40) NOT NULL,
     office_id INT NOT NULL,
     leader_id INT NOT NULL UNIQUE,
     
     FOREIGN KEY (office_id) REFERENCES offices(id),
     FOREIGN KEY (leader_id) REFERENCES employees(id)
);

CREATE TABLE games(
	 id INT PRIMARY KEY AUTO_INCREMENT,
     name VARCHAR(50) NOT NULL UNIQUE,
     description TEXT,
     rating FLOAT DEFAULT 5.5 NOT NULL,
     budget DECIMAL(10,2) NOT NULL,
     release_date DATE,
     team_id INT NOT NULL,
     
     FOREIGN KEY (team_id) REFERENCES teams(id)
);

CREATE TABLE games_categories(
	 game_id INT NOT NULL,
     category_id INT NOT NULL,
     
     PRIMARY KEY (game_id, category_id),
     FOREIGN KEY (game_id) REFERENCES games(id),
     FOREIGN KEY (category_id) REFERENCES categories(id)
);

/* 02. Insert */
INSERT INTO games(name, rating, budget, team_id)
SELECT
	LOWER(REVERSE(SUBSTRING(name, 2))),
    id,
    leader_id * 1000,
    id
FROM teams
WHERE id BETWEEN 1 and 9;

/* 03. Update */
UPDATE employees e
JOIN teams t ON e.id = t.leader_id
SET e.salary = e.salary + 1000
WHERE e.age < 40 AND e.salary < 5000;

/* 04. Delete */
DELETE FROM games
WHERE release_date IS NULL AND id NOT IN (SELECT game_id FROM games_categories);

/* 05. Employees */
SELECT first_name, last_name, age, salary, happiness_level
FROM employees
ORDER BY salary, id;

/* 06. Addresses of the teams */
SELECT
	t.name,
    a.name,
    CHAR_LENGTH(a.name) AS count_of_characters
FROM teams t
JOIN offices o ON t.office_id = o.id
JOIN addresses a ON o.address_id = a.id
WHERE o.website IS NOT NULL
ORDER BY t.name, a.name;

/* 07. Categories Info */
SELECT
	c.name,
    COUNT(*) AS games_count,
    ROUND(AVG(g.budget), 2) AS avg_budget,
    MAX(g.rating) AS max_rating
FROM categories c
JOIN games_categories gc ON c.id = gc.category_id
JOIN games g ON gc.game_id = g.id
GROUP BY c.name
HAVING max_rating >= 9.5
ORDER BY games_count DESC, c.name;

/* 08. Games of 2022 */
SELECT
	g.name,
    g.release_date,
    CONCAT(SUBSTRING(g.description, 1, 10), '...') AS summary,
    CASE
		WHEN MONTH(g.release_date) <= 3 THEN 'Q1'
		WHEN MONTH(g.release_date) <= 6 THEN 'Q2'
		WHEN MONTH(g.release_date) <= 9 THEN 'Q3'
        ELSE 'Q4'
    END AS quarter,
    t.name AS team_name
FROM games g
JOIN teams t ON g.team_id = t.id
WHERE g.name LIKE '%2' AND (MONTH(g.release_date) % 2 =0) AND YEAR(g.release_date) = 2022
ORDER BY quarter;

/* 09. Full info for games */
SELECT
	g.name,
    CASE
		WHEN g.budget < 50000 THEN 'Normal budget'
        ELSE 'Insufficient budget'
    END AS budget_level,
    t.name,
    a.name
FROM games g
JOIN teams t ON g.team_id = t.id
JOIN offices o ON t.office_id = o.id
JOIN addresses a ON o.address_id = a.id
WHERE g.release_date IS NULL AND g.id NOT IN (SELECT game_id FROM games_categories)
ORDER BY g.name;

/* 10. Find all basic information for a game */
DELIMITER $
CREATE FUNCTION udf_game_info_by_name (game_name VARCHAR (20))
RETURNS TEXT
DETERMINISTIC
BEGIN
	DECLARE result TEXT;
    SET result = (
				SELECT CONCAT('The ', g.name, ' is developed by a ', t.name, ' in an office with an address ', a.name) 
                FROM games g
                JOIN teams t ON g.team_id = t.id
                JOIN offices o ON t.office_id = o.id
                JOIN addresses a ON o.address_id = a.id
                WHERE g.name = game_name
                );
	RETURN result;
END $
DELIMITER ;

SELECT udf_game_info_by_name('Bitwolf') AS info;

/* 11. Update Budget of the Games */
DELIMITER $
CREATE PROCEDURE udp_update_budget(min_game_rating FLOAT) 
BEGIN
	UPDATE games
    SET budget = budget + 100000,
		release_date = DATE_ADD(release_date, INTERVAL 1 YEAR)
	WHERE id NOT IN (SELECT game_id FROM games_categories) AND
		rating > min_game_rating AND
        release_date IS NOT NULL;
END $
DELIMITER ;