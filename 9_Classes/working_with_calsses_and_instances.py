#Name: Aurelio Siordia
#Date: 07/04/23

#9-4 Number served
class Restaurant:
    """A simple attempt to simulate a restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name & cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self, cost, location):
        """Display two pieces of information about restaurant"""
        print(f'Level Cost: {cost}')
        print(f'Location: {location}')
        

    def open_restaurant(self):
        """Display the restaurant is open"""
        print(f'The restaurant "{self.restaurant_name}" is open')

    def set_number_served(self, number_served):
        """Set a new number served"""
        self.number_served = number_served


    def increment_number_served(self, number):
        """Increment the number of served"""
        self.number_served += number 


restaurant = Restaurant('Taco Bell', 'Mexican food')
print(restaurant.number_served)
restaurant.number_served = 5
print(restaurant.number_served)
restaurant.set_number_served(10)
print(restaurant.number_served)
restaurant.increment_number_served(16)
print(f'{restaurant.number_served}\n')


#9-5 Login Attempts
class User:
    """A simple attempt to simulate an user"""
    def __init__(self, first_name, last_name, age, civil_status):
        """Initialize restaurant_name & cuisine_type"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.civil_status = civil_status
        self.login_attempts = 0
    
    
    def describe_user(self):
        """Display describe a user"""
        print(f'Name: {self.first_name} {self.last_name}')
        print(f'Age: {self.age}')
        print(f'Civil Status: {self.civil_status}')
    
    def greet_user(self):
        """Display a greeting to the user"""
        print(f'Good day {self.first_name}')

    def increment_login_attempts(self):
        """Increment login attempts"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset login attempts"""
        self.login_attempts = 0
      
      
user = User('Aurelio', 'Siordia', '30', 'single')

for counter in range(1,18):
    user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)






