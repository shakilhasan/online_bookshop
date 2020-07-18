from django.conf.urls import url
from . import  views
from django.urls import path, re_path



urlpatterns = [
    path('', views.book_home, name= 'book_home'),
    path('catagory_add/', views.catagory_add, name= 'catagory_add'),
    path('book_add/', views.book_add, name= 'book_add'),
    path('book_edit/<int:book_id>/', views.book_edit, name='book_edit'),
    path('book_delete/<int:book_id>/', views.book_delete, name='book_delete'),
    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),
    path('catagory_home/', views.catagory_home, name='catagory_home'),
    path('catagory_detail/<int:catagory_id>/', views.catagory_detail, name='catagory_detail'),

# api
    path('api/v1/posts/',  views.post_collection, name= 'post_collection'),
    path('api/v1/posts/<int:pk>/', views.post_element, name='post_element'),

 ]
