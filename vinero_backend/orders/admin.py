from django.contrib import admin

from .models import Orders

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('emri', 'emaili', 'nr_telefoni', 'adresa', 'qyteti', 'kodi_postar', 'emri_produktit', 'cmimi_total')
