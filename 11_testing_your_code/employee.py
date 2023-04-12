#Name: Aurelio Siordia
#Date: 11/04/23

class Employee:
    """ """
    def __init__(self, first, last, annual_salary):
        self.first = first
        self.last = last
        self.annual_salary = annual_salary

    def give_raise(self,custom_raise=None):
        if custom_raise:
            updated_salary = int(self.annual_salary) + custom_raise
        else:
            updated_salary = int(self.annual_salary) + 5000
        return updated_salary


