import pandas as pd
import numpy as np

# Create Series with values: 10, 20, 30, 20, NaN
s = pd.Series([10, 20, 30, 20, np.nan])

print("Original Series:")
print(s)

# Sum - adds all non-NaN values
print("\nSum:", s.sum())

# Mean - average of all non-NaN values
print("Mean:", s.mean())

# Max - highest value in Series
print("Max:", s.max())

# Min - lowest value in Series
print("Min:", s.min())

# Head(3) - displays first 3 values with index
print("\nFirst 3 values:")
print(s.head(3))

# isnull() - identifies missing values (returns True/False)
print("\nisnull():")
print(s.isnull())

# fillna(0) - replaces NaN with 0
print("\nAfter fillna(0):")
print(s.fillna(0))

# sort_values() - sorts in ascending order
print("\nSorted values:")
print(s.sort_values())

# value_counts() - counts repeated values (ignores NaN)
print("\nvalue_counts():")
print(s.value_counts())