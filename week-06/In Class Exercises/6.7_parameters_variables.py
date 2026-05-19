# Cris Ramirez
# Multiple parameters
# Python automatically packages multiple return values into a tuple

def greeting(name, city, hobby):
    return name, city, hobby

name, city, hobby = greeting(
    input("Please enter your name: "),
    input("Please enter your city: "),
    input("Please enter your hobby: ")
)


print(f"Hello, {name}! You are from {city} and you enjoy {hobby}.")