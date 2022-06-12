from ._base_model import BaseModel
from django.db import models

Shipment_StatusChoises = [
    ('processing', 'shipment is processing.'),
    ('in_transit', 'Shipment in transit.'),
    ('shipped', 'Shipment completed.')
]

Shipment_ServiceTypesChoises = [
    ('same_day', 'Shipped by 10:30 am, delivery by 5 pm.'),
    ('next_day', 'Guaranteed shipment next day by 5 pm.'),
    ('express', 'Picked up in one hour, shipped in three hours.'),
    ('super_rush', 'Pickup within one hour, directly shipped.'),
]

class Shipment(BaseModel):
    courier = models.ForeignKey('Courier', on_delete=models.SET_NULL, null=True, related_name='shipment_courier')
    product = models.ForeignKey('Product', on_delete=models.DO_NOTHING, null=True, related_name='shipment_product')
    sender = models.ForeignKey('User', on_delete=models.DO_NOTHING, null=True, related_name='shipment_sender')
    reciever = models.ForeignKey('User', on_delete=models.DO_NOTHING, null=True, related_name='shipment_reciever')
    pickup_country =  models.CharField(null=True, max_length=150)
    destination_country =  models.CharField(null=True, max_length=150)
    service_type = models.CharField(max_length=255, null=True, choices=Shipment_ServiceTypesChoises)
    status = models.CharField(max_length=255, choices=Shipment_StatusChoises, default=Shipment_StatusChoises[0][0])
    label = models.ForeignKey('ShipmentLabel', null=True, on_delete=models.DO_NOTHING, related_name='shipment_label')
    description = models.TextField(default='')
    cost = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    shipment_canceled = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "shipment"
