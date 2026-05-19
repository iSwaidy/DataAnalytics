# Cris Ramirez

import numpy as np

arr3d = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

# Loop through layers
for layer in arr3d:
    print("Layer:")
    print(layer)