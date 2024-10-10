from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There are currently no items in your bag")
        return redirect(reverse('shop'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Q8SnMAn8cKANS5IDFzDDT6wnykoYqv1PXfw2MvbbVe3xfxyS7SwDXxJOeyZF7tAY4lul46p9IUNR7XAptL7ITjH00XEgm2KWm',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)