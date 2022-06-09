from rest_framework import serializers
from ..serializers import UserSerializer, ShipmentLabelSerializer, ProductSerializer
from ..models import User, Product, Shipment
from ..repos import UserRepo, ProductRepo
from django.core.exceptions import ValidationError

## Get Serializer ##

class ShipmentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    product = ProductSerializer(read_only=True)
    sender = UserSerializer(read_only=True)
    reciever = UserSerializer(read_only=True)
    origin =  serializers.CharField(read_only=True)
    destination = serializers.CharField(read_only=True)
    service_type = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
    label = ShipmentLabelSerializer(read_only=True)
    description = serializers.CharField(read_only=True)
    cost = serializers.DecimalField(10, decimal_places=3, read_only=True)

    date_picked_up = serializers.DateTimeField(read_only=True)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

## Create Serializer ##

class ShipmentCreateSerializer(serializers.Serializer):
    product_id = serializers.CharField(allow_null=True, min_length=1, max_length=150, help_text='Product ID.')
    sender_id = serializers.IntegerField(min_value=1, help_text='Sender ID.')
    reciever_id = serializers.IntegerField(min_value=1, help_text='Sender ID.')
    pickup_country =  serializers.CharField(required=False, max_length=150, help_text='Pickup Country.')
    destination_country =  serializers.CharField(required=False, max_length=150, help_text='Destination Country.')
    description = serializers.CharField(required=False, max_length=150, help_text='Description.')

    sender: User
    reciever: User
    product: Product

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sender = None
        self.reciever = None
        self.product = None

    def validate_sender_id(self, sender_id):
        self.sender = UserRepo().get_user(sender_id)
        if self.sender is None: raise ValidationError('User not found.')
        return sender_id
    
    def validate_reciever_id(self, reciever_id):
        self.reciever = UserRepo().get_user(reciever_id)
        if self.reciever is None: raise ValidationError('User not found.')
        return reciever_id

    def validate_product_id(self, prodcut_id):
        self.product = ProductRepo().get_product(prodcut_id)
        if self.product is None: raise ValidationError('Product not found.')
        return prodcut_id

    def create(self, validated_data):
        shipment = Shipment.objects.create(**validated_data)
        return shipment

    class Meta:
        ref_name = None
