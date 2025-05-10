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
    return {"result": result}


LLAMA_API_URL = os.getenv("LLAMA_API_URL")
LLAMA_API_KEY = os.getenv("LLAMA_API_KEY")

#data = chat()
'''
chore = data['chore completed']
time = data['time taken']
short_description = data['short description']
name = "bob"
'''

suggestion()

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('chores_manager.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS chore_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_name TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS chores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_id INTEGER,
    chore_type_id INTEGER,
    description TEXT,
    completed BOOLEAN DEFAULT 0,
    FOREIGN KEY (person_id) REFERENCES people(id),
    FOREIGN KEY (chore_type_id) REFERENCES chore_types(id)
);
''')

# Insert sample data
cursor.execute('delete from people')
cursor.execute('delete from chores')
cursor.execute('delete from chore_types')

cursor.executemany('INSERT INTO people (name) VALUES (?)', [('Alice',), ('Bob',), ('Charlie',)])
cursor.executemany('INSERT INTO people (name) VALUES (?)', [('Alice',), ('Bob',), ('Charlie',)])
cursor.executemany('INSERT INTO chore_types (type_name) VALUES (?)', [('Cleaning',), ('Cooking',), ('Laundry',)])
cursor.executemany('INSERT INTO chores (person_id, chore_type_id, description) VALUES (?, ?, ?)', [
    (1, 1, 'Vacuum the living room'),
    (2, 2, 'Cook dinner'),
    (3, 3, 'Do the laundry')
])

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


# Close the connection
conn.close()
