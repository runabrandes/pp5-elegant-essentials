from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import NewsletterForm

def newsletter_signup(request):
    if request.method == 'POST':
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            return redirect('newsletter_success')
        else:
            for field, errors in newsletter_form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
    else:
        newsletter_form = NewsletterForm()

    return render(request, 'newsletter/newsletter.html', {'newsletter_form': newsletter_form})


def newsletter_success(request):
    return render(request, 'newsletter/newsletter_success.html')