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

# 5. empty() - uninitialized values (random memory content)
e = np.empty((2, 2))
print("np.empty((2,2))")
print(e, "\n")

# 6. arange() - sequence with step
f = np.arange(0, 10, 2)
print("np.arange(0,10,2)")
print(f, "\n")

# 7. linspace() - evenly spaced values
g = np.linspace(0, 1, 5)
print("np.linspace(0,1,5)")
print(g, "\n")

print("=== End of Demo ===")