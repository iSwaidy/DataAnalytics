# Cris Ramirez

# 5/16/2026
# Indexing a DataFrame

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [20, 22, 21, 23],
    "Math": [85, 78, 92, 80]
}

df = pd.DataFrame(data)

print(df)

# Label-Based Indexing (iloc())
# iloc[] uses row labels and column names
# Select a Row
print()

print(df.loc[1])

print()

# Select a Specific Value
print(df.loc[2, "Name"])
print()