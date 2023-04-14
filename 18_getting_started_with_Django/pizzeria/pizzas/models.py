from django.db import models

class Pizza(models.Model):
    """A pizza the user can choose"""
    name = models.CharField(max_length=20)
    
    def __str__(self):
        """Return a string representation of the model"""
        return self.name
    
class Topping(models.Model):
    """Set topping for each pizza"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    
    def __str__(self):
        """Return a string representation of the model"""
        return self.name
    
