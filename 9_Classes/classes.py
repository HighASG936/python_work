#Name: Aurelio Siordia
#Date: 07/04/23

#9-1 Restaurant
class Restaurant:
    """A simple attempt to simulate a restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name & cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self, cost, location):
        """Display two pieces of information about restaurant"""
        print(f'Level Cost: {cost}')
        print(f'Location: {location}')
        


    def open_restaurant(self):
        """Display the restaurant is open"""
        print(f'The restaurant "{self.restaurant_name}" is open')

res1 = Restaurant('Italianni Moe', 'italian food')
print(f'Name: {res1.restaurant_name}')
print(f'Cusine Type: {res1.cuisine_type}')
res1.describe_restaurant('$$', '1st. Avenue')
res1.open_restaurant()
print()


#9-2 Three Restaurants
res2 = Restaurant('Monster Burger', 'Burgers and chips')
print(f'Name: {res2.restaurant_name}')
print(f'Cusine Type: {res2.cuisine_type}')
res2.describe_restaurant('$', 'Chester Street')
res2.open_restaurant()
print()

res3 = Restaurant('Taco Marquito', 'Mexican food')
print(f'Name: {res3.restaurant_name}')
print(f'Cusine Type: {res3.cuisine_type}')
res3.describe_restaurant('$', 'Overton Avenue')
res3.open_restaurant()
print()

res4 = Restaurant("Je t'aime", 'French food')
print(f'Name: {res4.restaurant_name}')
print(f'Cusine Type: {res4.cuisine_type}')
res4.describe_restaurant('$$$', 'Lavanda Street')
res4.open_restaurant()
print()


#9-3 Users
class User:
    """A simple attempt to simulate an user"""
    def __init__(self, first_name, last_name, age, civil_status):
        """Initialize restaurant_name & cuisine_type"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.civil_status = civil_status
    
    
    def describe_user(self):
        """Display describe a user"""
        print(f'Name: {self.first_name} {self.last_name}')
        print(f'Age: {self.age}')
        print(f'Civil Status: {self.civil_status}')
    
    def greet_user(self):
        """Display a greeting to the user"""
        print(f'Good day {self.first_name}')


user1 = User('Kevin', 'Roosevelt', 40, 'marriaged')
user1.describe_user()
user1.greet_user()
print()

user2 = User('Robert', 'Mckanzie', 19, 'single')
user2.describe_user()
user2.greet_user()
print()
        
user3 = User('Clarence', 'Lee', 25, 'divorced')
user3.describe_user()
user3.greet_user()
print()

user4 = User('Sandra', 'Goodman', 32, 'marriage')
user4.describe_user()
user4.greet_user()
print()

user5 = User('Lola', 'Kethmen', 29, 'marriage')
user5.describe_user()
user5.greet_user()
print()
        
        
        