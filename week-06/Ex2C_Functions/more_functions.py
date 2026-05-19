# Cris Ramirez


# Function 1

def display_mailing_label(name, address, city, state, zip):
    print(f"{name}\n{address}\n{city}, {state} {zip}")

display_mailing_label('Bob Smith', '123 Bob Road', 'Bobbyville', 'NJ', '07012')
display_mailing_label('Sarah Johnson', '456 Sarah Blvd', 'Miami', 'FL', '33101')

# Function 2
def add_numbers(*nums):
    total = sum(nums)
    expression = " + ".join(str(n) for n in nums)
    print(f"{expression} = {total}")

add_numbers(7)                   # one number
add_numbers(7, 13)               # two numbers
add_numbers(7, 13, 20, 5, 100)   # your choice, more than two

# Function 3

def display_receipt(total_due, amount_paid):
    if amount_paid >= total_due:
        change = amount_paid - total_due
        print(f"Total Due: ${total_due:.2f}")
        print(f"Amount Paid: ${amount_paid:.2f}")
        print(f"Change Due: ${change:.2f}")
    else:
        balance = total_due - amount_paid
        print(f"Total Due: ${total_due:.2f}")
        print(f"Amount Paid: ${amount_paid:.2f}")
        print(f"Balance Due: ${balance:.2f}")

display_receipt(50.00, 60.00)    # overpay
display_receipt(50.00, 50.00)    # exact
display_receipt(50.00, 40.00)    # underpay