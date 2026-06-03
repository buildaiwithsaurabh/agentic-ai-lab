# Backend Development Fundamentals

## 1. What is Backend?

### Definition

Backend is the part of an application that runs on a server and handles:

* Business Logic
* Authentication
* Database Operations
* API Processing
* Data Storage
* Security

The backend is not directly visible to users.

Users interact with the frontend, while the frontend communicates with the backend.

---

### Real-World Example

When you log into Instagram:

1. You enter username and password.
2. Frontend sends data to backend.
3. Backend verifies credentials.
4. Backend checks database.
5. Backend returns response.
6. Frontend displays result.

---

### Backend Responsibilities

* User Authentication
* Authorization
* Data Validation
* Database Management
* API Development
* Payment Processing
* Logging & Monitoring

---

# 2. Client vs Server

## Client

The client is the application used by the user.

Examples:

* Web Browser
* Mobile App
* Desktop Application

Examples:

* Chrome
* Edge
* Instagram App
* WhatsApp

---

## Server

A server is a machine or application that provides services and data to clients.

Examples:

* FastAPI Server
* Node.js Server
* Django Server

---

## Communication Flow

```text
Client
   ↓ Request
Server
   ↓ Response
Client
```

Example:

```text
Browser
   ↓
GET /users
   ↓
Backend Server
   ↓
User Data
   ↓
Browser
```

---

## Simple Analogy

Restaurant Example:

### Client

Customer

### Server

Waiter

### Database

Kitchen

### Response

Food

Flow:

```text
Customer
   ↓
Order Food
   ↓
Waiter
   ↓
Kitchen
   ↓
Food Ready
   ↓
Customer
```

---

# 3. HTTP (HyperText Transfer Protocol)

## Definition

HTTP is the communication protocol used between clients and servers.

It defines how requests and responses are sent over the internet.

---

## Example

```text
Browser
   ↓
HTTP Request
   ↓
Server
   ↓
HTTP Response
   ↓
Browser
```

---

## Common HTTP Methods

### GET

Retrieve data.

Example:

```http
GET /users
```

Meaning:

```text
Give me all users
```

---

### POST

Create new data.

Example:

```http
POST /users
```

Meaning:

```text
Create a new user
```

---

### PUT

Update existing data completely.

Example:

```http
PUT /users/1
```

Meaning:

```text
Update user with ID 1
```

---

### PATCH

Update part of existing data.

Example:

```http
PATCH /users/1
```

Meaning:

```text
Update only selected fields
```

---

### DELETE

Remove data.

Example:

```http
DELETE /users/1
```

Meaning:

```text
Delete user with ID 1
```

---

# 4. REST API

## Definition

REST stands for:

```text
Representational State Transfer
```

REST is a standard way of designing APIs.

It uses:

* HTTP Methods
* URLs
* JSON

to communicate between systems.

---

## REST API Example

Get Users:

```http
GET /users
```

Get Single User:

```http
GET /users/1
```

Create User:

```http
POST /users
```

Update User:

```http
PUT /users/1
```

Delete User:

```http
DELETE /users/1
```

---

## Why REST APIs?

Because they are:

* Simple
* Scalable
* Easy to understand
* Language Independent

---

# 5. Request and Response

## Request

A request is sent from client to server.

Contains:

* URL
* Method
* Headers
* Body

Example:

```http
POST /users
```

Body:

```json
{
  "name": "Saurabh",
  "email": "saurabh@example.com"
}
```

---

## Response

A response is returned by the server.

Contains:

* Status Code
* Headers
* Data

Example:

```json
{
  "message": "User Created Successfully"
}
```

---

## Flow

```text
Client
   ↓ Request
Server
   ↓ Response
Client
```

---

# 6. JSON

## Definition

JSON stands for:

```text
JavaScript Object Notation
```

JSON is the most common format for exchanging data between applications.

---

## JSON Example

```json
{
  "name": "Saurabh",
  "age": 21,
  "skills": [
    "Python",
    "FastAPI",
    "AI"
  ]
}
```

---

## JSON Rules

### Key-Value Pair

```json
{
  "name": "Saurabh"
}
```

---

### Strings use double quotes

Correct:

```json
{
  "name": "Saurabh"
}
```

Wrong:

```json
{
  'name': 'Saurabh'
}
```

---

## Why JSON?

Because it is:

* Lightweight
* Human Readable
* Easy to Parse
* Supported Everywhere

---

# 7. HTTP Status Codes

Status codes tell clients whether a request succeeded or failed.

---

## 200 OK

Request successful.

Example:

```http
200 OK
```

Meaning:

```text
Everything worked correctly.
```

---

## 201 Created

New resource created successfully.

Example:

```http
201 Created
```

Meaning:

```text
User created successfully.
```

---

## 400 Bad Request

Client sent invalid data.

Example:

```text
Missing required field.
```

---

## 401 Unauthorized

Authentication required.

Example:

```text
Login required.
```

---

## 403 Forbidden

User authenticated but lacks permission.

Example:

```text
Admin access required.
```

---

## 404 Not Found

Requested resource does not exist.

Example:

```http
GET /user/999
```

Response:

```http
404 Not Found
```

---

## 500 Internal Server Error

Server-side failure.

Example:

```text
Database connection failed.
```

---

# Complete Backend Flow

```text
Frontend (Client)
        ↓
HTTP Request
        ↓
FastAPI Backend
        ↓
Business Logic
        ↓
Database
        ↓
JSON Response
        ↓
Frontend
```

---

# Why Learn These Concepts?

Every modern AI application uses them:

* ChatGPT
* Perplexity
* Cursor
* AI Agents
* ATS Systems
* SaaS Platforms

Before building Agentic AI systems, you must understand how applications communicate, store data, and expose APIs.

These concepts form the foundation of Backend Development and AI Engineering.
