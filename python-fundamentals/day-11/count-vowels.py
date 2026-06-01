# Count Vowels

text = input("Enter a string: ").lower()

count = 0

for char in text:
    if char in "aeiou":
        count += 1

print(f"Total vowels: {count}")