# ====================================================== 
# Class Practice Exercise -- Data Analytics 
# Name:   Cris Ramirez 
# Date:    
# Course: Data Analytics 
# File:    
# Topic:  
# ======================================================

import matplotlib.pyplot as plt
import pandas as pd

# Create DataFrame
sales = pd.DataFrame({
    "month": [1, 2, 3, 4, 5, 6],
    "qty_sold": [45, 34, 62, 55, 69, 72]
})

# Plot line graph with markers
plt.plot(
    sales["month"],
    sales["qty_sold"],
    marker="o"    # adds dots on each data point
)

# Title and labels
plt.title("Sales at 6 Months")
plt.xlabel("Month")
plt.ylabel("Quantity Sold")

# Save the graph BEFORE showing it
plt.savefig("G:/Yu_Class 7/PythonFiles2026/Week7/line_graph2.png")

# Show grid (optional but helpful)
plt.grid(True)

# Display plot
plt.show()