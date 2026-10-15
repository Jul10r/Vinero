from django.shortcuts import render
from .models import WineCategory, WineProduct



def home(request):
    products = WineProduct.objects.all()[:3]
    return render(request, 'index.html', {'products': products})


def products_page(request):
    categories = WineCategory.objects.all()
    return render(request, 'products.html', {'categories': categories})


def checkout_view(request):
    product = None
    quantity = 1
    product_id = request.GET.get('product_id')
    if product_id:
        try:
            product = WineProduct.objects.get(id=product_id)
        except WineProduct.DoesNotExist:
            product = None
    return render(request, 'checkout.html', {'product': product, 'quantity': quantity})


