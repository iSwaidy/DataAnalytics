# ====================================================== 
# Class Practice Exercise -- Data Analytics 
# Name:   Cris Ramirez 
# Date:    
# Course: Data Analytics 
# File:    
# Topic:  
# ======================================================

import pandas as pd
import matplotlib.pyplot as plt


# Create DataFrame
data = pd.DataFrame({
    "exam_scores": [45, 55, 62, 70, 75, 80, 85, 90, 95, 60, 68, 73, 77, 88, 92]
})

# Figure size
plt.figure(figsize=(4, 2))

# Histogram
plt.hist(
    data["exam_scores"],   # data column
    bins=5,                # number of intervals (bars)
    color="skyblue",       # bar color
    edgecolor="black",     # border color
    alpha=0.8              # transparency
)

# Title and labels
plt.title("Distribution of Exam Scores")
plt.xlabel("Score Range")
plt.ylabel("Number of Students")

# Grid (y-axis only for readability)
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.savefig("histogram.png")

# Show plot
plt.show()