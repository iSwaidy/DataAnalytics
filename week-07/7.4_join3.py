import numpy as np

arrA = np.array([
    [1, 2],
    [3, 4]
])

arrB = np.array([
    [5, 6],
    [7, 8]
])

# join horizontally (column-wise)
result2 = np.concatenate((arrA, arrB), axis=1)
print(result2)