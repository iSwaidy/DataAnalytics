# Cris Ramirez
# Generating a Sample DataFrame Using NumPy

import numpy as np
import pandas as pd

# Generate a range of numbers with .arange()
data = np.arange(1, 13)
print(data)

# Reshape Data into Rows and Columns
data = data.reshape(3, 4)

print(data)

# Convert to a Pandas DataFrame
df = pd.DataFrame(data)

print(df)

# Adding Column Names
df = pd.DataFrame(
    data.reshape(3, 4),
    columns=["A", "B", "C", "D"]
)

print(df)