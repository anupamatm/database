
-- Create a table to store item information.
CREATE TABLE items (
    item_id serial PRIMARY KEY,
    item_name VARCHAR(255),
    item_price numeric(10, 2)
);

-- Insert some sample data into the table.
INSERT INTO items (item_name, item_price) VALUES
    ('Item 1', 10.99),
    ('Item 2', 5.49),
    ('Item 3', 8.99),
    ('Item 4', 12.99),
    ('Item 5', 7.49);

-- Insert some sample data into the table.
INSERT INTO items (item_name, item_price) VALUES
    ('Item 1', 10.99),
    ('Item 2', 5.49),
    ('Item 3', 8.99),
    ('Item 4', 12.99),
    ('Item 5', 7.49);

-- Create a stored procedure to calculate the total price.
CREATE OR REPLACE FUNCTION calculate_total_price()
RETURNS numeric(10, 2) AS $$
DECLARE
    total numeric(10, 2);  -- Initialize the total to 0.
    item_record record;    -- Declare a record variable to hold query results.
BEGIN
    total := 0.00;  -- Initialize the total to 0.

    -- Use a cursor to fetch rows from the query result.
    FOR item_record IN (SELECT item_price FROM items) LOOP
        total := total + item_record.item_price;  -- Add the item's price to the total.
    END LOOP;

    RETURN total;  -- Return the total.
END;
$$ LANGUAGE plpgsql;




CREATE OR REPLACE FUNCTION calculate_sum(a integer, b integer)
 RETURNS integer AS $$
DECLARE
    result integer;
BEGIN
   result := a + b;
   RETURN result;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE VIEW all_items_view AS
SELECT item_id, item_name, item_price
FROM items;