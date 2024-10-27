from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Generates the review form for users
    """
    class Meta:
        model = Review
        fields = ['review']
        labels = {
            'review': 'Review',
        }
