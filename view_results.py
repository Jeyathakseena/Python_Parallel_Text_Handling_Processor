import sqlite3

conn = sqlite3.connect("textdb.db")
cursor = conn.cursor()

cursor.execute ("SELECT * FROM results")

rows= cursor.fetchall()

for row in rows:
    print(row)

conn.close()