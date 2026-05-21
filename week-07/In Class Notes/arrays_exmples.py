#Cris Ramirez

import numpy as np

# 1D array - one row, three values
arr_1d = np.array([1, 2, 3])

# 2D array - three rows, three columns
arr_2d = np.array([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
])

# 3D array - three 2D arrays stacked
arr_3d = np.array([
    [[1, 2, 3],
     [1, 2, 3],
     [1, 2, 3]],

    [[1, 2, 3],
     [1, 2, 3],
     [1, 2, 3]],

    [[1, 2, 3],
     [1, 2, 3],
     [1, 2, 3]]
])

print("1D Array:")
print(arr_1d)
print("\n2D Array:")
print(arr_2d)
print("\n3D Array:")
print(arr_3d)