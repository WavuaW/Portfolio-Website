from rest_framework import serializers
from .models import Shipment, ShippingTo, ShippingFrom



class ShipmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'


class ShippingToSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShippingTo
        fields = '__all__'


class ShippingFromSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShippingFrom
        fields = '__all__'