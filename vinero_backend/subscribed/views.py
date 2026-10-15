from django.shortcuts import render, redirect
from .models import Emails

# Create your views here.

def events_page(request):
    if request.method == "POST":
        Emails.objects.create(email=request.POST.get('email'))
        return redirect('events')
    return render(request, 'events.html')

