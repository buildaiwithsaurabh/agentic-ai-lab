# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

name = input("Enter the username: ")

if len(name) > 12:
    print("Username must not exceed 12 characters")

elif  name.find(" ") != -1:
    print("Username must not contain spaces")

elif not name.isalpha():
    print("Username must not contain digits")

else:
    print("Username is valid")