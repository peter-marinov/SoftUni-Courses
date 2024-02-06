CREATE SCHEMA `insta` DEFAULT CHARACTER SET utf8 ;

USE insta;

CREATE TABLE users(
	id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(30) NOT NULL UNIQUE,
    password VARCHAR(30) NOT NULL,
    email VARCHAR(50) NOT NULL,
    gender CHAR(1) NOT NULL,
    age INT NOT NULL,
    job_title VARCHAR(40) NOT NULL,
    ip VARCHAR(30) NOT NULL
);

CREATE TABLE addresses(
	id INT PRIMARY KEY AUTO_INCREMENT,
    address VARCHAR(30) NOT NULL,
    town VARCHAR(30) NOT NULL,
    country VARCHAR(30) NOT NULL,
    user_id INT NOT NULL,
    
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE photos(
	id INT PRIMARY KEY AUTO_INCREMENT,
    `description` TEXT NOT NULL,
    `date` DATETIME NOT NULL,
    views INT DEFAULT 0 NOT NULL
);

CREATE TABLE comments(
	id INT PRIMARY KEY AUTO_INCREMENT,
    comment VARCHAR(255) NOT NULL,
    date DATETIME NOT NULL,
    photo_id INT NOT NULL,
    
    FOREIGN KEY (photo_id) REFERENCES photos(id)
);

CREATE TABLE users_photos(
	user_id INT NOT NULL,
    photo_id INT NOT NULL,
    
    KEY (user_id, photo_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (photo_id) REFERENCES photos(id)
);

CREATE TABLE likes(
	id INT PRIMARY KEY AUTO_INCREMENT,
    photo_id INT,
    user_id INT,
    
    FOREIGN KEY (photo_id) REFERENCES photos(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

/* 02. Insert */
INSERT INTO addresses(address, town, country, user_id)
SELECT
	username,
    password,
    ip,
    age
FROM users
WHERE gender = 'M';

/* 03. Update */
UPDATE addresses
SET country =
	CASE
		WHEN LEFT(country, 1) = 'B' THEN 'Blocked'
		WHEN LEFT(country, 1) = 'T' THEN 'Test'
		WHEN LEFT(country, 1) = 'P' THEN 'In Progress'
        ELSE country
	END;

/* 04. Delete */
DELETE FROM addresses
WHERE id % 3 = 0;

/* 05. Users */
SELECT username, gender, age
FROM users
ORDER BY age DESC, username;

/* 06. Extract 5 most commented photos */
SELECT
	p.id,
    p.date AS date_and_time,
    p.description,
    COUNT(*) AS commentsCount
FROM photos p
JOIN comments c ON p.id = c.photo_id
GROUP BY p.id
ORDER BY commentsCount DESC, p.id
LIMIT 5;

/* 07. Lucky users */
SELECT
	CONCAT(u.id, ' ', u.username) AS id_username,
    u.email
FROM users u
JOIN users_photos up ON u.id = up.user_id
WHERE u.id = up.photo_id
ORDER BY u.id;

/* 08. Count likes and comments */
SELECT
	p.id AS photo_id,
    COUNT(DISTINCT l.id) AS likes_count,
    COUNT(DISTINCT c.id) AS comment_count
FROM photos p
LEFT JOIN likes l ON p.id = l.photo_id
LEFT JOIN comments c ON p.id = c.photo_id
GROUP BY p.id
ORDER BY likes_count DESC, comment_count DESC, p.id;

SELECT * FROM likes;

/* 09. The photo on the tenth day of the month */
SELECT
	CONCAT(LEFT(description, 30), '...') AS summary,
    `date`
FROM photos
WHERE DAY(`date`) = 10
ORDER BY `date` DESC;

SELECT LEFT('1234567', 5);

/* 10. Get user’s photos count */
DELIMITER $
CREATE FUNCTION udf_users_photos_count(username VARCHAR(30))
RETURNS INT
DETERMINISTIC
BEGIN
	DECLARE result INT;
    SET result = (
				SELECT COUNT(*)
                FROM users u
                JOIN users_photos up ON u.id = up.user_id
                WHERE u.username = username);
    RETURN result;
END $
DELIMITER ;

/* 11. Increase user age */
DELIMITER $
CREATE PROCEDURE udp_modify_user (address VARCHAR(30), town VARCHAR(30))
BEGIN
	UPDATE users u
    JOIN addresses a ON u.id = a.user_id
    SET u.age = u.age + 10
    WHERE a.address = address AND a.town = town;
END $
DELIMITER ;


