from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('overview/', views.ReviewListView.as_view(), name='review_overview'),
]