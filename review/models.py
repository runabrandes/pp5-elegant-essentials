from django.db import models


class Review(models.Model):
    """
    Model for leaving public reviews for the store.
    """

    name = models.CharField(max_length=100, blank=False)
    review = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (f"{self.name} left a review on {self.date}.")


