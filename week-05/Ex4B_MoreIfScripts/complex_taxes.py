## Cris Ramirez

pay_rate = float(input("Enter pay rate: $"))
hours_worked = float(input("Hours worked this week: "))
filing_status = input("Filing status (single or joint): ").lower()

# Calculate gross pay with overtime
if hours_worked > 40:
    gross_pay = (40 * pay_rate) + ((hours_worked - 40) * pay_rate * 1.5)
else:
    gross_pay = hours_worked * pay_rate

annual_gross = gross_pay * 52

# Determine tax rate based on filing status and annual gross income
if filing_status == "single":
    if annual_gross < 12000:
        tax_rate = 0.05
    elif annual_gross < 25000:
        tax_rate = 0.10
    elif annual_gross < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
elif filing_status == "joint":
    if annual_gross < 12000:
        tax_rate = 0.00
    elif annual_gross < 25000:
        tax_rate = 0.06
    elif annual_gross < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20

# Calculate tax withheld and net pay
tax_withheld = gross_pay * tax_rate
net_pay = gross_pay - tax_withheld

# Print the results
print(f"You worked {hours_worked} hours this period.")
print(f"Because you earn ${pay_rate} per hour, your gross weekly pay is ${gross_pay:.2f}")
print(f"Your filing status is {filing_status}")
print(f"Your tax withholding for the week is ${tax_withheld:.2f}")
print(f"Your net pay is ${net_pay:.2f}")