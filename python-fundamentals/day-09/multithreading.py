# MULTITHREADING IN PYTHON

# Definition:
# Multithreading is a technique that allows a program
# to run multiple threads (smaller units of a process)
# concurrently within the same process.

# A thread is a lightweight unit of execution.

# Multithreading is useful for:
# - I/O operations
# - File handling
# - Network requests
# - Waiting tasks
# - Background operations

# It improves responsiveness and efficiency.


# ============================================================
# REAL-WORLD EXAMPLE
# ============================================================

# Without Multithreading:

# Task 1 starts
# Task 1 finishes
# Task 2 starts
# Task 2 finishes

# Tasks run one after another.


# With Multithreading:

# Task 1 starts
# Task 2 starts
# Both run concurrently

# Better utilization of waiting time.


# ============================================================
# BASIC SYNTAX
# ============================================================

import threading


def task():
    print("Task is running")


thread = threading.Thread(target=task)

thread.start()

thread.join()   # Wait until thread finishes

print("Program completed")


# ============================================================
# EXAMPLE 1
# ============================================================

import threading
import time


def walk_dog():
    time.sleep(3)
    print("Dog walk completed")


def take_out_trash():
    time.sleep(2)
    print("Trash removed")


t1 = threading.Thread(target=walk_dog)
t2 = threading.Thread(target=take_out_trash)

t1.start()
t2.start()

t1.join()
t2.join()

print("All chores completed")


# ============================================================
# IMPORTANT METHODS
# ============================================================

# start()
# Starts a thread

# join()
# Waits for thread completion

# current_thread()
# Returns current thread information

# active_count()
# Returns active thread count


# Example:

import threading

print(threading.active_count())
print(threading.current_thread())


# ============================================================
# BENEFITS OF MULTITHREADING
# ============================================================

# 1. Faster execution of I/O-bound tasks
# 2. Better application responsiveness
# 3. Concurrent task handling
# 4. Background processing
# 5. Improved user experience


# ============================================================
# LIMITATIONS
# ============================================================

# Python has a GIL (Global Interpreter Lock)

# Because of the GIL:
# - Only one thread executes Python bytecode at a time
# - Multithreading is NOT ideal for CPU-heavy calculations

# Good For:
# - Network requests
# - APIs
# - Database operations
# - File I/O

# Not Ideal For:
# - Heavy mathematical computations
# - CPU-intensive processing


# ============================================================
# DIFFERENCE BETWEEN PROCESS & THREAD
# ============================================================

# Process:
# - Independent program
# - Separate memory
# - More resources

# Thread:
# - Part of a process
# - Shared memory
# - Lightweight


# ============================================================
# SIMPLE INTERVIEW DEFINITION
# ============================================================

# Multithreading is a programming technique that
# allows multiple threads to execute concurrently
# within the same process, improving responsiveness
# and efficiency, especially for I/O-bound tasks.