## Cris Ramirez


bill = input("What was your bill amount? $")
tip_percent = input("What tip percent would you like to leave? ")

# input() returns a string, so we need to convert to float for math
bill = float(bill)
tip_percent = float(tip_percent)

tip = bill * tip_percent

print(f"The tip on a ${bill} restaurant bill is ${tip:.2f}")

# Pitfalls with input():
# 1. input() always returns a string. math will fail unless you cast to int or float
# 2. If the user types something that's not a number, float() crashes the program
# 3. There's no validation,the user could type "seven dollars" and break it