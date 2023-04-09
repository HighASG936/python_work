""" """
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
        