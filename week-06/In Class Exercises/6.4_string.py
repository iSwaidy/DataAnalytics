# Cris Ramirez

# Define function with a single function call

def parse_inv_code(inv_code):
    parts    = inv_code.split("-")
    category = parts[0]
    location = parts[1]
    item_no  = parts[2]
    return category, location, item_no

cat, loc, num = parse_inv_code("ELC-B04-00142")

print(cat)  # ELC
print(loc)  # B04
print(num)  # 00142

# iterate with a for loop, passing each code as the argument

inv_codes = [
    "ELC-B04-00142",
    "PLB-A01-00089",
    "TLS-C12-00374",
    "ELC-B07-00215",
    "HVA-D03-00501"
]

for code in inv_codes:
    cat, loc, num = parse_inv_code(code)
    print(f"Category: {cat}  Location: {loc}  Item: {num}")