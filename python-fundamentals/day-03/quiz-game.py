# QUIZ GAME IN PYTHON

score = 0

print("Welcome to the Python Quiz Game!")
print()


# Question 1
answer = input("1. What is the capital of India? ")

if answer.lower() == "delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong!")


print()


# Question 2
answer = input("2. Which language is used for AI and Machine Learning? ")

if answer.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong!")


print()


# Question 3
answer = input("3. How many days are there in a week? ")

if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong!")


print()


# Question 4
answer = input("4. What keyword is used to create a function in Python? ")

if answer.lower() == "def":
    print("Correct!")
    score += 1
else:
    print("Wrong!")


print()


# Final Score
print("Quiz Completed!")
print(f"Your Score: {score}/4")


# Result
if score == 4:
    print("Excellent!")
elif score >= 2:
    print("Good Job!")
else:
    print("Keep Practicing!")