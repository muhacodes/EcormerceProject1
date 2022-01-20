from django.db import models
from product.models import Product
from account.models import User
from account.models import customer
# Create your models here.

class OrderItem(models.Model):
    product             = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity            = models.SmallIntegerField()
    price			    = models.DecimalField(max_digits=7, decimal_places=2)
    timestamp  		    = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product.name



class Order(models.Model):
    item                = models.ManyToManyField(OrderItem)
    customer            = models.ForeignKey(customer, related_name='order_customer', on_delete=models.CASCADE, null=True)
    address             = models.ForeignKey("order.Address", related_name='order_address', on_delete=models.CASCADE, blank=True, null=True)
    message             = models.TextField(max_length=1000, null=True, blank=True)
    deliver             = models.DateField(verbose_name="Delivery Date", null=True, blank=True)
    timestamp  		    = models.DateField(auto_now_add=True)

    def __str__(self):
        variations = ','.join(str(v) for v in self.item.all())
        return "{},{}".format(self.customer, variations)
        # return ' / '.join(item.OrderItem for order_obj in self.item.all())
	    # return "%s" %(self.item, )



class Address(models.Model):
    address             = models.CharField(max_length=500)
    appartment          = models.CharField(max_length=500, null=True, blank=True)
    street              = models.CharField(max_length=500, null=True, blank=True)
    LandMark            = models.CharField(max_length=500, null=True, blank=True)
    notes               = models.TextField(verbose_name="Comment", null=True, blank=True)
    timestamp  		    = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.address