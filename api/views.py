from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from buy.models import Order
from django.http import JsonResponse

@api_view()
def check_order(request, order_number):
    is_exist = Order.objects.filter(id=order_number).exists()
    #return JsonResponse({'status': is_exist})
    return Response({'status': is_exist})
