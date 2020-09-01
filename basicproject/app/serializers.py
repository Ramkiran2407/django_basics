from .models import Topping, UserRegister, EmployeeRegister
from rest_framework import serializers

# from django.core import serializers  (serializezr.serialize)
##inbuilt serializers




class ToppingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topping
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRegister
        fields = '__all__'


class EmployeeRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeRegister
        fields = '__all__'