# ==========================================
# DATABASE SETUP
# ==========================================

# Purpose:
# Create SQLite database and products table


import sqlite3


# Connect Database
conn = sqlite3.connect("products.db")

cursor = conn.cursor()


# Create Products Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL
)
""")


conn.commit()

print("Products Table Created Successfully")


conn.close()

print("Database Connection Closed")