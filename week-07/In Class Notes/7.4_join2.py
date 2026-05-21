# Joining 2 2D array with axis = 0

import numpy as np

arrA = np.array([
    [1, 2],
    [3, 4]
])

arrB = np.array([
    [5, 6],
    [7, 8]
])

# join vertically (row-wise)
result1 = np.concatenate((arrA, arrB), axis=0)
print(result1)