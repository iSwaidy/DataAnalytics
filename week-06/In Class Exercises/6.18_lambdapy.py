# Cris Ramirez
# demonstrates lambda functions

#  lambda arguments: expression
# contains any number of arguments but contains only one expression.

# Lambda function to double a number
doubler = lambda n: n * 2

print(doubler(5))


# Lambda function to add a number
add_numbers = lambda a, b: a + b

print(add_numbers(3, 7))


# Lambda function to determine largest number
largest = lambda x, y: x if x > y else y

print(largest(12, 8))