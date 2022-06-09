from rest_framework import serializers
from ..serializers import UserSerializer

#####################
## Get Serializer ###
#####################

class ShipmentLabelSerializer(serializers.Serializer):
    sender = UserSerializer(read_only=True)
    reciever = UserSerializer(read_only=True)
    origin =  serializers.CharField(read_only=True)
    destination =  serializers.CharField(read_only=True)
    amount = serializers.IntegerField(read_only=True)
    weight = serializers.DecimalField(5, decimal_places=3, read_only=True)
    comment = serializers.CharField(read_only=True)
    cost = serializers.DecimalField(10, decimal_places=3, read_only=True)

    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)
