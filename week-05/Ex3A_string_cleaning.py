## Cris Ramirez

name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

# convert all three names to lowercase
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

print('-' * 30)

# convert all three names to title case
print(name_1.title())
print(name_2.title())
print(name_3.title())

print('-' * 30)

# remove the $ from both salary strings
print(salary_1.replace("$", ""))
print(salary_2.replace("$", ""))
print(type(salary_1.replace("$", "")))   # still a string
# To do math on these, also drop the comma and cast to int.

print('-' * 30)

# chain together
salary_1_int = int(salary_1.replace("$", "").replace(",", ""))
print(salary_1_int, type(salary_1_int)) 