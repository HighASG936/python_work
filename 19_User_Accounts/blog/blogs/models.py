from django.db import models

class BlogPost(models.Model):
    """A publication the user can entry """
    text = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text

class Entry(models.Model):
    """Content of post"""  
    title = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.TextField()
    delete_added = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model"""
        if len(self.text) >= 50:
            output = f"{self.text[:50]}"
        else:
            output = self.text
        return output



