from django.shortcuts import render
from .models import Book_info
from .models import Catagory
from .forms import CatagoryForm
from .forms import BookAddForm
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
from .serializers import PostSerializer
from .serializers import CatagorySerializer
from functools import wraps


def auth(f):
    @wraps(f)
    def decorated(request,*arg, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/login')
        return f(request,*arg,**kwargs)
    return decorated

def super(f):
    @wraps(f)
    def decorated(request,*arg, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseRedirect('/login')
        return f(request,*arg,**kwargs)
    return decorated
# api.........
@auth
def bookapi(request):
    template = loader.get_template('book_info/bookapi.html')
    context = {}
    return HttpResponse(template.render(context, request))

@api_view(['GET', 'POST'])
def post_collection(request):
    if request.method == 'GET':
        posts = Book_info.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST' and request.user.is_superuser:
        #data = JSONParser().parse(request)
        data = {'name': request.data.get('the_post'), 'author': request.user.pk}
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE'])
def post_element(request, pk):
    try:
        post = Book_info.objects.get(pk=pk)
    except Book_info.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'DELETE' and request.user.is_superuser:
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#..............................
def book_home(request):
    template = loader.get_template('book_info/book_home1.html')
    book = Book_info.objects.all();
    context = { 'book' : book }
    return HttpResponse(template.render(context, request))


def book_detail(request,book_id):
    template = loader.get_template('book_info/book_detail.html')
    book=Book_info.objects.get(id=book_id)
    context = { 'book' : book }
    return HttpResponse(template.render(context, request))

@super
def catagory_add(request):
    template = loader.get_template('book_info/catagory_add.html')
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CatagoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('catagory_add')
        else :
            form = CatagoryForm
        context = {'form':form}
        return HttpResponse(template.render(context, request))

@super
def book_add(request):
    template = loader.get_template('book_info/book_add.html')
    if request.user.is_superuser:
        if request.method == 'POST':
            form = BookAddForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('book_add')
        else:
            form = BookAddForm
        context = {'form':form}
        return HttpResponse(template.render(context, request))

@super
def book_edit(request,book_id):
    template = loader.get_template('book_info/book_edit.html')
    if request.user.is_superuser:
        book = Book_info.objects.get(id=book_id)
        if request.method == 'POST':
            form = BookAddForm(request.POST, request.FILES, instance=book)
            if form.is_valid():
                form.save()
                return redirect('book_home')
        else:
            form = BookAddForm(instance=book)
        context = {'form':form}
        return HttpResponse(template.render(context, request))

@super
def book_delete(request,book_id):
    if request.user.is_superuser:
        books = Book_info.objects.get(id=book_id)
        books.delete()
        return redirect('book_home')

def catagory_home(request):
    template = loader.get_template('book_info/catagory_home.html')
    catagory = Catagory.objects.all()
    context = {'catagory':catagory}
    return HttpResponse(template.render(context, request))

def catagory_detail(request,catagory_id):
    template = loader.get_template('book_info/catagory_detail.html')
    catagory = Catagory.objects.get(id=catagory_id)
    book = Book_info.objects.filter(catagory=catagory)
    context = {
    'catagory':catagory,
    'book':book,
    }
    return HttpResponse(template.render(context, request))
