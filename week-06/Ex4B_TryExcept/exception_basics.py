# Cris Ramirez
# Exercise 4.B Lab 1 - Exception Handling

# ValueError
try:
    int('hello')
except ValueError:
    print("ValueError: Cannot convert 'hello' to an integer")
else:
    print("No error occurred")
finally:
    print("Let's try another one...")

# NameError
try:
    m = banana
except NameError:
    print("NameError: 'banana' is not defined")
else:
    print(m)
finally:
    print("Let's try another one...")

# TypeError
try:
    result = 'hello' + 5
except TypeError:
    print("TypeError: Cannot add a string and an integer")
else:
    print(result)
finally:
    print("Let's try another one...")

# SyntaxError - using eval() to catch at runtime
try:
    eval('x === 5')
except SyntaxError:
    print("SyntaxError: Invalid syntax detected")
else:
    print("No error occurred")
finally:
    print("Let's try another one...")