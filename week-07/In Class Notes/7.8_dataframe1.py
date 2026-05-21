#Cris Ramirez

# A DataFrame is a 2-dimensional table in Pandas made up of rows and columns.
# Each inner list becomes a row.

import pandas as pd

# Creating a DataFrame from a Python List
data = [
    ["Alice", 20],
    ["Bob", 22],
    ["Charlie", 21]
]

df = pd.DataFrame(data, columns=["Name", "Age"])

print(df)