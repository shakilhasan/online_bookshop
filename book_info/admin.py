from django.contrib import admin
from .models import Book_info
from .models import Catagory

# Register your models here.
admin.site.register(Catagory)
admin.site.register(Book_info)
