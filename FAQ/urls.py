from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.faq_q_and_a, name='faq_q_and_a'),
]