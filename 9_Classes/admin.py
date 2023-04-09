""" """

import n_user
import privileges

class Admin(n_user.User):
    """Special admin user"""
    def __init__(self, first_name, last_name, age, civil_status):
        """Set attributes like user. Then set attributes like admin user"""
        super().__init__(first_name, last_name, age, civil_status)
        self.privileges = privileges.Privileges()
        
        