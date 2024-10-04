from django.shortcuts import render, get_object_or_404
from django.views import generic

def bag(request):
    """
    This view renders bag.html
    """
    return render(request, 'bag/bag.html')