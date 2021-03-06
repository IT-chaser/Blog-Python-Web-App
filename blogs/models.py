from django.db import models

class BlogPost(models.Model):
    """A post about blog."""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.title.upper()}  ...  {self.text}"
