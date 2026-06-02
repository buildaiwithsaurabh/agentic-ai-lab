# URL Shortener Simulation

## Overview

This project is a simple command-line URL Shortener built using Python. It simulates the core functionality of services like Bitly and TinyURL by generating unique short codes for long URLs and allowing users to retrieve the original URLs later.

The project was developed as part of my Python learning journey to strengthen problem-solving skills and gain hands-on experience with data structures, functions, and menu-driven applications.

---

# Features

### Shorten URLs

Generate a unique short code for any URL.

Example:

```text
Original URL:
https://github.com/buildaiwithsaurabh/agentic-ai-lab

Short URL:
https://short.ly/Ab12Xy
```

---

### Retrieve Original URL

Convert a short code back into its original URL.

Example:

```text
Enter short code:
Ab12Xy

Original URL:
https://github.com/buildaiwithsaurabh/agentic-ai-lab
```

---

### View Stored URLs

Display all shortened URLs currently stored in the application.

Example:

```text
Ab12Xy -> https://github.com/buildaiwithsaurabh/agentic-ai-lab
K9mP4q -> https://python.org
```

---

# Concepts Practiced

This project helped reinforce several important Python concepts:

* Functions
* Dictionaries
* Loops
* Conditional Statements
* Random Module
* String Manipulation
* Menu-Driven Programs
* CRUD-like Operations

---

# Technologies Used

* Python 3
* VS Code
* PowerShell

---

# Project Structure

```text
url-shortener/
│
├── url_shortener.py
└── README.md
```

---

# How It Works

### Step 1

User enters a long URL.

### Step 2

The application generates a random 6-character short code.

### Step 3

The short code and original URL are stored in a dictionary.

### Step 4

Users can retrieve the original URL using the generated short code.

---

# Sample Workflow

```text
===== URL SHORTENER =====

1. Shorten URL
2. Retrieve URL
3. View All URLs
4. Exit

Enter choice: 1

Enter URL:
https://github.com/buildaiwithsaurabh/agentic-ai-lab

Short URL:
https://short.ly/X7aB2K
```

---

# Future Improvements

Potential enhancements for this project include:

* JSON File Storage
* SQLite Database Integration
* URL Analytics
* Click Tracking
* Custom Short Codes
* Expiration Dates
* FastAPI REST API Version
* Web-Based User Interface

---

# Key Learnings

Through this project, I gained practical experience in:

* Designing simple software systems
* Managing data using dictionaries
* Generating unique identifiers
* Building interactive command-line applications
* Applying problem-solving techniques using Python

---

# Conclusion

This URL Shortener Simulation demonstrates the fundamental concepts behind modern URL shortening services. While simplified, it provides valuable hands-on experience with Python programming, application design, and data management.

As I continue my journey toward Backend Development, AI Engineering, and Agentic AI Systems, projects like this help strengthen the foundation required to build scalable real-world applications.

🚀 Built as part of my Python learning and Build-in-Public journey.
