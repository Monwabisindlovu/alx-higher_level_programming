-- Create the table 'first_table' if it doesn't exist
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);

-- Print the full description of the table 'first_table'
SHOW CREATE TABLE first_table;
