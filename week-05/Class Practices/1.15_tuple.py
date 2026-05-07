## Cris Ramirez
## 05/07/26
## In Class Practice

#index
t = ("a", "b", "c")
print(t[0])  # Output: a
print(t[-1])  # Output: b

# slice

t = (1, 2, 3, 4, 5)
t_slice = t[1:4]
print(t_slice)  # Output: (2, 3, 4)

# concatenation
t1 = (1, 2, 3)
t2 = ('a', 'b', 'c')
t3 = t + t2
print(t3)  # Output: (1, 2, 3, 'a

#repitition
t = (1, 2, 3)
t2 = t * 3
print(t2)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

#membership
t = (1, 2, 3)
print(2 in t)  # Output: True

#uniqueness
t = (1, 2, 3, 4, 5)
print(len(set(t)))  # Output: 5

# convert to list
t = (1, 2, 3, 4, 5)
print(list(t))  # Output: [1, 2, 3, 4, 5]