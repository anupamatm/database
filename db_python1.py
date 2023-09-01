import psycopg2

# Database connection parameters
db_params = {
    "dbname": "thousand_records",
    "user": "postgres",
    "password": "root",
    "host": "localhost",
    "port": "5432"

}

try:
    # Connect to the database
    connection = psycopg2.connect(**db_params)

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Execute a view to retrieve all items
    cursor.execute("SELECT * FROM all_items_view")
    
    # Fetch all rows from the view
    all_items = cursor.fetchall()
    
    # Print all items
    print("All Items:")
    for item in all_items:
        print(f"Item ID: {item[0]}, Item Name: {item[1]}, Item Price: {item[2]}")

    # Prompt user for an item name
    item_name = input("Enter an item name to display details (or leave empty to skip): ").strip()

    if item_name:
        # Execute a query to display details for the specified item name
        cursor.execute("SELECT * FROM all_items_view WHERE item_name = %s", (item_name,))
        
        # Fetch the result for the specified item
        item_details = cursor.fetchone()
        
        if item_details:
            print(f"Details for Item Name: {item_name}")
            print(f"Item ID: {item_details[0]}, Item Name: {item_details[1]}, Item Price: {item_details[2]}")
        else:
            print(f"No details found for Item Name: {item_name}")
    
    # Commit the transaction (if needed)
    connection.commit()

except (Exception, psycopg2.Error) as error:
    print(f"Error: {error}")

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
