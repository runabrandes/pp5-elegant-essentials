from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    """
    Model for leaving public reviews for the store.
    """

    name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="review_name") 
    review = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
    review_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return (f"{self.name} left a review on {self.date}.")
