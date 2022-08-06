from django.db import models
from product.models import Product
from account.models import User
from account.models import customer
from django.utils.crypto import get_random_string
from django.db.models.signals import pre_save, post_save
from django.utils.crypto import get_random_string
from django.template.loader import render_to_string, get_template
from datetime import date, timedelta
from django.core.mail import EmailMessage
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
    order_id            = models.CharField(max_length=10, blank=True)
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
    

def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = get_random_string(length=5)


def SendConfirmationOrderMail(sender, instance, **kwargs):
    current = date.today()

    EstimatedDeliveryDate = current + timedelta(days=1)
    ctx = {
        'Name': instance.customer.name,
        'order_id' :instance.order_id,
        'deliveryDate' :EstimatedDeliveryDate
        
    }
    message = get_template('mail.html').render(ctx)
    msg = EmailMessage(
        'Order Confirmation',
        message,
        'app@lqcollectionstore.com',
        [instance.customer.email],
    )
    msg.content_subtype ="html"# Main content is now text/html
    msg.send()


def SendConfirmationOrderMailToAdmin(sender, instance, **kwargs):
    ctx = {
        'Name': instance.customer.name,
        'order_id' :instance.order_id,
        'phone' : instance.customer.phone_number,
    }
    message = get_template('confirm.html').render(ctx)
    msg = EmailMessage(
        'New Order',
        message,
        'app@lqcollectionstore.com',
        ['Layla.qalombi26@gmail.com', 'muha.oq3@gmail.com'],
    )
    msg.content_subtype ="html"# Main content is now text/html
    msg.send()



pre_save.connect(pre_save_create_order_id, sender=Order)

post_save.connect(SendConfirmationOrderMail, sender=Order)

post_save.connect(SendConfirmationOrderMailToAdmin, sender=Order)
