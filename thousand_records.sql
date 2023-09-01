-- Connect to your PostgreSQL database using psql.

-- Create a table.
CREATE TABLE sample_table (
    id serial PRIMARY KEY,
    name VARCHAR(255),
    age INT
);

-- Insert 10,000 records into the table using a loop.
DO $$ 
BEGIN 
   FOR i IN 1..10000 LOOP
      INSERT INTO sample_table (name, age) VALUES ('Name' || i, i);
   END LOOP; 
END $$;

-- Confirm that the records have been inserted.
SELECT COUNT(*) FROM sample_table;