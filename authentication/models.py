from django.db import models
from user.models import User


class Shipment(models.Model):   
    shipment_name = models.CharField(max_length=100)
    shipping_type = models.CharField(max_length=100)
    container_no = models.IntegerField()
    length = models.IntegerField()
    width = models.IntegerField()
    heigh = models.IntegerField()
    weight = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shipment')
    goodsType = models.CharField(max_length=100, blank=True)
    additional_info	= models.CharField(max_length=100, blank=True)
    pickup_timestamp = models.DateTimeField(auto_now=True,null=True)
    arrival_timestamp = models.DateTimeField(auto_now=True,null=True)
   


    class Meta:
        ordering = ["shipment_name"]


    def __str__(self) -> str:
        return self.shipment_name


class ShippingTo(models.Model):
    receiver_name = models.CharField(max_length=100)
    receiver_company = models.CharField(max_length=100)
    receiver_country = models.CharField(max_length=100)
    receiver_address =  models.CharField(max_length=100)
    receiver_address_2 =  models.CharField(max_length=100)
    receiver_address_3 =  models.CharField(max_length=100)
    postal_code = models.BigIntegerField(null = True)
    state =  models.CharField(max_length=100, blank=True)
    city =  models.CharField(max_length=100, blank=True)
    email =  models.CharField(max_length=100)
    phone_number = models.BigIntegerField(null = True)
    country_code = models.BigIntegerField(null = True)
    taxt_no = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shippingto')
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name='shippingto')
    
    class Meta:
        ordering = ["receiver_name"]


    def __str__(self) -> str:
        return self.receiver_name
    
    

class ShippingFrom(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_company = models.CharField(max_length=100)
    sender_country = models.CharField(max_length=100)
    sender_address =  models.CharField(max_length=100)
    sender_address_2 =  models.CharField(max_length=100)
    sender_address_3 =  models.CharField(max_length=100)
    postal_code = models.BigIntegerField(null= True)
    state =  models.CharField(max_length=100, blank=True)
    city =  models.CharField(max_length=100, blank=True)
    email =  models.CharField(max_length=100)
    phone_number = models.BigIntegerField(null = True)
    country_code = models.BigIntegerField(null= True)
    taxt_no = models.BigIntegerField(null= True)
    vat_no = models.IntegerField(null= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shippingfrom')
    shippingto = models.ForeignKey(ShippingTo, on_delete=models.CASCADE, related_name='shippingfrom')
    

    class Meta:
        ordering = ["sender_name"]


    def __str__(self) -> str:
        return self.sender_name



class Country(models.Model):
    sortname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phoneCode = models.IntegerField()
    
    def __str__(self) -> str:
        return self.sortname
    

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name