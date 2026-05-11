## Cris Ramirez


salary = 4500   # Monthly salary in dollars
tax_rate = 0.23 # Tax rate as a decimal (23% tax rate)
withheld = salary * tax_rate # Calculate the amount of taxes withheld using the formula: withheld = salary * tax_rate

# Display the results
print(f"You earn ${salary} per month")
print(f"Taxes withheld: ${withheld:.2f}")
print(f"Take home: ${salary - withheld:.2f}")