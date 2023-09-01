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

    # Execute a stored procedure
    cursor.callproc("calculate_total_price")

    # Fetch the result of the stored procedure
    total_price = cursor.fetchone()[0]

    # Commit the transaction (if needed)
    connection.commit()

    # Print the result
    print(f"Total Price: {total_price}")

except (Exception, psycopg2.Error) as error:
    print(f"Error: {error}")

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
