## Cris Ramirez
## 05/07/26
## In Class Practice

#Iterate with a for loop
my_set = {"alice", "bob", "charlie"}

for name in my_set:
    print(name)

#Membership testing
my_set = {1, 2, 3, 4, 5}

print(3 in my_set)  # Output: True
print(9 in my_set)  # Output: False

# Convert to list
my_set = {1, 2, 3, 4, 5}

my_list = list(my_set)
print(my_list[2])  # Output: 3

# Convert to a sorted list — access in a predictable order.
my_set = {1, 2, 3, 4, 5}

my_list = sorted(my_set)
print(my_list[2])

# Unpacking — assign elements to variables (order not guaranteed).
my_set = {1, 2, 3, 4, 5}

a, b, c, d, e = my_set
print(a, b, c, d, e)
