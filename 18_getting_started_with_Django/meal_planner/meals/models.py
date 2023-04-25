from django.db import models

class Meal(models.Model):
    """Meal you can plane"""
    name = models.CharField(max_length=30)

    def __str__(self):
        """Return a string representation of the model"""
        return self.name

