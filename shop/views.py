from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.views import generic
from .models import Product, Category
from django.db.models import Q


def shop(request):
    """
    This view renders shop.html
    """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category']
            products = products.filter(category__category_name__icontains=categories)
            categories = Category.objects.filter(category_name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'Please enter a search criteria!')
                return redirect(reverse('products'))
            
            queries = Q(product_name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        sort = request.GET.get('sort')
        direction = request.GET.get('direction')

        if sort == 'price':
            if direction == 'asc':
                products = products.order_by('price')
            elif direction == 'desc':
                products = products.order_by('-price')

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'shop/shop.html', context)


def product_info(request, product_id):
    """ A view to show individual product information """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'shop/product_info.html', context)