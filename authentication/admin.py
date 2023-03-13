from django.contrib import admin
from .models import Shipment, ShippingFrom, ShippingTo


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ["user", "shipment_name", "shipping_type"]
    ordering = ["user"]
    search_fields = ["shipment_name"]



@admin.register(ShippingTo)
class ShippingToAdmin(admin.ModelAdmin):
    list_display = ["shipment", "receiver_name", 
                    "receiver_company", "receiver_country", 
                    "receiver_address", "state", "city"]
    ordering = ["shipment"]
    search_fields = ["receiver_name"]


@admin.register(ShippingFrom)
class ShippingFromAdmin(admin.ModelAdmin):
    list_display = ["shippingto", "sender_name", 
                    "sender_company", "sender_country", 
                    "sender_address", "state", "city"]
    ordering = ["shippingto"]
    search_fields = ["sender_name"]