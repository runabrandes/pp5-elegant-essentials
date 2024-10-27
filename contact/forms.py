from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Generates the contact request form for users so
    they can input needed information.
    """
    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'comment')
        labels = {
            'name': 'Name',
            'email': 'Email',
            'comment': 'Comment',
        }
