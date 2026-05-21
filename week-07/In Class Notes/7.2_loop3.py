# Cris Ramirez

# Loop thru the elements in 2D

import numpy as np

arr2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# First loop → gets rows
# Second loop → gets elements inside each row

for row in arr2d:
    for value in row:
        print(value)