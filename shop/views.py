from django.shortcuts import render, get_object_or_404
from django.views import generic

def shop(request):
    """
    This view renders index.html
    """
    return render(request, 'shop/shop.html')