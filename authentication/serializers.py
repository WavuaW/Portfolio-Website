from rest_framework import serializers
from .models import Shipment, ShippingTo, ShippingFrom



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
