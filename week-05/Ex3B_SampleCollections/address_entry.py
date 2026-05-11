### Cris Ramirez


# Dictionary

contact_info = {
    "name": "BOB SMITH",
    "address": "123 Main St",
    "city": "Clownsville",
    "state": "NJ",
    "zip": "99999"
}

# Print the address 
print(f"""{contact_info['name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}""")

# Remove the key:value pair for name
del contact_info["name"]

# Add a new variable for full_name and assign its value as a dictionary
full_name = {
    "first name": "Bob",
    "last name": "Smith"
}

# se the .update() method to add one more key:value pair to full_name, with the key
# “honorific” and the value set to Mr. / Ms. / Mx. / Dr. / Hon. / etc. as appropriate.
full_name.update({"honorific": "MR."})

# Use the .update() method to add full_name to contact_info
contact_info.update({"full_name": full_name})

# Print the formatted address again, updating as needed to include the new dictionary items
print(f"""
{contact_info['full_name']['honorific']} {contact_info['full_name']['first name']} {contact_info['full_name']['last name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}""")