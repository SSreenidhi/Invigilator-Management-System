import sqlite3

# Connect to database (or create it if it doesn't exist)
conn = sqlite3.connect("faculty.db")
cursor = conn.cursor()

# Create table for faculty duty count
cursor.execute('''
CREATE TABLE IF NOT EXISTS Faculty (
    name TEXT PRIMARY KEY,
    department TEXT,
    invigilation_count INTEGER DEFAULT 0
)
''')


# Create table to store invigilation assignments
cursor.execute('''
CREATE TABLE IF NOT EXISTS InvigilationAssignments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    subject TEXT,
    day TEXT,
    slots TEXT,
    teacher TEXT
)
''')

conn.commit()
conn.close()
print("✅ faculty.db initialized successfully.")
