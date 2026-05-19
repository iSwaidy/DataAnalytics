#Cris Ramirez

# A Pandas Series is a one-dimensional labeled array.
# It can be created from many data types—
# most commonly a Python list or a Python dictionary.

import pandas as pd

# Creating a Pandas Series from a Python List
data = [10, 20, 30, 40]

s = pd.Series(data)

print(s)