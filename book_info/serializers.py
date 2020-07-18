from rest_framework import serializers
from book_info.models import Book_info


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_info
        fields = '__all__'
        # fields = ['pk','name','author','description','price','available','catagory']
