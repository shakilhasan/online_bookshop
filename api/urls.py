from django.conf.urls import url
from . import  views
from django.urls import path


urlpatterns = [
    path('check/<order_number>', views.check_order)
 ]
