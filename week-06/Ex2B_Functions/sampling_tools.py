# Cris Ramirez
# Lab 1 - Sampling Tools

import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam', 
'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']

# Scenario A: Product of the Day
product_of_the_day = random.choice(products)
print(f"Product of the Day: {product_of_the_day}")

# Scenario B: Usability survey
survey_products = random.sample(products, 3)
print(f"Survey products: {survey_products}")

# Scenario C: Shuffled display
random.shuffle(products)
print(f"Shuffled products: {products}")

# Scenario D: Transaction count
transactions = random.randint(50, 300)
print(f"Today's transaction count: {transactions}")