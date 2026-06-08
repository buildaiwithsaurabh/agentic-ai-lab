# ==========================================
# SQLITE BASICS
# ==========================================

# Definition:
#
# SQLite is a lightweight database
# built into Python.
#
# It stores data in a single file.


import sqlite3


# ==========================================
# CREATE DATABASE
# ==========================================

# Creates products.db if it does not exist

conn = sqlite3.connect("products.db")

print("Database Connected Successfully")


# ==========================================
# CREATE CURSOR
# ==========================================

cursor = conn.cursor()


# ==========================================
# CREATE TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (

    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL
)
""")


print("Table Created Successfully")


# ==========================================
# SAVE CHANGES
# ==========================================

conn.commit()


# ==========================================
# CLOSE CONNECTION
# ==========================================

conn.close()

print("Database Connection Closed")