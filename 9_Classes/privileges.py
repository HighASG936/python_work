""" """

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