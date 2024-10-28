from django.db import models


class FAQ(models.Model):
    """
    Model for a Frequently Asked Question with a question and answer.
    """
    question = models.CharField(max_length=300)
    answer = models.TextField()

    def __str__(self):
        return self.question
