
from django.urls import path
from app.views import *

urlpatterns = [
    path('employee_login/', employee_login),
    path('user_login/', userlogin),
    path('pizza_menu/', pizza_menu),
    path('order_pizza/', order_pizza ),
    path('sample_rest/', sample),
]