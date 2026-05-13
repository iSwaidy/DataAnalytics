# Cris Ramirez
# Multiple parameters
# return a single formatted string instead:


def greeting(name, city, hobby):
    return f"Hello, {name}! You are from {city} and you enjoy {hobby}."

result = greeting(
    input("Please enter your name: "),
    input("Please enter your city: "),
    input("Please enter your hobby: ")
)

print(result)