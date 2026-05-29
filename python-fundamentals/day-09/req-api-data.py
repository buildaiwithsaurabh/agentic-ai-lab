# REQUESTING DATA FROM AN API IN PYTHON

# Definition:
# An API (Application Programming Interface) allows
# different applications to communicate and exchange data.

# A Request is sent to an API endpoint,
# and the API returns a Response containing data.

# Most modern APIs return data in JSON format.


# ============================================================
# WHAT HAPPENS BEHIND THE SCENES?
# ============================================================

# Python Application
#        ↓
# Send HTTP Request
#        ↓
# API Server
#        ↓
# Send HTTP Response
#        ↓
# JSON Data Returned


# Example:

# Client Request
# GET https://api.example.com/users

# Server Response
# {
#   "id": 1,
#   "name": "John"
# }


# ============================================================
# INSTALL REQUESTS LIBRARY
# ============================================================

# pip install requests


# ============================================================
# BASIC API REQUEST
# ============================================================

import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print(response)


# Output:
# <Response [200]>


# ============================================================
# STATUS CODES
# ============================================================

# 200 = Success
# 201 = Created
# 400 = Bad Request
# 401 = Unauthorized
# 403 = Forbidden
# 404 = Not Found
# 500 = Server Error


# Example:

if response.status_code == 200:
    print("Request Successful")
else:
    print("Request Failed")


# ============================================================
# GET JSON DATA
# ============================================================

import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

print(data)


# Output:
# [
#   {
#       "id":1,
#       "name":"Leanne Graham"
#   }
# ]


# ============================================================
# ACCESS SPECIFIC DATA
# ============================================================

import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

users = response.json()

print(users[0]["name"])


# Output:
# Leanne Graham


# ============================================================
# LOOP THROUGH API DATA
# ============================================================

import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

users = response.json()

for user in users:
    print(user["name"])


# Output:
# Leanne Graham
# Ervin Howell
# Clementine Bauch
# ...


# ============================================================
# SEND PARAMETERS
# ============================================================

import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1
}

response = requests.get(url, params=params)

print(response.json())


# Generated URL:
# https://jsonplaceholder.typicode.com/posts?userId=1


# ============================================================
# POST REQUEST
# ============================================================

import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Python",
    "body": "Learning APIs",
    "userId": 1
}

response = requests.post(url, json=payload)

print(response.json())


# POST is used to:
# - Create data
# - Submit forms
# - Send information to server


# ============================================================
# REQUEST HEADERS
# ============================================================

headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}

response = requests.get(url, headers=headers)


# Used for:
# - Authentication
# - API Keys
# - Security


# ============================================================
# ERROR HANDLING
# ============================================================

import requests

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    response.raise_for_status()

    data = response.json()

    print(data)

except requests.exceptions.RequestException as e:
    print("Error:", e)


# ============================================================
# COMMON REQUEST METHODS
# ============================================================

# GET    -> Retrieve data
# POST   -> Create data
# PUT    -> Update entire resource
# PATCH  -> Update partial resource
# DELETE -> Remove data


# ============================================================
# REAL-WORLD USE CASES
# ============================================================

# Weather Apps
# Stock Market Apps
# AI Applications
# Chatbots
# Payment Gateways
# Authentication Systems
# Social Media Integrations


# ============================================================
# INTERVIEW DEFINITION
# ============================================================

# An API request is a communication sent from a client
# to a server using HTTP methods such as GET, POST,
# PUT, PATCH, and DELETE to retrieve, send, update,
# or remove data.