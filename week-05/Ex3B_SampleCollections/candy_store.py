## Cris Ramirez

candies = ("gummy bears", "lollipops", "hard candy")
flavors = ("strawberry", "watermelon", "blue raspberry")

# Sets only hold unique items, and they don't promise any order.
combos = {
    candies[0] + " " + flavors[1],   
    candies[1] + " " + flavors[0],   
    candies[2] + " " + flavors[2],   
}

print("Today's candy options include:")
print(combos)

# We can add more items to a set, but we can't change the existing ones.