CREATE SCHEMA `universities` DEFAULT CHARACTER SET utf8;

USE universities;

CREATE TABLE countries(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL UNIQUE
);

CREATE TABLE cities(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL UNIQUE,
    population INT,
    country_id INT NOT NULL,
    CONSTRAINT fk_countries_id FOREIGN KEY (country_id) REFERENCES countries(id)
);

CREATE TABLE universities(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(60) NOT NULL UNIQUE,
    address VARCHAR(80) NOT NULL UNIQUE,
    tuition_fee DECIMAL(19,2) NOT NULL,
    number_of_staff INT,
    city_id INT,
    
    CONSTRAINT fk_cities FOREIGN KEY (city_id) REFERENCES cities(id)
);

CREATE TABLE students (
	id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(40) NOT NULL,
    age INT,
    phone VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    is_graduated BOOLEAN NOT NULL,
    city_id INT,
    
    CONSTRAINT fk_cities_id FOREIGN KEY (city_id) REFERENCES cities(id)
);

CREATE TABLE courses (
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL UNIQUE,
    duration_hours DECIMAL(19,2),
    start_date DATE,
    teacher_name VARCHAR(60) NOT NULL UNIQUE,
    description TEXT,
    university_id INT,
    
    CONSTRAINT fk_universities_id FOREIGN KEY (university_id) REFERENCES universities(id)
);

CREATE TABLE students_courses(
	grade DECIMAL(19,2) NOT NULL,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    
    KEY (student_id, course_id),
    CONSTRAINT fk_students_id_students_courses FOREIGN KEY (student_id) REFERENCES students(id),
    CONSTRAINT fk_course_id_students_courses FOREIGN KEY (course_id) REFERENCES courses(id)
);

SELECT COLUMN_KEY, TABLE_NAME FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
  AND LENGTH(COLUMN_KEY) > 1
ORDER BY TABLE_NAME, COLUMN_KEY
LIMIT 13;

/* 02. Insert */
SELECT * FROM courses WHERE id <=5;
INSERT INTO courses(`name`, duration_hours, start_date, teacher_name, description, university_id)
SELECT
	CONCAT(teacher_name, ' course'),
    CHAR_LENGTH(`name`)/10,
    DATE(start_date + 5),
    REVERSE(teacher_name),
    CONCAT('Course ', teacher_name, REVERSE(description)),
    DAY(start_date)
FROM courses AS c
WHERE id <= 5;
--

/* 03. Update */
SELECT * FROM universities;
UPDATE universities
SET tuition_fee = tuition_fee + 300
WHERE id BETWEEN 5 AND 12;

/* 04. Delete */
SELECT * FROM universities;
DELETE FROM universities 
WHERE number_of_staff IS NULL;

/* 05. Cities */
SELECT * FROM cities ORDER BY population DESC;

/* 06. Students age */
SELECT first_name, last_name, age, phone, email
FROM students
WHERE age >= 21
ORDER BY first_name DESC, email, id
LIMIT 10;

/* 07. New students */
SELECT 
	CONCAT(s.first_name, ' ', s.last_name) AS full_name,
    SUBSTRING(s.email, 2, 10) AS username,
    REVERSE(s.phone) AS `password`
FROM students s
WHERE s.id NOT IN (SELECT student_id FROM students_courses)
ORDER BY `password` DESC;

SELECT * FROM students;
SELECT * FROM students_courses;

/* 08. Students count */
SELECT * FROM students;
SELECT * FROM universities;
SELECT * FROM courses;
SELECT * FROM students_courses;

SELECT
	COUNT(*) AS students_count,
	u.name AS university_name
FROM universities u
JOIN courses c ON u.id = c.university_id
JOIN students_courses sc ON c.id = sc.course_id
GROUP BY university_name
HAVING students_count >= 8
ORDER BY students_count DESC, university_name DESC;

/* 09. Price rankings */
SELECT 
	u.name AS university_name,
    c.name AS city_name,
    u.address,
    CASE
		WHEN u.tuition_fee < 800 THEN 'cheap'
		WHEN u.tuition_fee < 1200 THEN 'normal'
		WHEN u.tuition_fee < 2500 THEN 'high'
		ELSE 'expensive'
    END AS price_rank,
    u.tuition_fee
FROM universities u
JOIN cities c ON u.city_id = c.id
ORDER BY tuition_fee;

/* 10. Average grades */
DELIMITER $
CREATE FUNCTION udf_average_alumni_grade_by_course_name(course_name VARCHAR(60)) RETURNS DECIMAL(19, 2)
DETERMINISTIC
BEGIN
	DECLARE avg_grade DECIMAL(19, 2);
    SET avg_grade := (
		SELECT AVG(sc.grade)
		FROM courses c
		JOIN students_courses sc ON c.id = sc.course_id
        JOIN students t ON sc.student_id = t.id
		WHERE c.name = course_name AND t.is_graduated IS TRUE
		GROUP BY c.id);
	RETURN avg_grade;
END $
DELIMITER ;

SELECT AVG(sc.grade)
		FROM courses c
		JOIN students_courses sc ON c.id = sc.course_id
        JOIN students t ON sc.student_id = t.id
		WHERE c.name = 'Quantum Physics' AND t.is_graduated IS TRUE
		GROUP BY c.id;
        
SELECT c.name, udf_average_alumni_grade_by_course_name('Quantum Physics') as average_alumni_grade FROM courses c 
WHERE c.name = 'Quantum Physics';

/* 11. Graduate students */
DELIMITER $

CREATE PROCEDURE udp_graduate_all_students_by_year(year_started INT)
BEGIN
	UPDATE courses c
		JOIN students_courses sc ON c.id = sc.course_id
		JOIN students s ON sc.student_id = s.id
	SET s.is_graduated = TRUE
    WHERE YEAR(c.start_date) = year_started AND s.is_graduated = FALSE;
END $
DELIMITER ;


SELECT * FROM students;
SELECT * FROM courses;
SELECT * FROM students_courses;