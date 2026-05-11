##Cris Ramirez

# This program will greet the user based on the time of day.
hour = int(input("What hour is it (0-23)? "))

# The following code will print a greeting based on the hour of the day.
if hour >= 23 or hour < 4: 
    print("What are you doing up so late??") 
    print("Good morning!")
elif hour < 17:
    print("Good day!")
else:
    print("Good evening!")