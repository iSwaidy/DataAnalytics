# Cris Ramirez
# DataFrame Operations
# Insert a column using .insert()

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "SQL": [85, 78, 92]
}

df = pd.DataFrame(data)

print(df)

print()
# Insert a column
df.insert(1, "Java", [80, 85, 90])

print(df)