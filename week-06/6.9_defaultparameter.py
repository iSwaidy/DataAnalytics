# Use a default parameter city = New York


def greeting(name, hobby, city="New York"):
    return f"Hello, {name}! You are from {city} and you enjoy {hobby}."

result = greeting(
    name=input("Please enter your name: "),
    hobby=input("Please enter your hobby: ")
)

print(result)