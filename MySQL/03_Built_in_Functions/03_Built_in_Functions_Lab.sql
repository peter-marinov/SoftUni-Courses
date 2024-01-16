SELECT SUBSTRING('Very Long Text', 4); -- take the symbols after index
SELECT SUBSTRING('Very Long Text', -3); -- take the last symbols
SELECT SUBSTRING('Very Long Text', 4, 5); -- take the symbol from the 4th character up to next 5 characters

USE book_library;

SELECT SUBSTRING(title, 1, 20) AS Title
FROM books;

SELECT CONCAT(SUBSTRING(title, 1, 20), '...') AS Title
FROM books;

SELECT REPLACE('Some string', 's', 'WORKS'); -- REPLACE is case sensitive

SELECT REPLACE(REPLACE('Some string', 's', 'WORKS'), 'S', 'works'); -- In this way we can replace two different key words

-- remove white spaces from the left
SELECT LTRIM('      after spaces');
SELECT LTRIM('			after tabs');
SELECT LTRIM('			

after newline');

SELECT RTRIM('   lalaslda    ');
SELECT TRIM('   lalaslda    ');

SELECT LENGTH('text'), CHAR_LENGTH('text');
SELECT LENGTH(title), CHAR_LENGTH(title)
FROM books;

SELECT LENGTH('асд'), CHAR_LENGTH('асд');

SELECT SUBSTRING('Pesho', 1, 3) = LEFT('Pesho', 3);

SELECT SUBSTRING('Pesho', -3) = RIGHT('Pesho', 3);

SELECT LOWER('Hello'), UPPER('Hello');

-- locate where the string start
SELECT *
FROM books
WHERE LOCATE('the', title, 2) > 0;

SELECT *
FROM books
WHERE LOCATE('the', title) = 0; -- where we do not have the string to be presented

SELECT INSERT('Some text', 3, 2, 're');
SELECT INSERT('Some text', 3, 0, 're');

SELECT 7 DIV 2, 7 / 2;
SELECT 7 MOD 2;

SELECT PI();
SELECT ABS(-10), ABS(10);

SELECT SQRT(16), SQRT(2);

SELECT POW(2, 5), POW(14,7);

SELECT CONV(14, 10, 2);
SELECT CONV(1110, 2, 10);

SELECT ROUND(2.67), ROUND(2.67, 1), ROUND(2.67, 2), ROUND(2.67, 3);
SELECT ROUND(156.37, -2), ROUND(156.37, -1), ROUND(156.37, 0), ROUND(156.37, 1), ROUND(156.37, 2); 

SELECT FLOOR(1.2), CEILING(1.2);
SELECT FLOOR(-3.4), CEILING(-3.4);

SELECT SIGN(7), SIGN(0), SIGN(-9);

SELECT RAND(100);

SELECT RAND() * 5;

-- [0, 1)

-- [0, 1, 2, 3, 4, 5]
SELECT FLOOR(RAND() * 6);
-- [13; 27]
SELECT FLOOR(RAND() * 14) + 13;

-- [min; max]
-- SELECT FLOOR(RAND() * max-min) + min;

SELECT
	title,
    EXTRACT(YEAR FROM year_of_release)
FROM books;

SELECT
	title,
    EXTRACT(DAY FROM year_of_release)
FROM books;

SELECT TIMESTAMPDIFF(DAY, '2024-01-01', '2024-01-16');
SELECT YEAR('2024-01-01'), EXTRACT(YEAR FROM '2024-01-01');

SELECT
	title,
    DATE_FORMAT(year_of_release, '%Y %c %e'),
    DATE_FORMAT(year_of_release, '%y %m %d')
FROM books;

SELECT NOW();

SELECT *
FROM books
WHERE title LIKE 'The%';

SELECT *
FROM books
WHERE title LIKE 'a%' OR title LIKE 'b%' OR title LIKE 'c%';

/* 01. Find Book Titles */
SELECT title
FROM books
WHERE SUBSTRING(title, 1, 4) = 'The ' -- is not case sensitive
ORDER BY id;
-- END

/* 02. Replace Titles */
SELECT
	REPLACE(title, 'The', '***') as 'title'
FROM books
WHERE SUBSTRING(title, 1, 4) = 'The '
ORDER BY id;
-- END

/* 03. Sum Cost of All Books */
SELECT 
	ROUND(SUM(cost), 2)
FROM books;
-- END

/* 04. Days Lived */
SELECT
	CONCAT_WS(' ', first_name, last_name),
    ABS(TIMESTAMPDIFF(DAY, died, born)) AS 'Days Lived'
FROM authors;
-- END

/* 05. Harry Potter Books */
SELECT title
FROM books
WHERE title LIKE 'Harry Potter%'
ORDER BY id;
-- END
