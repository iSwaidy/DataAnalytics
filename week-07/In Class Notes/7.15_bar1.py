# ====================================================== 
# Class Practice Exercise -- Data Analytics 
# Name:   Cris Ramirez 
# Date:    
# Course: Data Analytics 
# File:    
# Topic:  
# ======================================================

# 5/16/2026

# bar chart
# using dataFrame

import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame
sales = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr"],
    "qty_sold": [45, 34, 62, 55]
})

# Figure size
plt.figure(figsize=(5, 3))

# Bar chart using plt.bar()
plt.bar(
    sales["month"],         # x-axis (categories)
    sales["qty_sold"],      # y-axis (values)

    color="skyblue",        # bar color
    edgecolor="black",      # border color
    width=0.6               # bar width
)

# Title and labels
plt.title("Monthly Sales (Bar Chart)")
plt.xlabel("Month")
plt.ylabel("Quantity Sold")

# Grid (y-axis only for clarity)
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.savefig("G:/Yu_Class 7/PythonFiles2026/Week7/bar_graph1.png")

# Show plot
plt.show()