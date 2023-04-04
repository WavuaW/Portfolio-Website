import random
from user.models import User
from django.db import models
from authentication.models import (Shipment,
                                ShippingTo,
                               ShippingFrom)


def generate_tracking_no(size=12, chars='012345678912'):
       return ''.join(random.choice(chars) for _ in range(size))


class Tracking(models.Model):
    tracking_no = models.CharField(max_length=12, default=generate_tracking_no(),unique=True)
    tracking_description = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True, blank=True)
    timestamps = models.DateTimeField(auto_now=True)
    quantity = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, null=True, related_name="shipment_key")
    shipping_to = models.ForeignKey(ShippingTo, on_delete=models.CASCADE, null=True, related_name="shippingto_key")
    shipping_from = models.ForeignKey(ShippingFrom, on_delete=models.CASCADE, null=True, related_name="shippingfrom_key")
    delivered = models.BooleanField(default=False)
    status = models.CharField(max_length=100, null=True)
    estdeliveryDate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["location"]


    def __str__(self) -> str:
        return self.location