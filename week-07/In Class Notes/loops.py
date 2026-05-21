# Cris Ramirez

import numpy as np

# 1. Create 2D array and print it
arrA = np.array([[11, 12, 13],
                 [14, 15, 16]])
print(arrA)

print('--' * 20)

# 2. Loop first dimension, print each element * 2
for x in arrA:
    print(x * 2)
    
print('--' * 20)

# 3 & 4. Loop second dimension, assign x*2 to loop_result and print it
for x in arrA:
    for y in x:
        loop_result = x * 2
        print(loop_result)