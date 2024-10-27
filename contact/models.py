from django.db import models
from django.utils import timezone


class Contact(models.Model):
    """
    Model for contacting the store.
    """

    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    comment = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.name} sent a request on {self.date}."
                + f"They can be reached at {self.email}.")

    class Meta:
        verbose_name = "Request"
        verbose_name_plural = "Requests"
