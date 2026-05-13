#Cris Ramirez
# Sales Summary Calculator
# Concepts: user input, f-string, type cast, user-defined function

import math

associate_name = input("Enter the associate's name: ")
store_region = input("Enter the store region: ")
units_sold = int(input("Enter the number of units sold: "))
price_per_unit = float(input("Enter the price per unit: "))

def sales_summary(name, region, units, price):
    