# ====================================================== 
# Class Practice Exercise -- Data Analytics 
# Name:   Cris Ramirez 
# Date:    
# Course: Data Analytics 
# File:    
# Topic:  
# ======================================================

# Simple Line Graph
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create line plot
plt.plot(x, y, scalex=True, scaley=True)

# Add labels and title
plt.title("Simple Line Graph")
plt.xlabel("X values")
plt.ylabel("Y values")

# Display grid (optional but helpful)
plt.grid(True)

# Show the plot
plt.show()