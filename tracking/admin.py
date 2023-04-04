from django.contrib import admin
from  . models import Tracking


@admin.register(Tracking)
class TrackingAdmin(admin.ModelAdmin):
    list_display = ["tracking_no", "location", "quantity",]
    ordering = ["tracking_no"]
    search_fields = ["location"]