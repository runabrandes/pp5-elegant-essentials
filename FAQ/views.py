from django.shortcuts import render
from .models import FAQ


def faq_q_and_a(request):
    """
    View that retrieves all FAQs and renders them on the FAQ page.
    """
    faqs_page = FAQ.objects.all()
    return render(request, 'FAQ/FAQ.html', {'faqs_page': faqs_page})
