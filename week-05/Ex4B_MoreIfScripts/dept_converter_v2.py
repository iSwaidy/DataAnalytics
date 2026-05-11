# Cris Ramirez

# Get the department code from the user
dept_code = int(input("Enter a department code: "))

# Use a match statement to determine the department name based on the code
match dept_code:
    case 1:
        dept_name = "Marketing"
    case 5:
        dept_name = "Human Resources"
    case 10:
        dept_name = "Accounting"
    case 12:
        dept_name = "Legal"
    case 18:
        dept_name = "IT"
    case 20:
        dept_name = "Customer Relations"
    case _:
        dept_name = "Unknown"

# Print the department name
print(f"Department {dept_code}: {dept_name}")