from django.shortcuts import render
from .models import Book_info
from .models import Catagory
from .forms import CatagoryForm
from .forms import BookAddForm
from django.shortcuts import redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
# Create your views here.

@api_view(['GET'])
def post_collection(request):
    if request.method == 'GET':
        posts = Book_info.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def post_element(request, pk):
    try:
        post = Book_info.objects.get(pk=pk)
    except Book_info.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
#....................

def book_home(request):
    book = Book_info.objects.all();
    context = { 'book' : book }
    return render(request,'book_info/book_home.html',context)

def book_detail(request,book_id):
    book=Book_info.objects.get(id=book_id)
    return render(request,'book_info/book_detail.html',{'book':book})


def catagory_add(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CatagoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('catagory_add')
        else :
            form = CatagoryForm
        return render(request, 'book_info/catagory_add.html', {'form':form})


def book_add(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = BookAddForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('book_add')
        else:
            form = BookAddForm
        return render(request,'book_info/book_add.html', {'form':form})


def book_edit(request,book_id):
    if request.user.is_superuser:
        book = Book_info.objects.get(id=book_id)
        if request.method == 'POST':
            form = BookAddForm(request.POST, request.FILES, instance=book)
            if form.is_valid():
                form.save()
                return redirect('book_home')
        else:
            form = BookAddForm(instance=book)
        return render(request, 'book_info/book_edit.html', {'form':form})


def book_delete(request,book_id):
    if request.user.is_superuser:
        books = Book_info.objects.get(id=book_id)
        books.delete()
        return redirect('book_home')

def catagory_home(request):
    catagory = Catagory.objects.all()
    return render(request, 'book_info/catagory_home.html',{'catagory':catagory})

def catagory_detail(request,catagory_id):
    catagory = Catagory.objects.get(id=catagory_id)
    book = Book_info.objects.filter(catagory=catagory)
    context = {
    'catagory':catagory,
    'book':book,
    }
    return render(request, 'book_info/catagory_detail.html', context)
