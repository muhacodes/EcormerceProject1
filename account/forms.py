from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import ChoiceWidget, PasswordInput
from .models import User
from django import forms
from .backend import Backend


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(CreateUser, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })
    

class LoginForm(forms.Form):
    # password = forms.CharField(widget=forms, PasswordInput, required=True)
    username = forms.CharField(max_length=255, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = Backend.authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = Backend.authenticate(username=username, password=password)
        return user