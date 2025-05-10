import sqlite3
import os
import requests
from llama import chat
from llama import suggestion
import json

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"], 
    allow_methods=["*"], 
    allow_headers=["*"],
    allow_credentials=True
    )

class Task(BaseModel):
    text: str
    
@app.post("/task")
def process(task: Task):
    result = chat(task.text)

    chore = data['chore completed']
    time = data['time taken']
    short_description = data['short description']
    name = "Bob"

    cursor.executemany('INSERT INTO people (name) VALUES (?)', [('Alice',), ('Bob',), ('Charlie',)])
    cursor.executemany('INSERT INTO chore_types (type_name) VALUES (?)', [('Cleaning',), ('Cooking',), ('Laundry',)])

    return {"result": result}


def get_all_chores():
    # Connect to the SQLite database
    conn = sqlite3.connect("chores_manager.db")
    cursor = conn.cursor()

    # Predefined query
    query = "SELECT * FROM chores"

    # Execute the predefined query
    cursor.execute(query)
    # Fetch and return all results
    results = cursor.fetchall()
    ls = []
    for result in results:
        cur = {}
        print(result[0])
        cursor.execute("select name from people where id = ?", (result[1],))
        name = cursor.fetchall()
        print("name: ", name[0][0])
        cur["name"] = name[0][0]

        cursor.execute("select type_name from chore_types where id = ?", (result[2],))
        type = cursor.fetchall()
        cur["type"] = type[0][0]
        cur["desc"] = result[3] #desc
        cur["min"] = result[4] #minutes
        print(cur)
        ls.append(cur)
        #
    # Close the connection
    cursor.close()
    conn.close()

    return ls



LLAMA_API_URL = os.getenv("LLAMA_API_URL")
LLAMA_API_KEY = os.getenv("LLAMA_API_KEY")

#data = chat()
'''
chore = data['chore completed']
time = data['time taken']
short_description = data['short description']
name = "bob"

cursor.execute('INSERT INTO chores (person_id, chore_type_id, description) VALUES (?, ?, ?)', [
    (1, 1, 'Vacuum the living room')
])

'''

#suggestion()

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('chores_manager.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS people (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS chore_types (
    id INTEGER PRIMARY KEY,
    type_name TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS chores (
    id INTEGER PRIMARY KEY,
    person_id INTEGER,
    chore_type_id INTEGER,
    description TEXT,
    minutes int DEFAULT 0,
    FOREIGN KEY (person_id) REFERENCES people(id),
    FOREIGN KEY (chore_type_id) REFERENCES chore_types(id)
);
''')

# Insert sample data
'''
cursor.execute('delete from people')
cursor.execute('delete from chores')
cursor.execute('delete from chore_types')


cursor.executemany('INSERT INTO people (name) VALUES (?)', [('Alice',), ('Bob',), ('Charlie',)])
cursor.executemany('INSERT INTO people (name) VALUES (?)', [('Alice',), ('Bob',), ('Charlie',)])
cursor.executemany('INSERT INTO chore_types (type_name) VALUES (?)', [('Cleaning',), ('Cooking',), ('Laundry',)])
cursor.executemany('INSERT INTO chores (person_id, chore_type_id, description, minutes) VALUES (?, ?, ?)', [
    (1, 1, 'Vacuum the living room', 10),
    (2, 2, 'Cook dinner', 10),
    (3, 3, 'Do the laundry', 5)
])
'''

# Commit changes
conn.commit()

# Print data from tables
print("People:")
for row in cursor.execute('SELECT * FROM people'):
    print(row)

print("\nChore Types:")
for row in cursor.execute('SELECT * FROM chore_types'):
    print(row)

print("\nChores:")
for row in cursor.execute('SELECT * FROM chores'):
    print(row)

#get_all_chores()

# Close the connection
conn.close()



