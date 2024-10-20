from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.newsletter_signup, name='newsletter_signup'),
    path('success/', views.newsletter_success, name='newsletter_success'),
]