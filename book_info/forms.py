from django import forms
from .models import Catagory
from .models import Book_info

class CatagoryForm(forms.ModelForm):
    class Meta:
        model = Catagory
        fields = '__all__'

class BookAddForm(forms.ModelForm):
    class Meta:
        model = Book_info
        # fields = ['name','author','description','price','available','catagory']
        fields = ['cover','name','author','description','price','available','catagory']
