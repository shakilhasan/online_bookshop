# from django.conf.urls import url
from . import  views
from django.urls import path

app_name = "cgpa"
urlpatterns = [
     path('student_add/', views.student_add, name= 'student_add'),
     path('student_home/', views.student_home, name= 'student_home'),
     path('student_edit/<int:student_id>/', views.student_edit, name='student_edit'),
     path('student_delete/<int:student_id>/', views.student_delete, name='student_delete'),


     path('course_add/', views.course_add, name= 'course_add'),
     path('course_home/', views.course_home, name='course_home'),
     path('course_edit/<int:course_id>/', views.course_edit, name='course_edit'),
     path('course_delete/<int:course_id>/', views.course_delete, name='course_delete'),


     path('result_add/', views.result_add, name= 'result_add'),
     path('result_home/', views.result_home, name= 'result_home'),
     path('result_edit/<int:result_id>/', views.result_edit, name='result_edit'),
     path('result_delete/<int:result_id>/', views.result_delete, name='result_delete'),

 ]
