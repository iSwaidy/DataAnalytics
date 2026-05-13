# Cris Ramirez
# Parsing a String

def parse_name(full_name):
    parts = full_name.split(" ")
    first_name = parts[0]
    last_name  = parts[-1]
    return first_name, last_name

# Call the function
first, last = parse_name('Alice Johnson')

# Display the results
print(f"First Name: {first}")
print(f"Last Name: {last}")