"""
URL configuration for elegant_essentials project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('', include('home_page.urls')),
    path('shop/', include('shop.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profiles/', include('profiles.urls')),
    path('contact/', include('contact.urls')),
    path('newsletter/', include('newsletter.urls')),
    path('FAQ/', include('FAQ.urls')),
    path('review/', include('review.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)