from rest_framework import serializers
from shipment_gateway.settings import PRICE_PER_KG
from ..serializers import UserSerializer, ProductSerializer
from ..models import User, Shipment
from ..repos import UserRepo, ProductRepo
from django.core.exceptions import ValidationError

## Get Serializer ##

class ShipmentLabelSerializer(serializers.Serializer):
    product = ProductSerializer(read_only=True)
    sender = UserSerializer(read_only=True)
    reciever = UserSerializer(read_only=True)
    pickup_country =  serializers.CharField(read_only=True)
    destination_country =  serializers.CharField(read_only=True)
    amount = serializers.IntegerField(read_only=True)
    weight = serializers.DecimalField(5, decimal_places=3, read_only=True)
    comment = serializers.CharField(read_only=True)
    cost = serializers.DecimalField(10, decimal_places=3, read_only=True)
    
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)