from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'date',)
    search_fields = ['name']
    list_filter = ('name',)
