# Exercise 1 
# find Area of rectangle
 
""" 
length = float(input("Enter the length of the rectangle : "))
width = float(input("Enter the width of the rectangle : "))
area = length * width
print(f"The area of the rectangle is : {area}cm")
"""

# Exercise 2
# Shopping Cart Program

item1 = input("Enter the name of the first item : ")
price1 = float(input(f"Enter the price of {item1} : "))
quantity1 = int(input(f"Enter the quantity of {item1} : "))


print(f"You have added {quantity1} {item1}(s) to your cart at a price of {price1} each.")
total_price = price1 * quantity1
print(f"The total price for {quantity1} {item1}(s) is : {
total_price}")

