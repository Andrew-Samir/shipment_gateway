import imp
from api.models import shipment
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from django.db import transaction
from ..serializers import ShipmentSerializer, ShipmentCreateSerializer, ShipmentUpdateSerializer
from ..utils._init_ import SuccessResponse, ErrorHelper, ErrorResponse
from ..repos import ShipmentRepo

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
    
    # This endpoint to cancel courier or to update shipment status
    def update_shipment(self, request: Request, id: int):
        with transaction.atomic():
            # Get User
            shipment = ShipmentRepo().get_shipment(id)
            if shipment is None: return ErrorResponse([ErrorHelper.NOT_FOUND()], status.HTTP_404_NOT_FOUND, request)

            # Update User
            serializer = ShipmentUpdateSerializer(shipment, data=request.data, context={ 'request': request })
            if not serializer.is_valid():
                return ErrorResponse([ErrorHelper.VALIDATION_ERROR(serializer.errors)], status.HTTP_422_UNPROCESSABLE_ENTITY, request)
            shipment = serializer.save()

        # Return User
        serializer = ShipmentSerializer(shipment, context={ 'request': request })
        return SuccessResponse(serializer.data)

    def get_shipment_status(self, request: Request, id: int):
        
        ## To-do: Get Courier status after integration with aramex
        shipment = ShipmentRepo().get_shipment(id)
        if shipment is None: return ErrorResponse([ErrorHelper.NOT_FOUND()], status.HTTP_404_NOT_FOUND, request)

        return SuccessResponse(shipment.status)

        pass