from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.bag, name='bag'),
    path('add/<product_id>/', views.add_to_bag, name='add_to_bag'),
    path('update/<product_id>/', views.update_bag, name='update_bag'),
    path('remove/<product_id>/', views.remove_from_bag,
        name='remove_from_bag'),
]
