# ====================================================== 
# Class Practice Exercise -- Data Analytics 
# Name:   Cris Ramirez 
# Date:    
# Course: Data Analytics 
# File:    
# Topic:  
# ======================================================

# styling a Pandas line plot using Matplotlib, including:

# marker size (markersize)
# marker color
# line color + style # fmt shorthand (format string)
# figure size (figsize)

import matplotlib.pyplot as plt
import pandas as pd

# DataFrame
sales = pd.DataFrame({
    "month": [1, 2, 3, 4, 5, 6],
    "qty_sold": [45, 34, 62, 55, 69, 72]
})

# Create figure size (width, height in inches)
plt.figure(figsize=(4, 2))

# Plot with styling
plt.plot(
    sales["month"],            # x-axis
    sales["qty_sold"],         # y-axis

    # marker styling
    marker="o",                # shape
    markersize=10,             # size of markers
    markerfacecolor="red",     # fill color
    markeredgecolor="black",   # border color

    # line styling
    linestyle="--",            # dashed line
    linewidth=2,               # thickness
    color="blue"               # line color
)

# Labels and title
plt.title("Monthly Sales Trend (Styled)")
plt.xlabel("Month")
plt.ylabel("Quantity Sold")

# Grid
plt.grid(True)

plt.savefig("G:/Yu_Class 7/PythonFiles2026/Week7/line_graph3.png")

# Show plot
plt.show()