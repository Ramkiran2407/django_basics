from django.shortcuts import render
from django.http import HttpResponse
from app.models import UserRegister, UserLogin, EmployeeRegister, EmployeeLogin, PizzaMenu, OrderDetails, Topping, PaymentDetails
import jwt
from datetime import datetime,timedelta
from django.views.decorators.csrf import csrf_exempt


from django.http import JsonResponse
import json

#In built serializers.
from django.core import serializers
#serializers.serializer


#Function based rest_framework  by using decorator
from rest_framework.decorators import api_view


from rest_framework.response import Response

from .decorator import unauthenticated_user, allowed_users


#Create your views here.

@csrf_exempt
def employee_login(request):
    employee_details = request.POST.get('email')
    token = jwt.encode({'user':employee_details,
    'exp': datetime.utcnow() + timedelta(seconds = 35)}, 'secret_key').decode('utf-8')
    EmployeeLogin(email_id=login_details, token= token).save()
    return HttpResponse('Employee logged in successfully')


@csrf_exempt
def userlogin(request):
    login_details = request.POST.get('email')
    token = jwt.encode({'user':login_details,
    'exp': datetime.utcnow() + timedelta(seconds = 35)}, 'secret_key').decode('utf-8')
    UserLogin(email_id=login_details, token= token).save()
    return HttpResponse('user logged in successfully')



@csrf_exempt
def pizza_menu(request):
    if request.method == 'GET':
        data = PizzaMenu.objects.values('pizza_mania').distinct()
        menu = {"pizza": []}
        for a in data:
            print(a['pizza_mania'])
            menu['pizza'].append(a['pizza_mania'])
        return JsonResponse(menu)
    if request.method == 'POST':
        selected_pizza = request.POST.get('pizza_name')
        pizza_details = PizzaMenu.objects.filter(pizza_mania=selected_pizza)
        size_price = {'Please select Size': []}     
        for a in pizza_details:
            size_price['Please select Size'].append({selected_pizza: {"size":a.size, 'cost': a.price}})
        return HttpResponse(json.dumps(size_price))


@csrf_exempt
def order_pizza(request):
    if request.method == 'POST':
        selected_pizza = request.POST.get('pizza_name')
        pizza_size = request.POST.get('size')
        about_to_order = PizzaMenu.objects.values('price').filter(pizza_mania=selected_pizza,size=pizza_size)
        for _ in about_to_order:
            price = {"Please confirm your order": {'price': _['price']}}
        return HttpResponse(json.dumps(price))


#without using restframe work if we wanna make a API and its call we use decorator @api_view


@api_view(['GET','POST'])
def sample(request):
    return Response({'a':'a'})


@allowed_users(allowed_roles= ['kiran'])
@unauthenticated_user
def live(request):
    return HttpResponse("Welcome to live application !")