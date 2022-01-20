from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'backend'

urlpatterns = [
    path('home', login_required(views.home, login_url='user:login'), name='index'),

    # Category

    path('category', login_required(views.category), name='category'),

    path('category/add/', login_required(views.category_add), name='category-add'),

    path('category/edit/<int:pk>', login_required(views.category_edit), name='category-edit'),

    path('category/delete', login_required(views.category_delete), name='category-delete'),

    
    # Product

    path('product', login_required(views.product), name='product'),

    path('product/add/', login_required(views.product_add), name='product-add'),

    path('product/edit/<int:pk>', login_required(views.product_edit), name='product-edit'),

    path('product/delete', login_required(views.product_delete), name='product-delete'),

    path('product/content/<int:pk>', login_required(views.product_content), name='product-content'),


    # Order

    path('order', login_required(views.order), name='order'),

    # Testimonials
    path('testimonials', login_required(views.testimonials), name='testimonials'),
    
    path('testimonial-add', login_required(views.testimonial_add), name='testimonial-add'),

    path('testimonial/edit/<int:pk>', login_required(views.testimonial_edit), name='testimonial-edit'),

    path('testimonial/delete', login_required(views.testimonial_delete), name='testimonial-delete'),


    # Order

    path('order', login_required(views.order), name='order'),

    path('order/add/', login_required(views.order_add), name='order-add'),

    path('order/edit/<int:pk>', login_required(views.order_edit), name='order-edit'),

    path('order/delete', login_required(views.order_delete), name='order-delete'),
]
