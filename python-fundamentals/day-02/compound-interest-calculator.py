# COMPOUND INTEREST CALCULATOR

# Formula:
# A = P(1 + r/n)^(nt)

# A = Final amount
# P = Principal amount
# r = Interest rate
# n = Number of times interest compounded per year
# t = Time in years


principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (%): ")) / 100
time = float(input("Enter the time (years): "))
n = int(input("Enter number of times compounded per year: "))

amount = principal * (1 + rate / n) ** (n * time)

print(f"Final Amount: ₹ {amount:.2f}")