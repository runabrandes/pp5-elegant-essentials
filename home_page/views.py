from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView


def index(request):
    """
    This view renders index.html
    """
    return render(request, 'home_page/index.html')