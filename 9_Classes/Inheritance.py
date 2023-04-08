#Name: Aurelio Siordia
#Date: 08/04/23

#9-6 Number served
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


class IceCreamStand(Restaurant):
    """ """
    def __init__(self, restaurant_name, cuisine_type=''):
        """Initialize attributes of the parent class. Then initialize attributes
            specific to a Ice cream stand  """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vainilla', 'strawberry', 'oreo', 'lemon']


    def display_flavors(self):
        print("You'll find ice cream flavored:")
        for flavor in self.flavors:
            print(f' - {flavor}')

Ice_cream_stand = IceCreamStand(restaurant_name='Ice Ice Baby!')
            
Ice_cream_stand.display_flavors()            
print()

#9-7 Admin & 9-8 Privileges
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
 

class Privileges:
    """Store privilage of admin user"""
    def __init__(self):
        """Initialize attribute of class Privileges"""
        self.privileges = ['can add post', 'can delete post', 'can ban user']


    def show_privileges(self):
        """ """
        print('Admin privileges: ')
        for privilege in self.privileges:
            print(f' - {privilege}')


class Admin(User):
    """Special admin user"""
    def __init__(self, first_name, last_name, age, civil_status):
        """Set attributes like user. Then set attributes like admin user"""
        super().__init__(first_name, last_name, age, civil_status)
        self.privileges = Privileges()
            

admin = Admin('Aurelio', 'Siordia', '30', 'single')
admin.privileges.show_privileges()
print()


#9-9 Battery Upgrade
class Car:
    """A simple attempt to represent a car"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")
        
        
    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicules"""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 75
    

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kHh battery")
    
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315        
        print (f"This car can go about {range} miles on a full charge.")
            
    
    def upgrade_battery(self):
        """Upgrade battery"""
        if self.battery_size < 100:
            self.battery_size = 100
        
        

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
print(my_tesla.describe_battery())
print(my_tesla.get_range())

print(my_tesla.upgrade_battery())

print(my_tesla.get_descriptive_name())
print(my_tesla.describe_battery())
print(my_tesla.get_range())



