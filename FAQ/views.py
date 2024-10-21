from django.shortcuts import render
from .models import FAQ

# Create your views here.
def faq_q_and_a(request):
    faqs_page = FAQ.objects.all()
    return render(request, 'FAQ/FAQ.html', {'faqs_page': faqs_page})