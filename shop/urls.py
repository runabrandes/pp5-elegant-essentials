from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('<product_id>', views.product_info, name='product_info')
]
