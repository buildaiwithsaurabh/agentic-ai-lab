# *args = allows you to pass multiple non-key arguments
# ** kwargs = allows you to pass multiple keyword arguments
# * unpacking operator

"""
def add(*args):
  total = 0;
  for arg in args:
    total += arg
  return total


print(add(1 , 2 , 6))


def display_name(*args):
  for arg in args:
    print(arg, end=" ")

display_name("Aanya" , "Bro code" , "Saurabh")



def print_address(**kwargs):
  for key, value in kwargs.items():
    print(f"{key} : {value}")


print_address(street="laxmi chuaraha",
              city = "prayagraj",
              state="UP",
              zip="211001"
              )

# kwargs methods cheat sheet


"""


def demo(**kwargs):

    # 1. Get all kwargs (dictionary)
    print(kwargs)

    # 2. Get all keys
    print(kwargs.keys())

    # 3. Get all values
    print(kwargs.values())

    # 4. Get key-value pairs
    print(kwargs.items())

    # 5. Access value using key
    print(kwargs["name"])

    # 6. Safe access
    print(kwargs.get("age"))

    # 7. Check key exists
    print("city" in kwargs)

    # 8. Loop through keys
    for key in kwargs.keys():
        print(key)

    # 9. Loop through values
    for value in kwargs.values():
        print(value)

    # 10. Loop through key-value pairs
    for key, value in kwargs.items():
        print(f"{key} : {value}")


demo(
    name="Bro Code",
    age=22,
    city="Prayagraj"
)