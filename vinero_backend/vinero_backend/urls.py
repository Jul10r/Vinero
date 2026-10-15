"""
URL configuration for vinero_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from products.views import home, products_page, checkout_view
from orders import views as orders_views
from django.views.static import serve
import os
from subscribed.views import events_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  
    path('products/', products_page, name='products_page'),
    path('checkout.html', checkout_view, name='checkout'),
    path('porosi/', orders_views.checkout_order, name='checkout_order'),
    path('events/', events_page, name='events'),
    path('rreth-nesh/', serve, {
        'document_root': os.path.join(settings.BASE_DIR, '..', 'frontend'),
        'path': 'rreth-nesh.html'
    }, name='rreth_nesh'),
]

urlpatterns += static('css/', document_root=os.path.join(settings.BASE_DIR, '..', 'frontend', 'css'))
urlpatterns += static('img/', document_root=os.path.join(settings.BASE_DIR, '..', 'frontend', 'img'))
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
