# FUNCTION-BASED PROGRAMS IN PYTHON


# ==========================================
# 1. ADDITION CALCULATOR
# ==========================================

def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)

print("Sum:", result)



# ==========================================
# 2. EVEN OR ODD CHECKER
# ==========================================

def check_even_odd(number):

    if number % 2 == 0:
        return "Even"

    else:
        return "Odd"

print(check_even_odd(7))



# ==========================================
# 3. STUDENT GRADE SYSTEM
# ==========================================

def calculate_grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 75:
        return "B"

    elif marks >= 50:
        return "C"

    else:
        return "Fail"

print("Grade:", calculate_grade(82))



# ==========================================
# 4. FACTORIAL PROGRAM
# ==========================================

def factorial(num):

    result = 1

    for i in range(1, num + 1):
        result *= i

    return result

print("Factorial:", factorial(5))



# ==========================================
# 5. TEMPERATURE CONVERTER
# ==========================================

def celsius_to_fahrenheit(temp):

    return (temp * 9/5) + 32

print("Temperature:", celsius_to_fahrenheit(30), "F")



# ==========================================
# 6. LOGIN SYSTEM
# ==========================================

def login(username, password):

    if username == "admin" and password == "1234":
        return "Login Successful"

    else:
        return "Invalid Credentials"

print(login("admin", "1234"))



# ==========================================
# 7. MULTIPLICATION TABLE
# ==========================================

def multiplication_table(number):

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

multiplication_table(5)



# ==========================================
# 8. SIMPLE BANK BALANCE CHECK
# ==========================================

def check_balance(balance):
    return f"Your Balance is ₹{balance}"

print(check_balance(5000))



# ==========================================
# 9. MAXIMUM NUMBER FINDER
# ==========================================

def find_max(a, b, c):

    return max(a, b, c)

print("Largest Number:", find_max(10, 50, 25))



# ==========================================
# 10. VOWEL CHECKER
# ==========================================

def is_vowel(char):

    vowels = "aeiou"

    if char.lower() in vowels:
        return "Vowel"

    else:
        return "Not a Vowel"

print(is_vowel("A"))