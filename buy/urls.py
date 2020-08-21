from django.conf.urls import url
from . import  views
from django.urls import path




urlpatterns = [
    path('card_add/<int:book_id>/', views.card_add, name='card_add'),
    #path('card_add/', views.card_add, name='card_add'),
    path('card_home', views.card_home, name='card_home'),
    path('card_update', views.card_update, name='card_update'),    
    path('card_delete/<int:card_id>/', views.card_delete, name='card_delete'),
    path('shipping', views.shipping, name='shipping'),
    path('checkout', views.checkout, name='checkout'),
    path('payment', views.payment, name='payment'),
    path('order', views.order, name='order'),
    path('order_delete/<int:order_id>/', views.order_delete, name='order_delete'),
    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),

    path('check/<order_number>', views.check_order), # api
    path('checking/', views.checking ,name='checking'), # api check

 ]
