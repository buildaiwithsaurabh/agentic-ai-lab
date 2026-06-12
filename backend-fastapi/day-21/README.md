# Day 21 - Authentication Fundamentals

## Overview

Day 21 focused on understanding authentication and security concepts used in modern backend applications.

Authentication is essential for protecting APIs and ensuring that only verified users can access resources.

---

## Topics Covered

### Authentication

Authentication answers:

```text
Who are you?
```

Example:

```text
Email
Password
```

---

### Authorization

Authorization answers:

```text
What are you allowed to do?
```

Example:

```text
Admin -> Full Access

User -> Limited Access
```

---

### Session Authentication

Traditional authentication method where the server stores user sessions.

Used by:

- Facebook
- Banking Applications
- Traditional Websites

---

### Token Authentication

Modern API authentication method.

The server generates a token and the client sends it with each request.

Example:

```text
Authorization: Bearer token
```

---

### JWT (JSON Web Token)

A popular token format used in modern APIs.

Structure:

```text
Header
Payload
Signature
```

---

### Password Hashing

Passwords should never be stored in plain text.

Example:

❌ Unsafe

```text
admin123
```

✅ Secure

```text
$2b$12$....
```

Hashing helps protect user credentials even if the database is compromised.

---

## Files

### auth_concepts.py

Covers:

- Authentication
- Authorization
- Login Flow
- Session Authentication
- Token Authentication
- JWT Basics

### password_hashing.py

Demonstrates:

- Password Hashing
- Password Verification
- bcrypt Hash Generation

---

## Technologies Used

- Python
- Passlib
- bcrypt

---

## Installation

```bash
pip install passlib[bcrypt]
```

---

## Run Files

### Authentication Concepts

```bash
python auth_concepts.py
```

### Password Hashing

```bash
python password_hashing.py
```

---

## Learning Outcome

Day 21 helped me understand how modern applications secure user accounts using authentication, authorization, tokens, and password hashing.

These concepts form the foundation for building secure APIs and user management systems.

---

## Next Step

Day 22:

- User Registration API
- User Database
- Store Hashed Passwords
- Registration Workflow
