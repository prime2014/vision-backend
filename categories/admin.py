from django.contrib import admin
from categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline',)
    list_filter = ('name',)
    search_fields = ('name',)
