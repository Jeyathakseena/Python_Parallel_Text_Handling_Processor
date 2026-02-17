import threading
import time
import sqlite3

rules = {
    "excellent": 1,
    "good": 0.5,
    "bad": -0.5,
    "poor": -1
}

conn = sqlite3.connect("textdb.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    score REAL
)
""")

print("Table created successfully")

conn.commit()
conn.close()


def process_file(filename):
    with open(filename, "r") as file:
        text = file.read().lower()

    score= 0

    for word, value in rules.items():
        score += text.count(word)* value

    conn = sqlite3.connect("textdb.db")
    cursor = conn.cursor()

    cursor.execute (
        "INSERT into results (filename,score) VALUES (?,?)",
        (filename,score)
    )
    conn.commit()
    conn.close()
    print("File:", filename)
    print("Score:", score)
    print("------------")

files = ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt"]

start_time= time.time()

threads= []
for filename in files:
    t= threading.Thread(target=process_file, args=(filename,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()   

end_time= time.time()

print("Total Excecution Time:", end_time-start_time)