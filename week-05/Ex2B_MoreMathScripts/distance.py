## Cris Ramirez


import math

# Get the coordinates of the first point from the user
x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))

# Get the coordinates of the second point from the user
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))

# Calculate the distance between the two points using the distance formula
distance = math.hypot(x2 - x1, y2 - y1)

# Display the result
print(f"The distance between the two points is {distance:.2f}")