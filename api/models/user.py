from ._base_model import BaseModel
from django.db import models

class User(BaseModel):
    email = models.EmailField(verbose_name='Email address', max_length=255, unique=True, null=True)
    username = models.CharField(verbose_name='Username', max_length=150, null=True)
    phone = models.CharField(max_length=30, null=True)
    address = models.TextField(default='')
    company_name = models.CharField(max_length=255, null=True)
    country = models.CharField(null=True, max_length=150)
    city = models.CharField(null=True, max_length=150)
    
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = "user"
