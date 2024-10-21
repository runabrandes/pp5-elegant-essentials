from django.contrib import admin
from .models import FAQ

@admin.register(Contact)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)