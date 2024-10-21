from django.shortcuts import render
from .models import FAQ

# Create your views here.
def faq_q_and_a(request):
    faq_page = FAQ.objects.all()
    return render(request, 'FAQ/FAQ.html', {faq_page: faq_page})