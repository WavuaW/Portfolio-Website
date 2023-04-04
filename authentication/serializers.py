from rest_framework import serializers
from .models import (Shipment, 
                     ShippingTo, 
                     ShippingFrom,
                     Country,State,City)



class ShipmentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Shipment
        fields = ['id','name', 
                'shipping_type', 'container_no',
                'length', 'width', 'heigh', 'weight', 
                'goodsType', 'additional_info']


    def create(self, validated_data):
        shipment = Shipment.objects.create(**validated_data)
        shipment.save()
        return shipment


class ShippingToSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShippingTo
        fields = [
            'id',"receiver_name","receiver_company",
            "receiver_country","receiver_address",
            "receiver_address_2","receiver_address_3",
            "postal_code","state","city","email","phone_number",
            "country_code""taxt_no","shipment"
        ]

    def create(self, validated_data):
        shipment = Shipment.objects.create(**validated_data)
        shipment.save(self)
        return shipment
    
    

class ShippingFromSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShippingFrom
        fields =  [
            'id','sender_name','sender_company', 
            'sender_country','shipment','sender_address',
            'sender_address_2','sender_address_3','postal_code',
            'state','city','email','phone_number','country_code',
            'taxt_no','vat_no'
        ]

    def create(self, validated_data):
        shipment = Shipment.objects.create(**validated_data)
        shipment.save(self)
        return shipment
    


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields= "__all__"


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields= "__all__"


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields= "__all__"