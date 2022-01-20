from django.shortcuts import render
from product.models import Product
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from cart.cart import Cart

# Create your views here.
def cart(request):
    
    return render(request, 'frontend/cart.html')


def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    # print(product)
    cart.add(product=product)
    return HttpResponseRedirect(reverse('cart:index'))
    # return HttpResponse("working")


def cart_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    print(product)
    return JsonResponse({'message': 'success'})


def cart_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return JsonResponse({'message': 'success'})

def cart_remove(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)

    return JsonResponse({'message': 'success'})
