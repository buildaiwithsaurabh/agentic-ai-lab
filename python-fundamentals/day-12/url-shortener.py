# URL Shortener Simulation

import random
import string

url_database = {}


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits

    short_code = ""

    for _ in range(length):
        short_code += random.choice(characters)

    return short_code


def shorten_url():

    original_url = input("Enter URL: ")

    short_code = generate_short_code()

    while short_code in url_database:
        short_code = generate_short_code()

    url_database[short_code] = original_url

    print(f"\nShort URL: https://short.ly/{short_code}")


def retrieve_url():

    short_code = input("Enter short code: ")

    if short_code in url_database:
        print(f"Original URL: {url_database[short_code]}")
    else:
        print("URL not found")


def view_database():

    if not url_database:
        print("No URLs stored")
        return

    print("\nStored URLs")

    for code, url in url_database.items():
        print(f"{code} -> {url}")


def main():

    while True:

        print("\n===== URL SHORTENER =====")
        print("1. Shorten URL")
        print("2. Retrieve URL")
        print("3. View All URLs")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            shorten_url()

        elif choice == "2":
            retrieve_url()

        elif choice == "3":
            view_database()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()