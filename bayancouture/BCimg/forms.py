# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from BCimg.models import User, couture



class RegistrationForm(UserCreationForm):
   
   class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)
    item_id = forms.IntegerField(widget=forms.HiddenInput())
    username = forms.CharField(max_length=255, widget=forms.HiddenInput())

class AddabayaForm(forms.ModelForm):
    class Meta:
        model = couture
        fields = ['title', 'description', 'code', 'price', 'size','image']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.TextInput(attrs={'class': 'form-control'})
           
        }