from django.shortcuts import render, redirect
from .models import Orders

def checkout_order(request):
    if request.method == 'POST':
        Orders.objects.create(
            emri=request.POST.get('full-name'),
            emaili=request.POST.get('email'),
            nr_telefoni=request.POST.get('phone'),
            adresa=request.POST.get('address'),
            qyteti=request.POST.get('city'),
            kodi_postar=request.POST.get('postal-code'),
            emri_produktit=request.POST.get('emri_produktit'),
            cmimi_total=request.POST.get('cmimi_total')
        )
        return render(request, 'checkout_success.html')
