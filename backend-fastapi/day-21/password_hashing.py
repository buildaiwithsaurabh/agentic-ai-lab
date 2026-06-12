# ==========================================
# PASSWORD HASHING
# ==========================================

# Install:
#
# pip install passlib[bcrypt]


from passlib.context import CryptContext  


# Create Hashing Context
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# ==========================================
# HASH PASSWORD
# ==========================================

password = "admin123"

hashed_password = pwd_context.hash(password)

print("Original Password:")
print(password)

print("\nHashed Password:")
print(hashed_password)


# ==========================================
# VERIFY PASSWORD
# ==========================================

is_valid = pwd_context.verify(
    "admin123",
    hashed_password
)

print("\nPassword Match:")
print(is_valid)


# ==========================================
# WRONG PASSWORD TEST
# ==========================================

is_valid = pwd_context.verify(
    "wrongpassword",
    hashed_password
)

print("\nWrong Password Match:")
print(is_valid)


# ==========================================
# WHY HASHING?
# ==========================================

# Never store:
#
# password = "admin123"
#
# Store:
#
# $2b$12$Qx....
#
# Benefits:
#
# ✓ Secure
# ✓ Irreversible
# ✓ Industry Standard