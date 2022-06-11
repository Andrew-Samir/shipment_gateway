from ._base_model import BaseModel
from django.db import models

class ShipmentLabel(models.Model):
    product = models.ForeignKey('Product', on_delete=models.DO_NOTHING, null=True, related_name='shipment_label_product')
    sender = models.ForeignKey('User', on_delete=models.DO_NOTHING, null=True, related_name='shipment_label_sender')
    reciever = models.ForeignKey('User', on_delete=models.DO_NOTHING, null=True, related_name='shipment_label_reciever')
    pickup_country =  models.CharField(max_length=150)
    destination_country =  models.CharField(max_length=150)
    amount = models.IntegerField(null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=3)
    comment = models.TextField(default='')
    cost = models.DecimalField(max_digits=10, decimal_places=3)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "shipment_label"
