name = "Hello"

print(f"Original string : {name}")
print(f"First character : {name[0]}")
name[0] = "J"

name = "Hello"

print(f"Original string : {name}")
print(f"First character : {name[0]}")
name[0] = "J"

string = "Hello, World!"

# Accessing the first character
print(string[0])   # Output: H

# Accessing the last character using negative indexing
print(string[-1])  # Output: !

# Slicing from index 1 to 4 (excluding 4)
print(string[1:4])  # Output: ell