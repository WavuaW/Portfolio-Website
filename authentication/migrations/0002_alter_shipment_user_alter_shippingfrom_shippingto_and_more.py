# Generated by Django 4.1.6 on 2023-03-16 00:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shippingfrom',
            name='shippingto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shippingfrom', to='authentication.shippingto'),
        ),
        migrations.AlterField(
            model_name='shippingto',
            name='shipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shippingto', to='authentication.shipment'),
        ),
    ]