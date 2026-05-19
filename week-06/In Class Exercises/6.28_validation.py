# Cris Ramirez
# Error Handling

while True:
    try:
        number = int(input("Enter a positive number: "))
        if number > 0:
            break
        else:
            print("Number must be positive.")
    except ValueError:
        print("Invalid input. Please enter a number.")

print("Valid number received:", number)