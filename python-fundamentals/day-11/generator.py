# Generators in Python

def count_up_to(max_num):
    count = 1

    while count <= max_num:
        yield count
        count += 1


for number in count_up_to(5):
    print(number)