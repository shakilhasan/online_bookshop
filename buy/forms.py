from django import forms
from book_info.models import Book_info
from django.contrib.auth.models import User
from .models import Card
from .models import Order

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        # fields = ['name','author','description','price','available','catagory']
        fields = ['user','book','sold']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        #fields = ['user','name','phone','aphone','country','district','thana','address','total']
        #fields = '__all__'
        fields = ['name','phone','aphone','country','district','thana','address']
