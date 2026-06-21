# Day 29 - Authentication Backend Project

## Overview

Day 29 focused on building a complete authentication backend using FastAPI and SQLAlchemy with a professional project architecture.

The application provides user registration, login, password hashing, JWT authentication, and modular code organization commonly used in production backend systems.

---

## Features

### Authentication

* User Registration
* User Login
* Password Hashing
* JWT Token Generation
* Protected Authentication Flow

### Architecture

* Routers
* Services
* Models
* Schemas
* Configuration Management
* Dependency Injection

---

## Project Structure

```text
day-29/
│
├── app/
│   ├── routers/
│   │   ├── auth.py
│   │   └── users.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   └── user_service.py
│   │
│   ├── models/
│   │   └── user.py
│   │
│   ├── schemas/
│   │   └── user_schema.py
│   │
│   ├── database.py
│   ├── config.py
│   └── main.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* FastAPI
* SQLAlchemy
* SQLite
* JWT
* Passlib
* Python-Jose

---

## API Endpoints

### Register User

```http
POST /auth/register
```

### Login User

```http
POST /auth/login
```

### Users Endpoint

```http
GET /users/
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
cd app

uvicorn main:app --reload
```

---

## API Documentation

```text
http://127.0.0.1:8000/docs
```

---

## Concepts Practiced

* Authentication
* Authorization Fundamentals
* Password Hashing
* JWT Tokens
* SQLAlchemy ORM
* Environment Variables
* Dependency Injection
* Professional FastAPI Architecture

---

## Learning Outcome

This project combines all major backend concepts learned so far into a single production-style application. It demonstrates how authentication systems are implemented using FastAPI, SQLAlchemy, and JWT while following a scalable project structure.

---

## Next Step

Day 30

* PostgreSQL Integration
* Deployment Basics
* Backend Revision
* Production Readiness
