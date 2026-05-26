# Encrypt and Decrypt Program
# Simple Substitution Cipher

import random
import string


# All possible characters
chars = " " + string.punctuation + string.digits + string.ascii_letters

# Convert to list
chars = list(chars)

# Create encryption key
key = chars.copy()

# Shuffle key
random.shuffle(key)


# Display mapping
print("===== ENCRYPTION KEY =====")

for i in range(len(chars)):
    print(f"{chars[i]} -> {key[i]}")

print("==========================\n")


# Menu
while True:

    print("\n===== MENU =====")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    # ENCRYPT
    if choice == '1':

        plain_text = input("Enter message to encrypt: ")
        cipher_text = ""

        for letter in plain_text:

            if letter in chars:
                index = chars.index(letter)
                cipher_text += key[index]
            else:
                cipher_text += letter

        print(f"\nOriginal Message : {plain_text}")
        print(f"Encrypted Message: {cipher_text}")


    # DECRYPT
    elif choice == '2':

        cipher_text = input("Enter message to decrypt: ")
        plain_text = ""

        for letter in cipher_text:

            if letter in key:
                index = key.index(letter)
                plain_text += chars[index]
            else:
                plain_text += letter

        print(f"\nEncrypted Message: {cipher_text}")
        print(f"Original Message : {plain_text}")


    # EXIT
    elif choice == '3':

        print("Exiting program...")
        break


    # INVALID INPUT
    else:
        print("Invalid choice. Please try again.")