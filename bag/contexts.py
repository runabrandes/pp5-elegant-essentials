from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from shop.models import Product

def bag_contents(request):
    bag = request.session.get('bag', {})
    bag_items = []
    total = Decimal('0.00')
    product_count = 0
    delivery = Decimal(settings.STANDARD_DELIVERY_FEE)

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        item_total = quantity * Decimal(product.price)
        total += item_total
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'subtotal': item_total,
        })

    grand_total = total + delivery

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context