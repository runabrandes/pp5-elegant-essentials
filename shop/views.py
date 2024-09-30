from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Product

def shop(request):
    """
    This view renders shop.html
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'shop/shop.html', context)