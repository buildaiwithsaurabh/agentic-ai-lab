import sqlite3

# ==========================================
# INVENTORY DATABASE SETUP
# ==========================================

conn = sqlite3.connect("inventory.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
)
""")

conn.commit()

print("Inventory Table Created Successfully")

conn.close()

print("Database Connection Closed")