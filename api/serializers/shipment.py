from rest_framework import serializers
from shipment_gateway.settings import PRICE_PER_KG
from ..serializers import UserSerializer, ShipmentLabelSerializer, ProductSerializer, CourierSerializer
from ..models import User, Product, Shipment, ShipmentLabel, Courier, Shipment_StatusChoises
from ..repos import UserRepo, ProductRepo, CourierRepo
from django.core.exceptions import ValidationError
from django.db.models import Q

## Get Serializer ##

class ShipmentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    courier = CourierSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    sender = UserSerializer(read_only=True)
    reciever = UserSerializer(read_only=True)
    pickup_country =  serializers.CharField(read_only=True)
    destination_country = serializers.CharField(read_only=True)
    service_type = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
    label = ShipmentLabelSerializer(read_only=True)
    description = serializers.CharField(read_only=True)
    cost = serializers.DecimalField(10, decimal_places=3, read_only=True)
    tracking_number = serializers.IntegerField(read_only=True)
    shipment_canceled = serializers.BooleanField(read_only=True)
    date_picked_up = serializers.DateTimeField(read_only=True)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

## Create Serializer ##

class ShipmentCreateSerializer(serializers.Serializer):
    courier_id = serializers.CharField(allow_null=True, min_length=1, max_length=150, help_text='Courier ID.')
    product_id = serializers.CharField(allow_null=True, min_length=1, max_length=150, help_text='Product ID.')
    sender_id = serializers.IntegerField(min_value=1, help_text='Sender ID.')
    reciever_id = serializers.IntegerField(min_value=1, help_text='Reciever ID.')
    pickup_country =  serializers.CharField(max_length=150, help_text='Pickup Country.')
    destination_country =  serializers.CharField(max_length=150, help_text='Destination Country.')
    description = serializers.CharField(required=False, max_length=150, help_text='Description.')

    courier: Courier
    sender: User
    reciever: User
    product: Product

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sender = None
        self.reciever = None
        self.product = None
        self.courier = None

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

    def validate_courier_id(self, courier_id):
        self.courier = CourierRepo().get_courier(courier_id)
        if self.courier is None: raise ValidationError('Courier not found.')
        return courier_id

    def create(self, validated_data):
        
        validated_data['cost'] = (self.product.amount*self.product.weight) * PRICE_PER_KG
        shipment = Shipment.objects.create(**validated_data)
        
        del validated_data['courier_id']
        shipment.label = ShipmentLabel.objects.create(**validated_data, weight=self.product.weight, amount=self.product.amount)
        
        shipment.save()
        return shipment

    class Meta:
        ref_name = None


## Update Serializer ##
class ShipmentUpdateSerializer(serializers.Serializer):
    cancel_shipment = serializers.BooleanField(required=False, help_text='cancel shipment.')
    status = serializers.CharField(required=False, help_text='status.')

    def validate_cancel_shipment(self, cancel_shipment):
        if cancel_shipment:
            if self.instance.courier is not None and not self.instance.courier.can_cancel_shipment:
                raise ValidationError('Unable to cancel shipment')
            if self.instance.shipment_canceled:
                raise ValidationError('Shipment already canceled')
        return cancel_shipment
    
    def validate_status(self, status):
        if status is not None:
            if status not in [Shipment_StatusChoises[0][0], Shipment_StatusChoises[1][0], Shipment_StatusChoises[2][0]]:
                raise ValidationError('Invalid Status, status should be processing , in transit or shipped')
        return status

    def update(self, instance, validated_data):
        instance.shipment_canceled = validated_data.get('cancel_shipment', instance.shipment_canceled)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

    class Meta:
        ref_name = None

