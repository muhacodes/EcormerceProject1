from traceback import print_tb
from django.forms import fields
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from .forms import category_form, product_form, testimonial_form, order_form
from product.models import Product, Category
from order.models import Order, OrderItem
from .models import Testimonials
from django.contrib import messages
from django.views.generic import UpdateView
from django.db.models import Sum
import os
from project.settings import BASE_DIR
from order.forms import itemsOrdered
# Create your views here.


def home(request):
    
    context = {
        'orders' : Order.objects.all().count(),
        'products' : Product.objects.all().count(),
    }

    return render(request, 'backend/home.html', context)



# Category
def category(request):
    context = {
        'object_list' : Category.objects.all()
    }
    return render(request, 'backend/category.html', context)


def category_add(request):
    form = category_form(request.POST or None)

    if form.is_valid():
        form.save()
        messages.error(request, 'Your actions have been succesfully saved !')
        return HttpResponseRedirect(reverse('backend:category'))

        
    return render(request, 'backend/category-add.html', {'form': form})


def category_edit(request, pk):
    object = Category.objects.get(id=pk)
    form = category_form(request.POST or None, instance=object)

    if form.is_valid():
        form.save()
        request.session['message'] = True
        return HttpResponseRedirect(reverse('backend:category'))
    
    return render(request, 'backend/category-edit.html', {'form': form})


def category_delete(request):
    pk = request.POST['product']
    object = Category.objects.get(id=pk)
    object.delete()
    messages.error(request, 'Your actions have been succesfully saved !')
    return HttpResponseRedirect(reverse('backend:category'))



# Product
def product(request):
    context = {
        'object_list' : Product.objects.all()
    }
    return render(request, 'backend/product.html', context)


def product_add(request):
    form = product_form(request.POST or None, request.FILES)
    # print(form)
    if form.is_valid():
        form.save()
        print("valid")
        return HttpResponseRedirect(reverse('backend:product'))

    
    return render(request, 'backend/product-add.html', {'form': form})


# class product_edit(UpdateView):
#     model = Product
#     form_class = 'product_form'
#     template_name = 'backend/product-edit.html'
#     success_url = '/'

def product_edit(request, pk):
    obj = Product.objects.get(id=pk)
    form = product_form(request.POST or None, request.FILES or None, instance=obj)
    
    if form.is_valid():
        obj = form.save(commit=False)
        print(obj.image.storage)
        obj.save()
        print(obj)
        messages.error(request, 'Your actions have been succesfully saved !')
        return HttpResponseRedirect(reverse('backend:product'))
    
    return render(request, 'backend/product-edit.html', {'form': form})


def product_delete(request):
    pk = request.POST['product']
    object = Product.objects.get(id=pk)
    object.delete()
    messages.error(request, 'Your actions have been succesfully saved !')
    return HttpResponseRedirect(reverse('backend:product'))


def product_content(request, pk):
    object = Product.objects.get(id=pk)
    context = {
        'description': object.description,
    }

    return JsonResponse(context) 


# TEstimonials
def testimonials(request):
    context =  {
        'object_list': Testimonials.objects.all()
    }

    return render(request, 'backend/testimonials.html', context)


def testimonial_add(request):
    form = testimonial_form(request.POST or None)
    if form.is_valid():
        # object = form.save(commit=False)
        form.save()
        return HttpResponseRedirect(reverse('backend:testimonials'))

    return render(request, 'backend/testimonial-add.html', {'form': form})


def testimonial_edit(request, pk):
    object = Testimonials.objects.get(id=pk)
    form = testimonial_form(request.POST or None, instance=object)
    
    if form.is_valid():
        form.save()

        return HttpResponseRedirect(reverse('backend:testimonials'))
    
    return render(request, 'backend/testimonial-add.html', {'form': form})


def testimonial_delete(request):
    pk = request.POST['product']
    object = Testimonials.objects.get(id=pk)
    object.delete()

    return HttpResponseRedirect(reverse('backend:testimonials'))


# Orders
def order(request):
    context = {
        'object_list' : Order.objects.all()
    }
    return render(request, 'backend/order.html', context)


def order_add(request):
    form = order_form(request.POST or None, request.FILES)
    # print(form)
    if form.is_valid():
        form.save()
        print("valid")
        return HttpResponseRedirect(reverse('backend:order'))

    
    return render(request, 'backend/order-add.html', {'form': form})


def order_edit(request, pk):
    object = Order.objects.get(id=pk)
    form = order_form(request.POST or None, instance=object)
    
    # print(pk)


    if form.is_valid():
        form.save()

        return HttpResponseRedirect(reverse('backend:order'))
    
    return render(request, 'backend/order-edit.html', {'form': form})


def order_delete(request):
    pk = request.POST['product']
    object = Order.objects.get(id=pk)
    # object.delete()

    return HttpResponseRedirect(reverse('backend:order'))