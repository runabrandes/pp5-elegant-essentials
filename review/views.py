from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.views.generic import ListView
from .models import Review
from .forms import ReviewForm



def reviews(request):
    """
    This view processes post request when users leave reviews for the shop. 
    """
    if request.method == "POST":
        reviews_form = ReviewForm(data=request.POST)
        if reviews_form.is_valid():
            review = reviews_form.save(commit=False)
            review.name = request.user
            reviews_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Many thanks for leaving your review!")
        else:
            for field, errors in reviews_form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")

    reviews_form = ReviewForm()

    return render(
        request,
        'review/review.html',
        {'reviews_form': reviews_form},
    )
