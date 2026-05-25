# match-case in Python
# Available from Python 3.10+

# Syntax:
#
# match variable:
#     case value:
#         code
#     case _:
#         default code


# 1. Basic Example
day = 2

match day:
    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case _:
        print("Invalid Day")


# 2. String Example
command = "start"

match command:
    case "start":
        print("System Started")

    case "stop":
        print("System Stopped")

    case "restart":
        print("System Restarted")

    case _:
        print("Unknown Command")


# 3. Multiple Values in One Case
letter = "a"

match letter:
    case "a" | "e" | "i" | "o" | "u":
        print("Vowel")

    case _:
        print("Consonant")


# 4. Match with Conditions
num = 10

match num:
    case x if x > 0:
        print("Positive Number")

    case x if x < 0:
        print("Negative Number")

    case _:
        print("Zero")


# 5. List Pattern Matching
data = [1, 2]

match data:
    case [x, y]:
        print(f"x = {x}, y = {y}")

    case _:
        print("No Match")


# 6. Dictionary Pattern Matching
student = {
    "name": "Aman",
    "age": 22
}

match student:
    case {"name": name, "age": age}:
        print(f"Name: {name}, Age: {age}")

    case _:
        print("No Match")


# 7. Default Case
value = 100

match value:
    case 1:
        print("One")

    case 2:
        print("Two")

    case _:
        print("Default Case")