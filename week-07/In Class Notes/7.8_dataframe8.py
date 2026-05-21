# Cris Ramirez

# Position-Based Indexing (iloc[])
# iloc[] uses row and column positions (0-based indexing)

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [20, 22, 21, 23],
    "Java": [85, 78, 92, 80]
}

df = pd.DataFrame(data)

# Select a Row
print(df.iloc[1])

print()
# Select a Specific Value
print(df.iloc[2, 0])

print()
# Select Multiple Rows and Columns
print(df.iloc[1:3, 0:2])

# Select One Column
print()
print(df["Name"])

print()
# Select Multiple Columns

print(df[["Name", "Java"]])