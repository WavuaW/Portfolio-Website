from rest_framework import serializers
from .models import (Shipment, 
                     ShippingTo, 
                     ShippingFrom,
                     Country,State,City)



class ShipmentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Shipment
        fields = '__all__'

    def create(self, validated_data):
        shipment = Shipment.objects.create(**validated_data)
        shipment.save()
        return shipment


class ShippingToSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShippingTo
        fields = '__all__'

    def create(self, validated_data):
        shipment = Shipment.objects.create(**validated_data)
        shipment.save(self)
        return shipment
    
    

class ShippingFromSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShippingFrom
        fields = '__all__'

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