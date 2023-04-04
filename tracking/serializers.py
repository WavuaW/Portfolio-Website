from rest_framework import serializers
from . models import Tracking
from authentication.models import (
                                Shipment,
                                ShippingTo,
                               ShippingFrom)
from authentication.serializers import (
                                    ShipmentSerializers,
                                    ShippingToSerializers,
                                    ShippingFromSerializers
                                    )




class TrackingSerializer(serializers.ModelSerializer):
    shipments = serializers.SerializerMethodField()                        
    shippingtos = serializers.SerializerMethodField()
    shippingfroms = serializers.SerializerMethodField()
    
    class Meta:
        model = Tracking
        fields= [
            'id','tracking_no', 'tracking_description','user',
            'location', 'timestamps', 'quantity','delivered',
            'status', 'estdeliveryDate', 'shipment', 'shippingtos',
            'shipping_to','shipments','shipping_from', 'shippingfroms'
        ]
                
        read_only_fields = ('tracking_no',)

    def get_shipments(self, obj):
        try:

            shipment = Shipment.objects.get(shipment_key__tracking_no=obj.tracking_no) 
            print(shipment)
            shipment_data = ShipmentSerializers(shipment, context=self.context, many=False).data
            return shipment_data
        except Shipment.DoesNotExist:
            return None
       

    def get_shippingtos(self, obj):
        try:
            shippingto =  ShippingTo.objects.get(shippingto_key__tracking_no=obj.tracking_no) 
            shippingto_data = ShippingToSerializers(shippingto, context=self.context, many=False).data
            return shippingto_data
        except ShippingTo.DoesNotExist:
            return None


    def get_shippingfroms(self, obj):
        try:
            shippingfrom =  ShippingFrom.objects.get(shippingfrom_key__tracking_no=obj.tracking_no) 
            shippingfrom_data = ShippingFromSerializers(shippingfrom, context=self.context, many=False).data
            return shippingfrom_data
        except ShippingFrom.DoesNotExist:
            return None