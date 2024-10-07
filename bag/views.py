from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

def bag(request):
    """
    This view renders bag.html
    """
    return render(request, 'bag/bag.html')

def add_to_bag(request, product_id):
    """ Add a specified quantity of a selected product to the bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)