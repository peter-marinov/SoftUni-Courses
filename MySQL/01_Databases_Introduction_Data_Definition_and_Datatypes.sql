USE gamebar;
SELECT * FROM employees;

CREATE TABLE people (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(50) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

SELECT first_name, last_name
FROM employees
LIMIT 1;

/* 01. Create Tables */
CREATE TABLE employees (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

CREATE TABLE categories (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE products (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    category_id INT NOT NULL
);
-- END

INSERT INTO employees VALUES(10, "Query", NULL);

INSERT INTO employees(first_name, last_name)
VALUES("Field", "List");

SELECT * FROM employees;

/* 02. Insert Data in Tables */
INSERT INTO employees(first_name, last_name)
VALUES
	("Field", "List"),
	("Second", "Entry"),
	("Third", "Employee");
-- END

/* 03. Alter Tables */
ALTER TABLE employees
ADD COLUMN middle_name VARCHAR(50) NOT NULL;
-- END

/* 04. Adding Constraints */
ALTER TABLE products
ADD INDEX `fk_category_id_idx` (`category_id` ASC) VISIBLE;

ALTER TABLE products
ADD CONSTRAINT `fk_category_id`
  FOREIGN KEY (`category_id`)
  REFERENCES categories (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
-- END

/* 05. Modifying Columns */
ALTER TABLE employees
MODIFY COLUMN middle_name VARCHAR(100);
-- END
