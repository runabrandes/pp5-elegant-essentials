from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .models import Review
from .forms import ReviewForm


def reviews(request):
    """
    This view processes post request when users leave
    reviews for the shop.
    """
    if request.method == "POST":
        reviews_form = ReviewForm(data=request.POST)
        if reviews_form.is_valid():
            review = reviews_form.save(commit=False)
            review.name = request.user
            reviews_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Many thanks for leaving your review!"
                "It will be approved shortly.")
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


class ReviewListView(ListView):
    """
    View to output reviews.
    """
    model = Review
    context_object_name = 'reviews'
    template_name = 'review/review_overview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review'] = self.get_queryset()

        return context


def edit_review(request, review_id):
    """
    View to edit reviews.
    """
    review = get_object_or_404(Review, pk=review_id)

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST, instance=review)
        if review_form.is_valid() and review.name == request.user:
            review = review_form.save(commit=False)
            review.review_approved = False
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!'
                                 'Please wait whilst we approve it.')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Could not update review!')
        return HttpResponseRedirect(reverse('review_overview'))
    else:
        review_form = ReviewForm(instance=review)

    return render(request, 'review/edit_review.html',
                  {'review_form': review_form, 'review': review})


def delete_review(request, review_id):
    """
    View to delete a review.
    """
    review = get_object_or_404(Review, pk=review_id)

    if review.name == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS,
                             'Your review has been deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You are not authorised to delete this review.')

    return HttpResponseRedirect(reverse('review_overview'))
