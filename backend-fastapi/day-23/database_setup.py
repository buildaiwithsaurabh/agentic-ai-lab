import sqlite3

# ==========================================
# USER DATABASE SETUP
# ==========================================

conn = sqlite3.connect("users.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

conn.commit()

print("Users Table Created Successfully")

conn.close()

print("Database Connection Closed")