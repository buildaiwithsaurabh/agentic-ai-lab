from database import engine
from database import SessionLocal

from models import Base
from models import User

# ==========================================
# CREATE TABLES
# ==========================================

Base.metadata.create_all(
    bind=engine
)

print("Users Table Created Successfully")

# ==========================================
# DATABASE SESSION
# ==========================================

db = SessionLocal()

# ==========================================
# CREATE USER
# ==========================================

new_user = User(
    username="saurabh",
    email="saurabh@gmail.com",
    password="admin123"
)

db.add(new_user)

db.commit()

print("User Added Successfully")

# ==========================================
# READ USERS
# ==========================================

users = db.query(User).all()

print("\nAll Users:\n")

for user in users:

    print(
        user.id,
        user.username,
        user.email
    )

# ==========================================
# CLOSE SESSION
# ==========================================

db.close()

print("\nDatabase Session Closed")