# CONCESSION STAND PROGRAM

# Menu
menu = {
    "Pizza": 120,
    "Burger": 80,
    "Fries": 60,
    "Cold Drink": 40
}

cart = []
total = 0

print("------ MENU ------")

for key, value in menu.items():
    print(f"{key:12} : ₹{value}")

print("------------------")


while True:

    food = input("Enter item to buy (q to quit): ")

    if food.lower() == "q":
        break

    elif menu.get(food) is not None:
        cart.append(food)

    else:
        print("Item not available!")


print()
print("------ YOUR ORDER ------")

for food in cart:
    total += menu.get(food)
    print(food)

print()

print(f"Total Amount: ₹{total}")