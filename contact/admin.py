from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'date',)
    search_fields = ['name']
    list_filter = ('name',)
