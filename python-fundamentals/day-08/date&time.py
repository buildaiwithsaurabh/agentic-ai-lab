# Date and Time in Python

# Python provides the datetime module
# to work with dates and times.

import datetime


# Example 1: Current Date and Time

current = datetime.datetime.now()

print("Current Date and Time:", current)


# Output:
# Current Date and Time: 2026-05-28 10:30:45.123456



# Example 2: Current Date Only

today = datetime.date.today()

print("Today's Date:", today)


# Output:
# Today's Date: 2026-05-28



# Example 3: Current Time Only

time = datetime.datetime.now().time()

print("Current Time:", time)


# Output:
# Current Time: 10:30:45.123456



# Example 4: Creating Custom Date

date = datetime.date(2026, 5, 28)

print("Custom Date:", date)


# Output:
# Custom Date: 2026-05-28



# Example 5: Formatting Date and Time

current = datetime.datetime.now()

formatted = current.strftime("%d-%m-%Y %H:%M:%S")

print("Formatted Date and Time:", formatted)


# Output:
# Formatted Date and Time: 28-05-2026 10:30:45



# Example 6: Getting Individual Values

current = datetime.datetime.now()

print("Year:", current.year)
print("Month:", current.month)
print("Day:", current.day)
print("Hour:", current.hour)
print("Minute:", current.minute)
print("Second:", current.second)


# Example Output:
# Year: 2026
# Month: 5
# Day: 28
# Hour: 10
# Minute: 30
# Second: 45