CREATE SCHEMA minios DEFAULT CHARACTER SET utf8;
USE minions;


/* 01. Create Tables */
CREATE TABLE minions(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age VARCHAR(50)
);

CREATE TABLE towns(
	town_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);
-- END

/* 02. Alter Minions Table */ 
ALTER TABLE towns
RENAME COLUMN town_id TO id;
-- below is for Judge
ALTER TABLE minions
ADD COLUMN town_id INT;

ALTER TABLE minions
ADD CONSTRAINT fk_minions_town
FOREIGN KEY (town_id) REFERENCES towns(id);
-- END

/* 03. Insert Records in Both Tables */
INSERT INTO towns(id, name)
VALUES
	(1, "Sofia"),
	(2, "Plovdiv"),
	(3, "Varna");

INSERT INTO minions(id, name, age, town_id)
VALUES
	(1, "Kevin", 22, 1),
	(2, "Bob", 15, 3),
	(3, "Steward", NULL, 2);
-- END

/* 04. Truncate Table Minions */
TRUNCATE TABLE minions;
-- END

/* 05. Drop All Tables */
DROP TABLE minions;
DROP TABLE towns;
-- END

/* 06. Create Table People */
CREATE TABLE people(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    picture MEDIUMBLOB, -- 2MB in bytes
    height DECIMAL(5, 2),
    weight DECIMAL(5, 2),
    gender VARCHAR(1) NOT NULL CHECK (gender IN("m", "f")),
    birthdate DATE NOT NULL,
    biography TEXT
);

INSERT INTO people(name, picture, height, weight, gender, birthdate, biography)
VALUES
	("Peter", NULL, 1.75, 80.22, 'm', '1990-09-14', 'Some text here'),
	("Desi", NULL, 1.61, 60.2, 'f', '1993-09-14', 'Some text here2'),
	("George", NULL, 1.05, 55.01, 'm', '1990-10-14', 'Some text here3'),
	("Stephane", NULL, 8.75, 100.20, 'm', '1999-10-24', 'Some text here4'),
	("Kali", NULL, 1.75, 45, 'f', '1990-09-14', 'Some text here5');
-- END

/* 07. Create Table Users */
CREATE TABLE users(
	id BIGINT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(30) NOT NULL,
    password VARCHAR(26) NOT NULL,
    profile_picture BLOB,
    last_login_time TIMESTAMP,
    is_deleted BOOLEAN
);

INSERT INTO users(username, password, profile_picture, last_login_time, is_deleted)
VALUES
	('user1', 'password1', NULL, NULL, false),
	('user2', 'password2', NULL, NULL, false),
	('user3', 'password3', NULL, NULL, true),
	('user4', 'password4', NULL, NULL, false),
	('user5', 'password5', NULL, NULL, false);
-- END

/* 08. Change Primary Key */
ALTER TABLE users
DROP PRIMARY KEY,
ADD CONSTRAINT pk_users PRIMARY KEY (id, username);
-- END

/* 9. Set Default Value of a Field */
ALTER TABLE users
MODIFY COLUMN last_login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP;
-- END

/* 10. Set Unique Field */
ALTER TABLE users
DROP PRIMARY KEY,
ADD PRIMARY KEY(id);

ALTER TABLE users
MODIFY COLUMN username VARCHAR(30) NOT NULL UNIQUE;
-- END

/* 11. Movies Database */
USE movies;
CREATE TABLE directors(
	id INT AUTO_INCREMENT PRIMARY KEY,
    director_name VARCHAR(50) NOT NULL,
    notes TEXT
);

CREATE TABLE genres(
	id INT AUTO_INCREMENT PRIMARY KEY,
    genre_name VARCHAR(50) NOT NULL,
    notes TEXT
);

CREATE TABLE categories(
	id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    notes TEXT
);

CREATE TABLE movies(
	id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    director_id INT,
    copyright_year YEAR,
    length TIME,
    genre_id INT,
    category_id INT,
    rating DECIMAL(3, 1),
    notes TEXT/*,
    FOREIGN KEY(director_id) REFERENCES directors(id),
    FOREIGN KEY(genre_id) REFERENCES genres(id),
    FOREIGN KEY(category_id) REFERENCES categories(id)*/
);

INSERT INTO directors(director_name, notes) 
VALUES
	("Director Name 1", "Director Note1"),
	("Director Name 2", "Director Note2"),
	("Director Name 3", "Director Note3"),
	("Director Name 4", "Director Note4"),
	("Director Name 5", "Director Note5");

INSERT INTO genres(genre_name, notes)
VALUES
	("Genre 1", "Genre Note 1"),
	("Genre 2", "Genre Note 2"),
	("Genre 3", "Genre Note 3"),
	("Genre 4", "Genre Note 4"),
	("Genre 5", "Genre Note 5");

INSERT INTO categories(category_name, notes)
VALUES
	("Category 1", "Category Note 1"),
	("Category 2", "Category Note 2"),
	("Category 3", "Category Note 3"),
	("Category 4", "Category Note 4"),
	("Category 5", "Category Note 5");

INSERT INTO movies (title, director_id, copyright_year, length, genre_id, category_id, rating, notes) 
VALUES
	("Movie 1", 3, "2002", "00:09:00", 2, 2, 8.2, "Movie note 1"),
	("Movie 2", 2, "2001", "00:08:00", 3, 1, 6.2, "Movie note 2"),
	("Movie 3", 1, "2006", "00:06:00", 2, 1, 2.2, "Movie note 3"),
	("Movie 4", 5, "2002", "00:07:00", 5, 4, 1.2, "Movie note 4"),
	("Movie 1", 4, "2020", "00:02:00", 4, 5, 5, "Movie note 5");
-- END

/* 12. Car Rental Database */
USE car_rental;
CREATE TABLE categories(
	id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(50) NOT NULL,
    daily_rate DECIMAL(4,2),
    weekly_rate DECIMAL(6,2),
    monthly_rate DECIMAL(10,2),
    weekend_rate DECIMAL(10,2)
);

INSERT INTO categories(category, daily_rate, weekly_rate, monthly_rate, weekend_rate)
VALUES
	("Category 1", NULL, NULL, NULL, NULL),
	("Category 2", NULL, NULL, NULL, NULL),
	("Category 3", NULL, NULL, NULL, NULL);

CREATE TABLE cars(
	id INT AUTO_INCREMENT PRIMARY KEY,
    plate_number VARCHAR(50) NOT NULL,
    make VARCHAR(50),
    model VARCHAR(50),
    car_year YEAR,
    category_id INT,
    doors SMALLINT,
    picture BLOB,
    car_condition VARCHAR(50),
    available BOOLEAN
);

INSERT INTO cars(plate_number, make, model, car_year, category_id, doors, picture, car_condition, available)
VALUES
	("Plate 1", NULL, NULL, NULL, 2, NULL, NULL, NULL, true),
	("Plate 2", NULL, NULL, NULL, 3, NULL, NULL, NULL, false),
	("Plate 3", NULL, NULL, NULL, 1, NULL, NULL, NULL, true);

CREATE TABLE employees(
	id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    title VARCHAR(50),
    notes TEXT
);

INSERT INTO employees(first_name, last_name, title, notes)
VALUES
	("Employee 1", NULL, NULL, NULL),
	("Employee 2", NULL, NULL, NULL),
	("Employee 3", NULL, NULL, NULL);

CREATE TABLE customers(
	id INT AUTO_INCREMENT PRIMARY KEY,
    driver_licence_number INT NOT NULL,
    full_name VARCHAR(50),
    address VARCHAR(50),
    city VARCHAR(50),
    zip_code VARCHAR(50),
    notes TEXT
);

INSERT INTO customers(driver_licence_number, full_name, address, city, zip_code, notes)
VALUES
	("1", NULL, NULL, NULL, NULL, NULL),
	("2", NULL, NULL, NULL, NULL, NULL),
	("3", NULL, NULL, NULL, NULL, NULL);

CREATE TABLE rental_orders(
	id INT AUTO_INCREMENT PRIMARY KEY, 
    employee_id INT NOT NULL, 
    customer_id INT NOT NULL, 
    car_id INT NOT NULL, 
    car_condition VARCHAR(50), 
    tank_level decimal(5,2), 
    kilometrage_start INT,
    kilometrage_end INT,
    total_kilometrage INT,
    start_date DATE,
    end_date DATE,
    total_days INT,
    rate_applied decimal(5,2),
    tax_rate decimal(5,2),
    order_status VARCHAR(50),
    notes TEXT
);

INSERT INTO rental_orders(employee_id, customer_id, car_id, car_condition, tank_level, kilometrage_start, kilometrage_end, total_kilometrage, start_date, end_date, total_days, rate_applied, tax_rate, order_status, notes)
VALUES
	(1, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(2, 2, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(3, 3, 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
-- END

/* 13. Basic Insert */
-- Only the INSERTS
USE soft_uni;
CREATE TABLE towns(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);
    
CREATE TABLE addresses(
	id INT AUTO_INCREMENT PRIMARY KEY,
    address_text TEXT NOT NULL,
    town_id INT,
    FOREIGN KEY (town_id) REFERENCES towns(id)
);

CREATE TABLE departments(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);
    
CREATE TABLE employees(
	id INT AUTO_INCREMENT PRIMARY KEY, 
    first_name VARCHAR(50) NOT NULL, 
    middle_name VARCHAR(50) NOT NULL, 
    last_name VARCHAR(50) NOT NULL, 
    job_title VARCHAR(50) NOT NULL, 
    department_id INT, 
    hire_date DATE, 
    salary DECIMAL(6, 2), 
    address_id INT,
    FOREIGN KEY(department_id) REFERENCES departments(id),
    FOREIGN KEY(address_id) REFERENCES addresses(id)
);

INSERT INTO towns(name)
VALUES
	("Sofia"),
	("Plovdiv"),
	("Varna"),
	("Burgas");
    
INSERT INTO departments(name)
VALUES
	("Engineering"),
	("Sales"),
	("Marketing"),
	("Software Development"),
	("Quality Assurance");

INSERT INTO employees(first_name, middle_name, last_name, job_title, department_id, hire_date, salary, address_id)
VALUES
	("Ivan", "Ivanov", "Ivanov", ".NET Developer", 4, "2013-02-01", 3500, NULL),
	("Petar", "Petrov", "Petrov", "Senior Engineer", 1, "2004-03-02", 4000, NULL),
	("Maria", "Petrova", "Ivanova", "Intern", 5, "2016-08-28", 525.25, NULL),
	("Georgi", "Terziev", "Ivanov", "CEO", 2, "2007-12-09", 3000, NULL),
	("Peter", "Pan", "Pan", "Intern", 3, "2016-08-28", 599.88, NULL);
-- END

/* 14. Basic Select All Fields */
SELECT * FROM towns;
SELECT * FROM departments;
SELECT * FROM employees;
-- END

/* 15. Basic Select All Fields and Order Them */
SELECT * FROM towns ORDER BY name;
SELECT * FROM departments ORDER BY name;
SELECT * FROM employees ORDER BY salary DESC;
-- END

/* 16. Basic Select Some Fields */
SELECT name FROM towns ORDER BY name;
SELECT name FROM departments ORDER BY name;
SELECT first_name, last_name, job_title, salary FROM employees ORDER BY salary DESC;
-- END

/* 17. Increase Employees Salary */
UPDATE employees
SET salary = salary * 1.1;
SELECT salary FROM employees;
-- END

