from ._base_model import BaseModel
from django.db import models

class Product(BaseModel):
    name = models.CharField(max_length=255, null=True)
    amount = models.IntegerField(null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=1)
    origin = models.CharField(max_length=255, default='')

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "product"
