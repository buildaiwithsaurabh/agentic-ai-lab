# Notes Manager

FILE_NAME = "notes.txt"


def add_note():
    note = input("Enter note: ")

    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")

    print("Note saved.")


def view_notes():
    try:
        with open(FILE_NAME, "r") as file:
            notes = file.read()

            if notes:
                print("\nNotes:")
                print(notes)
            else:
                print("No notes found.")

    except FileNotFoundError:
        print("No notes found.")


def main():

    while True:

        print("\n=== Notes Manager ===")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_note()

        elif choice == "2":
            view_notes()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()