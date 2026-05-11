## Cris Ramirez


import math

people = 38
seats_per_van = 15
cost_per_van = 250

vans_needed = math.ceil(people / seats_per_van)
total_cost = vans_needed * cost_per_van
cost_per_person = total_cost / people

print(f"Tourists: {people}")
print(f"Vans needed: {vans_needed}")
print(f"Total cost: ${total_cost}")
print(f"Cost per person: ${cost_per_person:.2f}")



# a) How much money did your script say you had to charge per person?
# $19.74

# b) If you multiply that out, how much did you collect?
# $750.00

# c) How much were the vans?
# $250

# d) Why do you have leftover money?
# The leftover money is due to the fact that we had to round up the number of vans needed to accommodate all the tourists. 