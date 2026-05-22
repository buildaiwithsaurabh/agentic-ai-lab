# RANDOM NUMBER IN PYTHON

# random module is used to generate random values

import random


# ==========================================
# RANDOM INTEGER
# ==========================================

# Generate random number between 1 and 10

number = random.randint(1, 10)

print("Random Integer:", number)



# ==========================================
# RANDOM FLOAT
# ==========================================

# Generate random float between 0 and 1

decimal = random.random()

print("Random Float:", decimal)



# ==========================================
# RANDOM CHOICE
# ==========================================

# Pick random item from list

fruits = ["apple", "banana", "orange"]

fruit = random.choice(fruits)

print("Random Fruit:", fruit)



# ==========================================
# RANDOM SHUFFLE
# ==========================================

# Shuffle list randomly

cards = ["A", "K", "Q", "J"]

random.shuffle(cards)

print("Shuffled Cards:", cards)



# ==========================================
# RANDOM RANGE WITH STEP
# ==========================================

# Random even number

even = random.randrange(0, 20, 2)

print("Random Even Number:", even)