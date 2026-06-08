# ==========================================
# PRODUCT DATABASE MANAGER
# ==========================================

# Project:
#
# Product Database Manager
#
# Features:
#
# 1. Create Table
# 2. Insert Product
# 3. View Products
# 4. Update Product
# 5. Delete Product


import sqlite3


# ==========================================
# CONNECT DATABASE
# ==========================================

conn = sqlite3.connect("products.db")

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

conn.commit()


# ==========================================
# INSERT PRODUCT
# ==========================================

cursor.execute("""
INSERT INTO products (name, price)
VALUES (?, ?)
""", ("Laptop", 50000))

conn.commit()

print("Product Inserted Successfully")


# ==========================================
# VIEW PRODUCTS
# ==========================================

print("\n===== ALL PRODUCTS =====")

cursor.execute("SELECT * FROM products")

products = cursor.fetchall()

for product in products:
    print(product)


# ==========================================
# UPDATE PRODUCT
# ==========================================

cursor.execute("""
UPDATE products
SET price = ?
WHERE id = ?
""", (55000, 1))

conn.commit()

print("\nProduct Updated Successfully")


# ==========================================
# VIEW UPDATED PRODUCTS
# ==========================================

print("\n===== UPDATED PRODUCTS =====")

cursor.execute("SELECT * FROM products")

products = cursor.fetchall()

for product in products:
    print(product)


# ==========================================
# DELETE PRODUCT
# ==========================================

cursor.execute("""
DELETE FROM products
WHERE id = ?
""", (1,))

conn.commit()

print("\nProduct Deleted Successfully")


# ==========================================
# FINAL PRODUCTS
# ==========================================

print("\n===== FINAL PRODUCTS =====")

cursor.execute("SELECT * FROM products")

products = cursor.fetchall()

for product in products:
    print(product)


# ==========================================
# CLOSE DATABASE
# ==========================================

conn.close()

print("\nDatabase Connection Closed")