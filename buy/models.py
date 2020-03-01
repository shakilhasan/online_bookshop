from django.db import models
from book_info.models import Book_info
from django.contrib.auth.models import User
# Create your models here.



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100,default=1)
    phone = models.CharField(max_length=100,default=1)
    aphone =models.CharField(max_length=100,default=1)
    country = models.CharField(max_length=100,default=1)
    district = models.CharField(max_length=100,default=1)
    thana = models.CharField(max_length=100,default=1)
    address = models.CharField(max_length=1000,default=1)
    total = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id)

class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book_info, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now=True)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
