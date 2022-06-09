from rest_framework import serializers

#####################
## Get Serializer ###
#####################

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(read_only=True)
    username = serializers.CharField(read_only=True)
    phone = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)
    company_name = serializers.CharField(read_only=True)
    country = serializers.CharField(read_only=True)
    city = serializers.CharField(read_only=True)
    
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)