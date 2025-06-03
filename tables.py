import sqlite3
import pandas as pd

# Connect to your SQLite DB
conn = sqlite3.connect("faculty.db")

# Load tables into DataFrames
faculty_df = pd.read_sql_query("SELECT * FROM Faculty", conn)
assignments_df = pd.read_sql_query("SELECT * FROM InvigilationAssignments", conn)

# Display
print("FACULTY TABLE")
print(faculty_df)

print("\nASSIGNMENTS TABLE")
print(assignments_df)

conn.close()
