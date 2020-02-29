from django.contrib import admin
from .models import Card
from .models import Order

# Register your models here.
admin.site.register(Card)
admin.site.register(Order)
