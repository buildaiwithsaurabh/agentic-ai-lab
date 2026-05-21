# format specifiers = {value:flags} format a value based on what flags are inserted 

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ₹ {price1:.2f}")
print(f"Price 1 is ₹ {price2:.1f}")
print(f"Price 1 is ₹ {price3:.1f}")

# FORMAT SPECIFIERS IN PYTHON

# .(number)f = round to that many decimal places (fixed point)

# :(number) = allocate that many spaces

# :03 = allocate and zero-pad that many spaces

# :< = left justify

# :> = right justify

# :^ = center align

# :+ = use a plus sign to indicate positive value

# := = place sign to leftmost position

# : = insert a space before positive numbers

# :, = comma separator



# EXAMPLES

price = 12345.6789
num = 7
name = "Python"


# .2f -> round to 2 decimal places
print(f"{price:.2f}")        # 12345.68


# 10 -> allocate 10 spaces
print(f"{num:10}")           #         7


# 03 -> zero padding
print(f"{num:03}")           # 007


# < -> left justify
print(f"{name:<10}")         # Python


# > -> right justify
print(f"{name:>10}")         #     Python


# ^ -> center align
print(f"{name:^10}")         #   Python


# + -> show positive sign
print(f"{num:+}")            # +7


# = -> sign at leftmost position
print(f"{-num:=5}")          # -   7


# space before positive number
print(f"{num: }")            #  7


# comma separator
print(f"{price:,.2f}")       # 12,345.68