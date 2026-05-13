# Cris Ramirez
# Exploring the math module in Python

import math

# Sample values
numbers = [1.2, 2.5, 3.7, 4.1]
x = 16
y = -5.7
a = 10
b = 3

print("=== Python Math Module Demo ===\n")

# fsum() → accurate sum of iterable
print("fsum:", math.fsum(numbers))

# sqrt() → square root (returns float)
print("sqrt:", math.sqrt(x))

# isqrt() → integer square root (whole number)
print("isqrt:", math.isqrt(x))

# fabs() → absolute value (returns float)
print("fabs:", math.fabs(y))

# fmod() → remainder of division
print("fmod:", math.fmod(a, b))

# floor() → rounds DOWN to nearest integer
print("floor:", math.floor(y))

# ceil() → rounds UP to nearest integer
print("ceil:", math.ceil(y))

# trunc() → removes decimal part (no rounding)
print("trunc:", math.trunc(y))

# pi → mathematical constant π
print("pi:", math.pi)