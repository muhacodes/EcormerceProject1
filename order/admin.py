from django.contrib import admin
from .models import Order, Address, OrderItem
# Register your models here.

admin.site.register(Order)
admin.site.register(Address)
admin.site.register(OrderItem)