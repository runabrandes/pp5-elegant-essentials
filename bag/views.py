from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def bag(request):
    """
    This view renders bag.html
    """
    return render(request, 'bag/bag.html')


@login_required
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


@login_required
def update_bag(request, product_id):
    """Update quantity of a selected product in the bag """

    redirect_url = request.POST.get('redirect_url')
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[product_id] = quantity
    elif product_id in bag:
        bag.pop(product_id)

    request.session['bag'] = bag
    return redirect(redirect_url)


@login_required
def remove_from_bag(request, product_id):
    """Remove selected item from the bag"""

    try:
        bag = request.session.get('bag', {})
        if product_id in bag:
            bag.pop(product_id)

            request.session['bag'] = bag
            return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
