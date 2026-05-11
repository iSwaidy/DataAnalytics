## Cris Ramirez
## 05/04/26
## Exercise 1B

customer_id = 10472                # int for now. If IDs ever start with 0, this breaks — should probably be a string.
customer_name = "Bob Smith"        # full name as one string. Probably better split into first and last.
customer_gender = "M"              # single letter. Limiting — full strings would be more inclusive.
customer_dob = "1995-03-14"        # string, but Python has actual date types that'd be more useful here.
drivers_license = "D1234567"       # string, has a letter in it.
auto_policy = "AP-998877"          # same deal.

# About me
my_name = "Cris"
hometown_city = "Roselle"
hometown_state = "NJ"

# Reserved words in Python:
# False, None, True, and, as, assert, async, await, break, class, continue,
# def, del, elif, else, except, finally, for, from, global, if, import, in,
# is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

# Five I picked:
# if      — runs the indented code only when the condition is True.
# else    — the fallback. Runs when if was False.
# for     — loops through a ^^sequence^^ (list, string, whatever).
# def     — makes a ^^function^^. Reusable code you can call later.
# return  — sends a value back out of a function.