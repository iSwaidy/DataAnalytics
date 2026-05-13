# Cris Ramirez
# Multiple parameters
# Python automatically packages multiple return values into a tuple

def greeting(name, city, hobby): # This defines a function named 'greeting' that takes three parameters: 'name', 'city', and 'hobby'
    return name, city, hobby # This will return the values of 'name', 'city', and 'hobby' as a tuple

result = greeting(
    input("Please enter your name: "),
    input("Please enter your city: "),
    input("Please enter your hobby: ")
)

print(type(result))

print(f"Hello, {result[0]}! You are from {result[1]} and you enjoy {result[2]}.")