-- Use the database
USE hbtn_0d_usa;

-- Identify duplicate entries for 'California'
SELECT id, name FROM states WHERE name = 'California';

-- Delete duplicate entries for 'California' except the one with the desired ID
DELETE FROM states WHERE id = 1;

-- Verify that there is only one entry for 'California'
SELECT * FROM states WHERE name = 'California';

-- Now, run the original script
SOURCE 8-cities_of_california_subquery.sql;

