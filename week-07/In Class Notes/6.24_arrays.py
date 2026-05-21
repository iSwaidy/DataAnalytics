# Arrays

import numpy as np

print("=== NumPy Array Creation Functions ===\n")

# 1. array() - create from Python list
a = np.array([1, 2, 3, 4, 5])
print("np.array([1,2,3,4,5])")
print(a, "\n")

# 2. zeros() - array of zeros
b = np.zeros((2, 3))
print("np.zeros((2,3))")
print(b, "\n")

# 3. ones() - array of ones
c = np.ones((2, 2))
print("np.ones((2,2))")
print(c, "\n")

# 4. full() - array filled with a constant value
d = np.full((3, 2), 7)
print("np.full((3,2), 7)")
print(d, "\n")