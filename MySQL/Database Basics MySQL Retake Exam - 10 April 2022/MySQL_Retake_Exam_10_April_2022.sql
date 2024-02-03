CREATE SCHEMA `softuni_imdb` DEFAULT CHARACTER SET utf8 ;

USE softuni_imdb;

CREATE TABLE countries(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL UNIQUE,
    continent VARCHAR(30) NOT NULL,
    currency VARCHAR(5) NOT NULL
);

CREATE TABLE genres(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE actors(
	id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birthdate DATE NOT NULL,
    height INT,
    awards INT,
    country_id INT NOT NULL,
    
    FOREIGN KEY (country_id) REFERENCES countries(id)
);

CREATE TABLE movies_additional_info(
	id INT PRIMARY KEY AUTO_INCREMENT,
    rating DECIMAL(10,2) NOT NULL,
    runtime INT NOT NULL,
    picture_url VARCHAR(80) NOT NULL,
    budget DECIMAL(10,2),
    release_date DATE NOT NULL,
    has_subtitles TINYINT(1),
    description TEXT
);

CREATE TABLE movies(
	id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(70) NOT NULL UNIQUE,
    country_id INT NOT NULL,
    movie_info_id INT NOT NULL UNIQUE,
    
    FOREIGN KEY (country_id) REFERENCES countries(id),
    FOREIGN KEY (movie_info_id) REFERENCES movies_additional_info(id)
);

CREATE TABLE movies_actors(
	movie_id INT,
    actor_id INT,
    
    KEY (movie_id, actor_id),
    FOREIGN KEY (movie_id) REFERENCES movies(id),
    FOREIGN KEY (actor_id) REFERENCES actors(id)
);

CREATE TABLE genres_movies(
	genre_id INT,
    movie_id INT,
    
    KEY (genre_id, movie_id),
    FOREIGN KEY (genre_id) REFERENCES genres(id),
    FOREIGN KEY (movie_id) REFERENCES movies(id)
);

/* 02. Insert */
INSERT INTO actors(first_name, last_name, birthdate, height, awards, country_id)
SELECT
	REVERSE(first_name),
    REVERSE(last_name),
    DATE_SUB(birthdate, INTERVAL 2 DAY),
    height + 10,
    country_id,
    (SELECT id FROM countries WHERE name = 'Armenia')
FROM actors
WHERE id <= 10;

/* 03. Update */
UPDATE movies_additional_info
SET runtime = runtime - 10
WHERE id BETWEEN 15 and 25;

/* 04. Delete */
DELETE FROM countries
WHERE id NOT IN (SELECT country_id FROM movies);

/* 05. Countries */
SELECT * FROM countries ORDER BY currency DESC, id;

/* 06. Old movies */
SELECT m.id, m.title, mai.runtime, mai.budget, mai.release_date
FROM movies m
JOIN movies_additional_info mai ON m.movie_info_id = mai.id
WHERE YEAR(mai.release_date) BETWEEN 1996 AND 1999
ORDER BY runtime, id
LIMIT 20;

/* 07. Movie casting */
SELECT 
	CONCAT(first_name, ' ', last_name) AS full_name,
    CONCAT(REVERSE(last_name), CHAR_LENGTH(last_name), '@cast.com') AS email,
    2022 - YEAR(birthdate) AS age,
    height
FROM actors
WHERE id NOT IN (SELECT actor_id FROM movies_actors)
ORDER BY height;

/* 08. International festival */
SELECT
	c.name,
    COUNT(*) AS movies_count
FROM countries c
JOIN movies m ON c.id = m.country_id
GROUP BY c.name
HAVING movies_count >= 7
ORDER BY c.name DESC;

/* 09. Rating system */
SELECT
	m.title,
    CASE
		WHEN mai.rating <=4 THEN 'poor'
		WHEN mai.rating <=7 THEN 'good'
        ELSE 'excellent'
    END AS rating,
	CASE
		WHEN has_subtitles = 1 THEN 'english'
        ELSE '-'
    END AS subtitles,
    budget
FROM movies m
JOIN movies_additional_info mai ON m.movie_info_id = mai.id
ORDER BY mai.budget DESC;

/* 10. History movies */
DELIMITER $
CREATE FUNCTION udf_actor_history_movies_count(full_name VARCHAR(50))
RETURNS INT
DETERMINISTIC
BEGIN
	DECLARE result INT;
    SET result = (
				SELECT COUNT(*)
				FROM actors a
				JOIN movies_actors ma ON a.id = ma.actor_id
				JOIN genres_movies gm ON ma.movie_id = gm.movie_id
				JOIN genres g ON gm.genre_id = g.id
				WHERE CONCAT(a.first_name, ' ', a.last_name) = full_name AND g.name = 'History');
	RETURN result;
END $
DELIMITER ;

/* 11. Movie awards */
DELIMITER $
CREATE PROCEDURE udp_award_movie(movie_title VARCHAR(50))
BEGIN 
	UPDATE actors a
    JOIN movies_actors ma ON a.id = ma.actor_id
    JOIN movies m ON ma.movie_id = m.id
    SET a.awards = a.awards + 1
    WHERE m.title = movie_title;
END $
DELIMITER ;

