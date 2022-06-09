from rest_framework import serializers

#####################
## Get Serializer ###
#####################

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    amount = serializers.IntegerField(read_only=True)
    weight = serializers.DecimalField(5, decimal_places=1, read_only=True)
    origin = serializers.CharField(read_only=True)

    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)