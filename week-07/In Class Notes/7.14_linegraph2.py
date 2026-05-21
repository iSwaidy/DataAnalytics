# ====================================================== 
# Class Practice Exercise -- Data Analytics 
# Name:   Cris Ramirez 
# Date:    
# Course: Data Analytics 
# File:    
# Topic:  # Simple Line Graph
# Use the plt.savefig() to save line graph
# ======================================================

import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create line graph
plt.plot(x, y, scalex=True, scaley=True)

# Add labels and title
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Save the graph BEFORE showing it
# plt.savefig("line_graph.png")
plt.savefig("G:/Yu_Class 7/PythonFiles2026/Week7/line_graph.png")

# Display the graph
plt.show()