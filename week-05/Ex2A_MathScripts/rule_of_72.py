### Cris Ramirez

savings = 5000
interest_rate = 0.06        # 6%
years = 72 / (interest_rate * 100)
doubled = savings * 2

print("Your current savings is " + str(savings) + ".")
print("At a " + format(interest_rate, ".0%") + " interest rate, your savings account will be worth " + format(doubled, ".2f")  + " in " + format(years, ".1f")  + " years")