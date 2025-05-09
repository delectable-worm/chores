import sqlite3
con = sqlite3.connect("data.db")

cur = con.cursor()

cur.execute("CREATE TABLE chore(id INT PRIMARY KEY, name VARCHAR(255), description TEXT, type VARCHAR(255))")
cur.execute("CREATE TABLE people(id INT PRIMARY KEY, name VARCHAR(255) NOT NULL)")
cur.execute("CREATE TABLE chore_instances(id INT PRIMARY KEY, chore_id int)")

