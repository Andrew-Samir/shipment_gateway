from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from django.db import transaction
from ..serializers import ShipmentSerializer, ShipmentCreateSerializer
from ..utils._init_ import SuccessResponse, ErrorHelper, ErrorResponse

class ShipmentView(ViewSet):

    ### Create Shipment ###

    def create_shipment(self, request: Request):
        # Create Shipment
        with transaction.atomic():
            serializer = ShipmentCreateSerializer(data=request.data, context={ 'request': request })
            if not serializer.is_valid():
                return ErrorResponse([ErrorHelper.VALIDATION_ERROR(serializer.errors)], status.HTTP_422_UNPROCESSABLE_ENTITY, request)
            shipment = serializer.save()

        # Return Shipment
        serializer = ShipmentSerializer(shipment, context={ 'request': request })
        return SuccessResponse(serializer.data)