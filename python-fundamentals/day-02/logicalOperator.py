# Logical Operator = Evaluate Multiple Conditions(OR , AND , NOT)
#                    OR = At least one condition must be True
#                    AND = Both conditions must be True
#                    NOT = inverts the condition(not False , not True)


""" OR Logical Operator"""
"""
temp = float(input("Enter the tempearture: "))

if temp > 35 or temp < 25:
      print(f"The temperature is {temp} and its hot weather")

"""

""" AND Logical Operator"""
"""
temp = float(input("Enter the tempearture: "))

is_sunny = input("Enter the weather: ")

if temp >= 28 and is_sunny:
      print("It is HOT outside 🥵")
      print("It is SUNNY 🌞")
elif temp <= 0 and is_sunny:
      print("It is COLD outside ❄")
      print("It is SUNNY 🌞")
"""



""" NOT Logical Operator """
"""
temp = float(input("Enter the temperature: "))

is_sunny = input("Is it sunny? (yes/no): ").lower() == "yes"

if temp >= 28 and is_sunny:
    print("It is HOT outside 🥵")
    print("It is SUNNY 🌞")

elif temp <= 0 and is_sunny:
    print("It is COLD outside ❄")
    print("It is SUNNY 🌞")

elif temp >= 28 and not is_sunny:
    print("It is HOT outside 🥵")
    print("It is CLOUDY ☁")
"""



# Conditional Expression = A One Line Shortcut for the if-else statement



# num = int(input("Enter the Number: "))

# print("Positive" if num > 0 else "Negative")

# print("Even" if num % 2 == 0 else "Odd")



a = 10
b = 20

print("A is greater" if a > b else "B is greater")







