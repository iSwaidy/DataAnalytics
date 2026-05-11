## Cris Ramirez

pay_rate = 17.30
hours_worked = 45

if hours_worked > 40: # If the employee worked more than 40 hours, calculate regular pay and overtime pay
    regular_pay = 40 * pay_rate # Regular pay for the first 40 hours
    overtime_pay = (hours_worked - 40) * pay_rate * 1.5 # Overtime pay for hours worked beyond 40 hours (1.5 times the regular pay rate)
    gross_pay = regular_pay + overtime_pay # Total gross pay is the sum of regular pay and overtime pay
else:
    gross_pay = hours_worked * pay_rate # If the employee worked 40 hours or less, calculate gross pay as hours worked multiplied by the pay rate

# Output the pay rate, hours worked, and gross pay
print(f"Pay rate: ${pay_rate}")
print(f"Hours worked: {hours_worked}")
print(f"Gross pay: ${gross_pay:.2f}")