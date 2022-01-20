from django import forms
from phonenumber_field.modelfields import PhoneNumberField
from django.forms import ModelForm



class ContactForm(forms.Form):
    name                = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name'}))
    email               = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your Email'}))
    phone               = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    message             = forms.CharField(widget=forms.Textarea(attrs={'placeholder' : 'What do you want to say', 'rows' : 3, 'cols' : 100}), required=True)
    

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })
