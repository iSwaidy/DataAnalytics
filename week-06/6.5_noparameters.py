def greeting(): # This defines a function named 'greeting' that takes no parameters
    name = input("What is your name? ")
    return name # This will return the name entered by the user
result = greeting()    # This will call the greeting function and store the returned name in the variable 'result'
print(f'Hello, {result}!') # This will print a greeting message that includes the name entered by the user