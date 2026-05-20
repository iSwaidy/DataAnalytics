# Cris Ramirez
# Exercise 3.A Lab 1 - Working with Classes

class Restaurant:
    '''A class to represent a restaurant.'''
    
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
    
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")
    
    def rest_open(self):
        print(f"{self.rest_name} is open.")


restaurant1 = Restaurant('Pizza Palace', 'Italian food')
restaurant2 = Restaurant('Sushi Spot', 'Japanese food')
restaurant3 = Restaurant('Taco Town', 'Mexican food')

restaurant1.describe_rest()
restaurant1.rest_open()

restaurant2.describe_rest()
restaurant2.rest_open()

restaurant3.describe_rest()
restaurant3.rest_open()