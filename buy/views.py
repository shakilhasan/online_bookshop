from django.shortcuts import render
from .models import Card
from .models import Order
from .forms import CardForm
from .forms import OrderForm
from book_info.models import Book_info
from django.shortcuts import redirect
from django.contrib.auth.models import User
# Create your views here.

def card_add(request):
    if request.user.is_authenticated:
        name= request.user.username
        u= User.objects.get(username=name)
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        amount= request.POST.get('amount')
        book = Book_info.objects.get(id=book_id)
        data = {
         'user':u,
         'book':book,
         'amount':amount,
         #'order':1,
          }
        form=Card(**data)
        form.save()
    return redirect('book_home')

def card_home(request):
    if request.user.is_authenticated:
        name= request.user.username
        u=User.objects.get(username=name)
    book = Card.objects.values('book').filter(user=u)
    card = Card.objects.filter(user=u)
    t_price=0
    return render(request,'card/card_home.html',{'card':card,'t_price':t_price,})
    # return render(request,'book_info/book_home.html',{ 'book' : book })
def order(request):
    order = Order.objects.all()
    u = User.objects.all()
    return render(request,'card/order.html',{'order':order,'u':u})

def order_detail(request,order_id):
    order = Order.objects.get(id=order_id)
    card = Card.objects.filter(order=order)
    return render(request,'card/order_detail.html',{'card':card,'order':order})

def order_delete(request,order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return redirect('order')


def card_delete(request,card_id):
    card = Card.objects.get(id=card_id)
    card.delete()
    if request.user.is_authenticated:
        name= request.user.username
        user=User.objects.get(username=name)
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
    if request.user.is_authenticated:
        name= request.user.username
        u=User.objects.get(username=name)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        form.save()
        #last=len(list(Order.objects.all()))
        li=list(Order.objects.values('id'))
        last=li[0]['id']
        Order.objects.filter(id=last).update(user=u)
        order=Order.objects.last()
        Card.objects.filter(sold='False').filter(user=u).update(order=order)
        return redirect('payment')
    else:
        form = OrderForm()
        return render(request, 'card/shipping.html', {'form':form})
def payment(request):
    return render(request,'card/payment.html')
