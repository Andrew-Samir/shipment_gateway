from rest_framework import serializers

#####################
## Get Serializer ###
#####################

class CourierSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    can_cancel_shipment = serializers.BooleanField(read_only=True)
