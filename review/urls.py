from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('overview/', views.ReviewListView.as_view(), name='review_overview'),
    path('edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),
]