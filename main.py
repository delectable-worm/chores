import sqlite3
import psycopg2
print("hello")
try:
    conn = psycopg2.connect(
        host="zwwnhuuyyakhedbuiepf.supabase.co",
        port=5432,
        dbname="postgres",
        user="postgres",
        password="!ilovewomen!"
    )
    print("connected")
except Exception as e:
    print("Error connecting to the database:", e)



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