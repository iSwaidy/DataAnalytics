# Description: This script tests various numeric
# conversion techniques
# Author: Cris Ramirez

a = "  101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

''' a) Cast as integer using int() '''
# print(int(a))         # ValueError: invalid literal for int() with base 10: '  101.1 '
print(int(b))           # works → 55
# print(int(c))         # ValueError: invalid literal for int() with base 10: '402 Stevens'
# print(int(d))         # ValueError: invalid literal for int() with base 10: 'Number 5  '

''' b) Cast as float using float() ''' 
print(float(a))        # works → 101.1 (float() handles surrounding whitespace fine)
print(float(b))        # works → 55.0
# print(float(c))      # ValueError: could not convert string to float: '402 Stevens'
# print(float(d))      # ValueError: could not convert string to float: 'Number 5  '

''' c) For variable a, try casting into a float then integer, like this: int(float(a)) ''' 
print(int(float(a)))   # works → 101 (drops the decimal)

''' d) Use slicing to add just the numeric portion of the string to a new variable ''' 
a_num = int(a[2:5])
b_num = int(b)
c_num = int(c[0:3])
d_num = int(d[7])

print(a_num)
print(b_num)
print(c_num)
print(d_num)

''' e) For variables a and d, use the .strip() method to remove the leading/trailingspaces, within a print statement to display each result. ''' 

print(a.strip())         # "101.1"
print(d.strip())         # "Number 5"