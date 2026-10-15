from django.contrib import admin
from .models import WineCategory, WineProduct

# Register your models here.


@admin.register(WineProduct)
class WineProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'vintage')
    list_filter = ('category',)
    search_fields = ('name', 'description')

admin.site.register(WineCategory)
