from django.shortcuts import render
from .models import Course
from .models import Result
from .models import Student
from .forms import CourseForm
from .forms import ResultForm
from .forms import StudentForm
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.decorators import login_required
# Create your views here.

#...........student.......................
@login_required(login_url='/login/')
def student_add(request):
    template = loader.get_template('cgpa/student_add.html')
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            # form.save()
            return redirect('cgpa:student_add')
    else:
        form = StudentForm
    context = {'form':form}
    return HttpResponse(template.render(context, request))

def student_home(request):
    if not Student.objects.filter(user=request.user).exists():
        return redirect('cgpa:student_add')
    template = loader.get_template('cgpa/student_home.html')
    student = Student.objects.get(user=request.user)
    context = { 'student' : student }
    return HttpResponse(template.render(context, request))

def student_edit(request,student_id):
    template = loader.get_template('cgpa/student_edit.html')
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('cgpa:student_home')
    else:
        form = StudentForm(instance=student)
    context = {'form':form}
    return HttpResponse(template.render(context, request))

def student_delete(request,student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('cgpa:student_home')


#...........course.......................
def course_add(request):
    if not Student.objects.filter(user=request.user).exists():
        return redirect('cgpa:student_add')
    template = loader.get_template('cgpa/course_add.html')
    student = Student.objects.get(user=request.user)
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.department = student.department
            obj.university = student.university
            obj.save()
            grade_point= request.POST.get('grade_point')
            if grade_point:
                data = {
                 'grade_point':grade_point,
                 'user':request.user,
                 'course':obj,
                  }
                cform=Result(**data)
                cform.save()
            return redirect('cgpa:course_add')
    else :
        form = CourseForm
    context = {'form':form, 'student': student }
    return HttpResponse(template.render(context, request))

def course_home(request):
    if not Student.objects.filter(user=request.user).exists():
        return redirect('cgpa:student_add')
    template = loader.get_template('cgpa/course_home.html')
    course = Course.objects.all()
    student = Student.objects.get(user=request.user)
    context = { 'course' : course ,'student':student}
    return HttpResponse(template.render(context, request))

def course_edit(request,course_id):
    template = loader.get_template('cgpa/course_edit.html')
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('cgpa:course_home')
    else:
        form = CourseForm(instance=course)
    context = {'form':form}
    return HttpResponse(template.render(context, request))

def course_delete(request,course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('cgpa:course_home')

#...........result.......................
def result_add(request):
    if not Student.objects.filter(user=request.user).exists():
        return redirect('cgpa:student_add')
    template = loader.get_template('cgpa/result_add.html')
    if request.method == 'POST':
        form = ResultForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            # form.save()
            return redirect('cgpa:result_add')
    else:
        form = ResultForm
    context = {'form':form}
    return HttpResponse(template.render(context, request))

def result_home(request):
    if not Student.objects.filter(user=request.user).exists():
        return redirect('cgpa:student_add')    
    template = loader.get_template('cgpa/result_home.html')
    result = Result.objects.all();
    context = { 'result' : result }
    return HttpResponse(template.render(context, request))

def result_edit(request,result_id):
    template = loader.get_template('cgpa/result_edit.html')
    result = Result.objects.get(id=result_id)
    if request.method == 'POST':
        form = ResultForm(request.POST, request.FILES, instance=result)
        if form.is_valid():
            form.save()
            return redirect('cgpa:result_home')
    else:
        form = ResultForm(instance=result)
    context = {'form':form}
    return HttpResponse(template.render(context, request))

def result_delete(request,result_id):
    result = Result.objects.get(id=result_id)
    result.delete()
    return redirect('cgpa:result_home')
