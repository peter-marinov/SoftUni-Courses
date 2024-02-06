CREATE SCHEMA `triple_s` DEFAULT CHARACTER SET utf8 ;

USE triple_s;


CREATE TABLE pictures(
	id INT PRIMARY KEY AUTO_INCREMENT,
    url VARCHAR(100) NOT NULL,
    added_on DATETIME NOT NULL
);

CREATE TABLE categories(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL UNIQUE
);

CREATE TABLE products(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL UNIQUE,
    best_before DATE,
    price DECIMAL(10,2) NOT NULL,
    description TEXT,
    category_id INT NOT NULL,
    picture_id INT NOT NULL,
    
    FOREIGN KEY (category_id) REFERENCES categories(id),
    FOREIGN KEY (picture_id) REFERENCES pictures(id)
);

CREATE TABLE towns(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE addresses(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE,
    town_id INT NOT NULL,
    
    FOREIGN KEY (town_id) REFERENCES towns(id)
);

CREATE TABLE stores(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL UNIQUE,
    rating FLOAT NOT NULL,
    has_parking TINYINT(1) DEFAULT 0,
    address_id INT NOT NULL,
    
    FOREIGN KEY (address_id) REFERENCES addresses(id)
);

CREATE TABLE products_stores(
	product_id INT NOT NULL,
    store_id INT NOT NULL,
    
    PRIMARY KEY (product_id, store_id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (store_id) REFERENCES stores(id)
);

CREATE TABLE employees(
	id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(15) NOT NULL,
    middle_name CHAR(1),
    last_name VARCHAR(20) NOT NULL,
    salary DECIMAL(19,2) DEFAULT 0,
    hire_date DATE NOT NULL,
    manager_id INT,
    store_id INT NOT NULL,
    
    FOREIGN KEY (manager_id) REFERENCES employees(id),
    FOREIGN KEY (store_id) REFERENCES stores(id)
);