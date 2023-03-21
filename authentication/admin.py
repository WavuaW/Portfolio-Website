from django.contrib import admin
from .models import (Country,Shipment, 
                     ShippingFrom,State, 
                     ShippingTo, City)


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


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["name", "sortname", "phoneCode"]
    search_fields = ["name"]
    ordering = ["name"]


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]
    search_fields = ["name"]
    ordering = ["name"]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name", "state"]
    search_fields = ["name"]
    ordering = ["name"]