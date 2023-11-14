-- List all records of the table 'second_table'
-- Exclude rows without a name value
-- Ordered by descending score
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
