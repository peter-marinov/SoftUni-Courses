/* 01. One-To-One Relationship */
CREATE TABLE people (
	person_id INT,
    first_name VARCHAR(50),
    salary DECIMAL,
    passport_id INT
);

CREATE TABLE passports (
	passport_id INT,
    passport_number VARCHAR(50)
);

INSERT INTO people(person_id, first_name, salary, passport_id)
VALUES 
	(1, 'Roberto', 43300.00, 102),
	(2, 'Tom', 56100.00, 103),
	(3, 'Yana', 60200.00, 101);

INSERT INTO passports(passport_id, passport_number)
VALUES
	(101, 'N34FG21B'),
	(102, 'K65LO4R7'),
	(103, 'ZE657QP2');

ALTER TABLE passports
ADD CONSTRAINT `pk_passport_id` PRIMARY KEY(passport_id),
ADD UNIQUE(passport_number);

ALTER TABLE people
ADD CONSTRAINT `pk_person_id` PRIMARY KEY (person_id),
ADD CONSTRAINT `fk_persons_passports` FOREIGN KEY (passport_id) REFERENCES passports(passport_id),
MODIFY COLUMN salary DECIMAL(10,2);



SELECT * FROM people;
SELECT * FROM passports;

# data insertion check

select * from
    people per inner join passports pas on per.passport_id = pas.passport_id
order by per.person_id;


USE relations;

-- below is for Judge
CREATE TABLE passports (
	passport_id INT PRIMARY KEY AUTO_INCREMENT,
    passport_number VARCHAR(50) UNIQUE
);

INSERT INTO passports(passport_id, passport_number)
VALUES
	(101, 'N34FG21B'),
	(102, 'K65LO4R7'),
	(103, 'ZE657QP2');

CREATE TABLE people (
	person_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    salary DECIMAL(10,2),
    passport_id INT UNIQUE,

    FOREIGN KEY (passport_id) REFERENCES passports(passport_id)
);

INSERT INTO people(person_id, first_name, salary, passport_id)
VALUES 
	(1, 'Roberto', 43300.00, 102),
	(2, 'Tom', 56100.00, 103),
	(3, 'Yana', 60200.00, 101);
-- 

/* 02. One-To-Many Relationship */
CREATE TABLE manufacturers (
	manufacturer_id INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50) UNIQUE,
    established_on DATE
);

INSERT INTO manufacturers (`name`, established_on)
VALUES
	('BMW', '1916-03-01'),
	('Tesla', '2003-01-01'),
	('Lada', '1966-05-01');
    
CREATE TABLE models (
	model_id INT PRIMARY KEY,
    name VARCHAR(50) UNIQUE,
    manufacturer_id INT,
    
    CONSTRAINT `fk_manufacturers_models` FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id)
);

INSERT INTO models(model_id, name, manufacturer_id)
VALUES
	(101, 'X1', 1),
	(102, 'i6', 1),
	(103, 'Model S', 2),
	(104, 'Model X', 2),
	(105, 'Model 3', 2),
	(106, 'Nova', 3);
-- 

/* 03. Many-To-Many Relationship */
CREATE TABLE students (
	student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50)
);

INSERT INTO students(name) VALUES ('Mila'), ('Toni'), ('Ron');

CREATE TABLE exams (
	exam_id INT PRIMARY KEY,
    name VARCHAR(50)
);

INSERT INTO exams 
VALUES 
	(101, 'Spring MVC'),
	(102, 'Neo4j'),
	(103, 'Oracle 11g');
    
CREATE TABLE students_exams (
	student_id INT,
    exam_id INT,
    
    CONSTRAINT pk_student_students_exams PRIMARY KEY (student_id, exam_id),
    CONSTRAINT fk_students_students_exams 
		FOREIGN KEY (student_id) 
        REFERENCES students(student_id),
	CONSTRAINT fk_exams_students_exams 
		FOREIGN KEY (exam_id) 
        REFERENCES exams(exam_id)
);

INSERT INTO students_exams
VALUES 
	(1, 101),
	(1, 102),
	(2, 101),
	(3, 103),
	(2, 102),
	(2, 103);

-- END

/* 04. Self-Referencing */
CREATE TABLE teachers (
	teacher_id INT PRIMARY KEY,
    name VARCHAR(50),
    manager_id INT
);

INSERT INTO teachers
VALUES
	(101, 'John', NULL),
	(102, 'Maya', 106),
	(103, 'Silvia', 106),
	(104, 'Ted', 105),
	(105, 'Mark', 101),
	(106, 'Greta', 101);

ALTER TABLE teachers ADD FOREIGN KEY (manager_id) REFERENCES teachers(teacher_id);
-- END

/* 05. Online Store Database */
CREATE TABLE cities (
	city_id INT(11) PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50)
);

CREATE TABLE customers (
	customer_id INT(11) PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    birthday DATE,
    city_id INT(11),
    
    FOREIGN KEY (city_id) REFERENCES cities(city_id)
);

CREATE TABLE orders(
	order_id INT(11) PRIMARY KEY AUTO_INCREMENT,
    customer_id INT(11),
    
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE item_types (
	item_type_id INT(11) PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50)
);

CREATE TABLE items (
	item_id INT(11) PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    item_type_id INT(11),
    
    FOREIGN KEY (item_type_id) REFERENCES item_types(item_type_id)
);

CREATE TABLE order_items (
	order_id INT(11),
    item_id INT(11),
    
    PRIMARY KEY (order_id, item_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);
-- END

/* 06. University Database */
CREATE TABLE subjects (
	subject_id INT PRIMARY KEY AUTO_INCREMENT,
    subject_name VARCHAR(50)
);

CREATE TABLE majors (
	major_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50)
);

CREATE TABLE students (
	student_id INT PRIMARY KEY AUTO_INCREMENT,
    student_number VARCHAR(12),
    student_name VARCHAR(50),
    major_id INT,
    
    FOREIGN KEY (major_id) REFERENCES majors(major_id)
);

CREATE TABLE payments (
	payment_id INT PRIMARY KEY AUTO_INCREMENT,
    payment_date DATE,
    payment_amount DECIMAL(8, 2),
    student_id INT,
    
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

CREATE TABLE agenda (
	student_id INT,
    subject_id INT,
    
    PRIMARY KEY (student_id, subject_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);
-- END

/* 09. Peaks in Rila */
USE geography;
SELECT
	mountains.mountain_range,
    peaks.peak_name,
    peaks.elevation AS 'peak_evelation'
FROM mountains
JOIN peaks ON mountains.id = peaks.mountain_id
WHERE mountain_range = 'Rila'
ORDER BY `peak_evelation` DESC;
-- END


