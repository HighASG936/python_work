""" """
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
        
        