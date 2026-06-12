# ==========================================
# AUTHENTICATION CONCEPTS
# ==========================================

# Authentication:
#
# Verifies who the user is.
#
# Example:
# Email + Password


# ==========================================
# AUTHORIZATION
# ==========================================

# Determines what the user can access.
#
# Example:
#
# Admin -> Create, Update, Delete
# User  -> Read Only


# ==========================================
# LOGIN FLOW
# ==========================================

# User
#   ↓
# Login Request
#   ↓
# Verify Credentials
#   ↓
# Generate Token
#   ↓
# Access Protected Routes


# ==========================================
# SESSION AUTHENTICATION
# ==========================================

# Traditional Websites
#
# Server stores user session.
#
# Example:
# Facebook
# Banking Websites


# ==========================================
# TOKEN AUTHENTICATION
# ==========================================

# Modern APIs
#
# Server generates token.
#
# Client sends token with each request.
#
# Example:
#
# Authorization: Bearer token


# ==========================================
# JWT
# ==========================================

# JSON Web Token
#
# Structure:
#
# Header
# Payload
# Signature
#
# Example:
#
# eyJhbGciOiJIUzI1NiIs...


# ==========================================
# WHY AUTHENTICATION?
# ==========================================

# Without Authentication:
#
# Anyone can access API
#
# With Authentication:
#
# Only verified users can access resources


print("Authentication Concepts Learned Successfully")