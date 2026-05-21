# if = this is a conditional statement that executes a block of code if a specified condition is true

# if statement syntax:
# if condition:
#     block of code to be executed if the condition is true
# example 1:
age = int(input("Enter your age : "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# example 2:
response = input("would you like to food ? (yes/no) : ")       
if response == "yes":
    print("You will get the food.")
else:
    print("You will not get the food.")
