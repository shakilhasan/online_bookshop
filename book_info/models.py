from django.db import models

# Create your models here.
class Catagory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book_info(models.Model):
    cover= models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    author= models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
