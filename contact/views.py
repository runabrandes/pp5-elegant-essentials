from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.views.generic import ListView
from .models import Contact
from .forms import ContactForm


def contact_request(request):
    """
    This view processes POST requests related to
    sending contact requests to the shop. On a POST request,
    it validates the submitted form, saves it,
    and associates it with the active user.
    """
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.name = contact_form.cleaned_data['name']
            contact_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Many thanks for contacting Elegant Essentials."
                + " We will aim to get back to you within 5 days!")
        else:
            for field, errors in contact_form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")

    contact_form = ContactForm()

    return render(
        request,
        'contact/contact.html',
        {'contact_form': contact_form},
    )
