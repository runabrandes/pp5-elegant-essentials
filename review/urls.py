from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('review_overview', views.review_overview, name='review_overview'),
]