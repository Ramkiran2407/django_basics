from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Topping, UserRegister, EmployeeRegister
from .serializers import ToppingSerializer, UserRegisterSerializer, EmployeeRegisterSerializer

## normal views using rest framework
class ToppingAddOns(APIView):
    
    def get(self, request):
        add_ons = Topping.objects.all()
        add_ons = ToppingSerializer(add_ons,  many=True)
        return Response(add_ons.data)


# viewsets using rest frame work
from rest_framework import viewsets

class RegisterEmployees(viewsets.ModelViewSet):
    queryset = UserRegister.objects.all() 
    serializer_class = UserRegisterSerializer



class EmployeeRegister(viewsets.ModelViewSet):
    queryset = EmployeeRegister.objects.all() 
    serializer_class = EmployeeRegisterSerializer 

    def send_the_mail(self, request):
        print("hello")
        return Response("mail sent successfully")


from django.shortcuts import get_object_or_404
class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = UserRegister.objects.all()
        serializer = UserRegisterSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        print("worked")
        queryset = Topping.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ToppingSerializer(user)
        
        return Response(serializer.data)

