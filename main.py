import sqlite3
import psycopg2
import os

import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

# Connect to the database
try:
    connection = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        dbname=DBNAME
    )
    print("Connection successful!")
    
    # Create a cursor to execute SQL queries
    cursor = connection.cursor()
    
    # Example query
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    print("Current Time:", result)

    # Close the cursor and connection
    cursor.close()
    connection.close()
    print("Connection closed.")

except Exception as e:
    print(f"Failed to connect: {e}")


cur = conn.cursor()
# Insert data into the 'chores' table
insert_query = """
INSERT INTO chores (id, name, description, due_date)
VALUES (%s, %s, %s, %s);
"""
data_to_insert = [
    (1, 'Clean kitchen', 'Wash dishes and wipe counters', '2025-05-15'),
    (2, 'Vacuum living room', 'Vacuum the carpet and sofa', '2025-05-16'),
    (3, 'Laundry', 'Wash and fold clothes', '2025-05-17')
]

for data in data_to_insert:
    cur.execute(insert_query, data)

# Commit the transaction
conn.commit()

# Fetch and display the inserted data
cur.execute("SELECT * FROM chores LIMIT 5;")
rows = cur.fetchall()

for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()