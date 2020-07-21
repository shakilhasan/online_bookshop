from rest_framework import serializers
from book_info.models import Book_info
from book_info.models import Catagory


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_info
        fields = '__all__'
        # fields = ['pk','name','author','description','price','available','catagory']

class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagory
        fields = '__all__'
        # fields = ['name']
