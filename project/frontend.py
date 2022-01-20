"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from . import views
from product.views import HomeView
from django.conf import settings
from django.conf.urls.static import static
from order.views import checkout

# app_name = 'frontend'

urlpatterns = [

    path('', views.home, name='home'),

    path('product/<slug:slug>', views.product_detail, name='product-detail'),

    path('cart/', include('Cart.urls', 'cart')),

    path('checkout', checkout, name='checkout'),


    path('about', views.about, name='about'),

    path('confirmation-order', views.confirm, name='confirm'),

    path('contact-us', views.contact_us, name='contact'),
    
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)