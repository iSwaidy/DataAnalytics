# ====================================================== 
# Class Practice Exercise -- Data Analytics 
# Name:   Cris Ramirez 
# Date:    
# Course: Data Analytics 
# File:    
# Topic:  
# ======================================================

# scatter plot
# using dataFrame

import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame
data = pd.DataFrame({
    "hours_studied": [1, 2, 3, 4, 5, 6, 7],
    "exam_score":    [50, 55, 65, 70, 75, 85, 95]
})

# Figure size
plt.figure(figsize=(4, 2))

# Scatter plot
plt.scatter(
    data["hours_studied"],   # x-axis
    data["exam_score"],      # y-axis

    color="blue",            # point color
    s=100,                   # marker size (IMPORTANT: size, not markersize)
    marker="o",              # marker shape
    alpha=0.7,               # transparency
    edgecolors="black"       # border around points
)

# Title and labels
plt.title("Study Hours vs Exam Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")

# Grid
plt.grid(True)

plt.savefig("G:/Yu_Class 7/PythonFiles2026/Week7/scatter1.png")

# Show plot
plt.show()