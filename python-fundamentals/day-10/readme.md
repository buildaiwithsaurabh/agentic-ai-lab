# ASYNCHRONOUS PROGRAMMING (ASYNC PROGRAMMING) IN PYTHON

# Definition:
# Asynchronous Programming is a programming technique
# that allows a program to perform multiple tasks
# concurrently without waiting for one task to finish
# before starting another.

# It is especially useful for:
# - API requests
# - Database operations
# - File I/O
# - Network communication
# - Web scraping

# Async programming improves efficiency by allowing
# the program to work on other tasks while waiting.


# ============================================================
# SYNCHRONOUS VS ASYNCHRONOUS
# ============================================================

# Synchronous:
#
# Task 1 ---> Complete
# Task 2 ---> Complete
# Task 3 ---> Complete
#
# Tasks execute one after another.


# Asynchronous:
#
# Task 1 ---> Waiting
# Task 2 ---> Running
# Task 3 ---> Running
#
# Tasks can progress concurrently.


# ============================================================
# KEY KEYWORDS
# ============================================================

# async
# Defines an asynchronous function.

# await
# Pauses execution until an async task completes.

# asyncio
# Built-in Python module for async programming.


# ============================================================
# BASIC EXAMPLE
# ============================================================

import asyncio

async def hello():
    print("Hello")
    await asyncio.sleep(2)
    print("World")

asyncio.run(hello())


# Output:
#
# Hello
# (wait 2 seconds)
# World


# ============================================================
# MULTIPLE TASKS
# ============================================================

import asyncio

async def task1():
    await asyncio.sleep(2)
    print("Task 1 Complete")

async def task2():
    await asyncio.sleep(1)
    print("Task 2 Complete")

async def main():
    await asyncio.gather(
        task1(),
        task2()
    )

asyncio.run(main())


# Output:
#
# Task 2 Complete
# Task 1 Complete


# Both tasks run concurrently.


# ============================================================
# ASYNC API REQUESTS
# ============================================================

# Requires:
# pip install aiohttp

import aiohttp
import asyncio

async def fetch_data():

    url = "https://jsonplaceholder.typicode.com/users"

    async with aiohttp.ClientSession() as session:

        async with session.get(url) as response:

            data = await response.json()

            print(data[0]["name"])

asyncio.run(fetch_data())


# ============================================================
# ASYNC VS MULTITHREADING
# ============================================================

# Multithreading:
# - Multiple threads
# - Good for I/O tasks
# - Uses threading module

# Async Programming:
# - Single thread
# - Event loop based
# - Efficient for many waiting tasks


# ============================================================
# EVENT LOOP
# ============================================================

# Definition:
# The event loop is the engine that manages
# asynchronous tasks and decides when each task runs.

# Example:

import asyncio

async def work():
    print("Working...")
    await asyncio.sleep(1)
    print("Done")

asyncio.run(work())


# asyncio.run() starts the event loop.


# ============================================================
# BENEFITS OF ASYNC PROGRAMMING
# ============================================================

# 1. Faster I/O operations
# 2. Better performance
# 3. Handles thousands of requests
# 4. Ideal for APIs and web applications
# 5. Efficient resource usage


# ============================================================
# REAL-WORLD USE CASES
# ============================================================

# FastAPI
# Web Scraping
# Chat Applications
# Real-Time Systems
# AI Agents
# API Aggregators
# Streaming Applications


# ============================================================
# INTERVIEW DEFINITION
# ============================================================

# Asynchronous Programming is a programming model
# that allows multiple tasks to execute concurrently
# by using an event loop, enabling efficient handling
# of I/O-bound operations without blocking program execution.