from django.db import models


class Newsletter(models.Model):
    """
    A model for a newsletter subscription with name, email and date.
    """
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.name} has signed up to our newsletter on {self.date}."
                + f" The email address used was: {self.email}.")
