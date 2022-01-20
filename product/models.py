from django.db import models
from account.models import User
from phonenumber_field.modelfields import PhoneNumberField
from .utils import unique_slug_generator
from django.db.models.signals import pre_save

# Create your models here.
class Category(models.Model):
    name                        = models.CharField(max_length=100)
    slug                        = models.SlugField(null=True, blank=True, unique=True)
    special_offer               = models.BooleanField(default=False, verbose_name="Special Offer?")
    timestamp  		            = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category                    = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE, null=True, blank=True)
    slug                        = models.SlugField(null=True, blank=True, unique=True)
    name                        = models.CharField(max_length=100)
    description                 = models.CharField(max_length=5000, null=True, blank=True)
    about                       = models.CharField(max_length=200, null=True, blank=True)
    availability                = models.BooleanField(default=True)
    MOQ                         = models.SmallIntegerField( verbose_name="Minimum Order Quantity",null=True, blank=True)
    
    price			            = models.IntegerField()
    discount			        = models.DecimalField(max_digits=7, decimal_places=0, null=True, blank=True)
    image                       = models.ImageField(upload_to='media/product/images', null=True, blank=True)
    image2                      = models.ImageField(upload_to='media/product/images', null=True, blank=True)
    image3                      = models.ImageField(upload_to='media/product/images', null=True, blank=True)
    
    timestamp  		            = models.DateField(auto_now_add=True)

    def __str__(self):  
        return  "item -  %s quantity %d " % (self.name, self.price)





def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender=Product)
pre_save.connect(pre_save_receiver, sender=Category)