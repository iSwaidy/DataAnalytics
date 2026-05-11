## Cris Ramirez


# Get user input for temperature in Fahrenheit
celsius = float(input("Enter the temperature in Celsius: "))
# Convert the temperature to Fahrenheit using the formula: F = (C * 9/5) + 32
fahrenheit = (celsius * 9 / 5) + 32
# Display the result
print(f"{celsius} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit.")