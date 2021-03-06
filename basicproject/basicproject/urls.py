"""basicproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import *
from app.classviews import ToppingAddOns, EmployeeRegister, UserViewSet

from django.conf import settings
from django.conf.urls.static import static



# from rest_framework import routers 

# router = routers.DefaultRouter() 

# router.register(r'emp_reg', RegisterEmployees) 

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('employee_login/', employee_login),
    # path('user_login/', userlogin),
    # path('pizza_menu/', pizza_menu),
    # path('order_pizza/', order_pizza )
    
    path('', include('app.urls')),
    
    path('addons/', ToppingAddOns.as_view()),
    
    path('register/', include('app.rest_framework_urls')),
    

    path('point/', EmployeeRegister.as_view({'get': "send_the_mail"})),


    # path('viewset/', UserViewSet.as_view())


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + router.urls
