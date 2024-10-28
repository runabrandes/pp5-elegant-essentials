from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):
    """
    Form for subscribing to the newsletter with name and email.
    """
    class Meta:
        model = Newsletter
        fields = ['name', 'email']
