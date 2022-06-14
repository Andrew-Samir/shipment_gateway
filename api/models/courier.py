from django.db import models

class Courier(models.Model):
    name = models.CharField(max_length=128, verbose_name='Courier Name')
    can_cancel_shipment = models.BooleanField(default=True)

    class Meta:
        db_table = "courier"
