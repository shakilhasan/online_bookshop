from django.shortcuts import render
from .models import Card
from .models import Order
from .forms import CardForm
from .forms import OrderForm
from book_info.models import Book_info
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.template import loader
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect

from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.decorators import login_required
# Create your views here.

@api_view()
def check_order(request, order_number):
    is_exist = Order.objects.filter(id=order_number).exists()
    #return JsonResponse({'status': is_exist})
    return Response({'status': is_exist})

def checking(request):
    template = loader.get_template('buy/check_order.html')
    context = {}
    return HttpResponse(template.render(context, request))

#............
@login_required(login_url='/login/')
def card_add(request, book_id):
    if request.user.is_authenticated:
        name= request.user.username
        u= User.objects.get(username=name)
    #if request.method == 'POST':
    #book_id = request.POST.get('book_id')
    #amount= request.POST.get('amount')
    book = Book_info.objects.get(id=book_id)
    data = {
     'user':u,
     'book':book,
     #'amount':amount,
      }
    form=Card(**data)
    form.save()
    return redirect('book_home')

def card_home(request):
    template = loader.get_template('buy/card_home1.html')
    if request.user.is_authenticated:
        name= request.user.username
        u=User.objects.get(username=name)
    card = Card.objects.filter(user=u)
    context ={'card':card}
    return HttpResponse(template.render(context, request))

def card_update(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        card_id = request.POST.get('card_id')
        Card.objects.filter(id=card_id).update(amount=amount)
        return redirect('card_home')

def order(request):
    template = loader.get_template('buy/order.html')
    if request.user.is_superuser:
        order = Order.objects.all()
        u = User.objects.all()
        context = {'order':order,'u':u}
        return HttpResponse(template.render(context, request))

def order_detail(request,order_id):
    template = loader.get_template('buy/order_detail.html')
    if request.user.is_superuser:
        order = Order.objects.get(id=order_id)
        card = Card.objects.filter(order=order)
        context = {'card':card,'order':order}
        return HttpResponse(template.render(context, request))

def order_delete(request,order_id):
    if request.user.is_superuser:
        order = Order.objects.get(id=order_id)
        order.delete()
        return redirect('order')

def card_delete(request,card_id):
    if request.user.is_authenticated:
        name= request.user.username
        user=User.objects.get(username=name)
        card = Card.objects.get(id=card_id)
        card.delete()
        if user.is_superuser:
            return redirect('order')
        else:
            return redirect('card_home')

def checkout(request):
    if request.user.is_authenticated:
        name= request.user.username
        u=User.objects.get(username=name)
        Card.objects.filter(user=u).update(sold='True')
        return redirect('book_home')

def shipping(request):
    template = loader.get_template('buy/shipping.html')
    if request.user.is_authenticated:
        name= request.user.username
        u=User.objects.get(username=name)
        card = Card.objects.filter(user=u)
    if request.method == 'POST':
        total = request.POST.get('total')
        form = OrderForm(request.POST)
        form.save()
        last=str(Order.objects.latest('id'))
        Order.objects.filter(id=last).update(user=u)
        Order.objects.filter(id=last).update(total=total)
        order=Order.objects.last()
        Card.objects.filter(sold='False').filter(user=u).update(order=order)
        return redirect('payment')
    else:
        form = OrderForm()
        context = {'form':form,'card':card}
        return HttpResponse(template.render(context, request))

def payment(request):
    template = loader.get_template('buy/payment.html')
    if request.user.is_authenticated:
        context = {}
        return HttpResponse(template.render(context, request))
