#Cris Ramirez

import numpy as np

# Create a 2D NumPy array
a = np.array([[10, 20, 30],
              [40, 50, 60]])

print("Array:")
print(a)

# .shape → dimensions (rows, columns)
print("\nShape of array:", a.shape)

# .ndim → number of dimensions
print("Number of dimensions (ndim):", a.ndim)

# .dtype → data type of elements
print("Data type (dtype):", a.dtype)