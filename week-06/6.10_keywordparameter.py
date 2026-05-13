# Cris Ramirez
# default parameters are also called keyword parameters
# make the argument optional at call time

def greeting(name="Unknown", hobby="nothing", city="New York"):
    return f"Hello, {name}! You are from {city} and you enjoy {hobby}."


# Call 1 - all defaults used, no arguments passed
result1 = greeting()
print(result1)

# Call 2 - name only provided, city and hobby use defaults
result2 = greeting(name="Alice")
print(result2)

# Call 3 - all three arguments provided, all defaults overridden
result3 = greeting(name="Alice", hobby="hiking", city="Brooklyn")
print(result3)

# Call 4 - using input() to let the user supply all three values
result4 = greeting(
    name=input("Please enter your name: "),
    hobby=input("Please enter your hobby: "),
    city=input("Please enter your city: ")
)
print(result4)