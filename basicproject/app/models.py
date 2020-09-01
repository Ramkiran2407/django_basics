from django.db import models

# Create your models here.

class UserRegister(models.Model):
    name = models.CharField("Name", max_length=50, null= False)
    age = models.IntegerField("Age")
    email = models.EmailField("Email", max_length=50, null= False, primary_key= True)
    contact = models.CharField("contact",max_length=50,  null = False)
    password = models.CharField("password", max_length=25, null= False)
    address = models.CharField("address", max_length=100)


class UserLogin(models.Model):
    email = models.ForeignKey("UserRegister", on_delete=models.CASCADE, null = True)
    token = models.CharField("token", max_length=200)
    time_and_date_track = models.DateTimeField(auto_now_add = True)


class EmployeeRegister(models.Model):
    id = models.AutoField("id", primary_key= True)
    name = models.CharField("Name", max_length=50, null= False)
    age = models.IntegerField("Age")
    email = models.EmailField("Email")
    contact = models.CharField("contact",max_length=50,  null = False)
    password = models.CharField("password", max_length=25, null= False)
    vehicle_number = models.CharField("vehicle_number", max_length=50)
    rc_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)


class EmployeeLogin(models.Model):
    email = models.ForeignKey("EmployeeRegister", on_delete=models.CASCADE)
    token = models.CharField("token", max_length=100)


class PizzaMenu(models.Model):
    pizza_mania = models.CharField("pizza_mania", null= False, max_length=25)
    size = models.CharField("pizza_mania", null= False, max_length=25)
    price = models.IntegerField('price', null = False)
    

class OrderDetails(models.Model):
    order_id  = models.ForeignKey(
        'PaymentDetails',
        on_delete=models.CASCADE,
    )
    delivery_address = models.CharField("delivery_address", null=False, max_length=25)
    tracking_id = models.IntegerField('tracking_id', primary_key= True)
    delivery_person = models.CharField('delivery_person', null= False, max_length=25)


class Topping(models.Model):
    chilli_flakes = models.IntegerField("chilli_flakes", null = True)
    organic_seasons = models.IntegerField("organic_seasons", null= True)
    cheese_cubes = models.IntegerField('cheese_cubes')
    garlic_cheese = models.IntegerField('garlic_cheese')
    black_olives = models.IntegerField("black_olives")
    other_instructions = models.CharField("other_instructions", max_length=25)


    # def __str__(self):
    #     return " ".format()


class PaymentDetails(models.Model):
    order_id  = models.IntegerField("order_id", primary_key= True)
    payment_method = models.CharField("payment_method", null= False, max_length=25)


