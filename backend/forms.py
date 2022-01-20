from django.forms import ModelForm
from product.models  import Category, Product
from .models import Testimonials
from order.models import Order
from django import forms        

class category_form(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(category_form, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'style': 'color: white'
        })
    

class product_form(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

        widgets = {
        'expire': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(product_form, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'style': 'color: white'
        })


class testimonial_form(ModelForm):
    class Meta:
        model = Testimonials
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(testimonial_form, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'style': 'color: white'
        })

class order_form(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(order_form, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'style': 'color: white'
        })