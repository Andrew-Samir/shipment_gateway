import imp
from api.models import shipment
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from django.db import transaction
from ..serializers import ShipmentSerializer, ShipmentCreateSerializer, ShipmentUpdateSerializer
from ..utils._init_ import SuccessResponse, ErrorHelper, ErrorResponse
from ..repos import ShipmentRepo, CourierRepo
from ..interface import InterfaceMapperFactory
from ..integration import FedexServices

class ShipmentView(ViewSet):
    
    ### Get Shipment ###
    def get_shipment(self, request: Request, id: int):
        shipment = ShipmentRepo().get_shipment(id)
        if shipment is None: return ErrorResponse([ErrorHelper.NOT_FOUND()], status.HTTP_404_NOT_FOUND, request)
        
        # Return User Theme
        serializer = ShipmentSerializer(shipment, context={ 'request': request })
        return SuccessResponse(serializer.data)

    ### Create Shipment ###
    def create_shipment(self, request: Request):
        
        # Create Shipment
        with transaction.atomic():
            serializer = ShipmentCreateSerializer(data=request.data, context={ 'request': request })
            if not serializer.is_valid():
                return ErrorResponse([ErrorHelper.VALIDATION_ERROR(serializer.errors)], status.HTTP_422_UNPROCESSABLE_ENTITY, request)
            shipment = serializer.save()
            if 'courier_id' in request.data and 'courier_id' is not None:
                courier_id = request.data['courier_id']
                courier = CourierRepo().get_courier(courier_id)
            if courier is not None:
                courier = InterfaceMapperFactory().get_courier(courier.name)
            else:
                courier = InterfaceMapperFactory().get_courier('fedex')
            
            ## Choose Courier
            shipment = courier.create_shipment(shipment)
        # Return Shipment
        serializer = ShipmentSerializer(shipment, context={ 'request': request })
        return SuccessResponse(serializer.data)
    
    # This endpoint to cancel courier or to update shipment status manually
    def update_shipment(self, request: Request, id: int):
        with transaction.atomic():
            # Get User
            shipment = ShipmentRepo().get_shipment(id)
            if shipment is None: return ErrorResponse([ErrorHelper.NOT_FOUND()], status.HTTP_404_NOT_FOUND, request)

            if shipment.courier is not None:
                courier = InterfaceMapperFactory().get_courier(shipment.courier.name)
            # Update User
            serializer = ShipmentUpdateSerializer(shipment, data=request.data, context={ 'request': request })
            if not serializer.is_valid():
                return ErrorResponse([ErrorHelper.VALIDATION_ERROR(serializer.errors)], status.HTTP_422_UNPROCESSABLE_ENTITY, request)
            data = serializer.validated_data
            if 'cancel_shipment' in data and data['cancel_shipment']:
                is_shipment_cancelled = courier.cancel_shipment(shipment.tracking_number)
                if not is_shipment_cancelled:
                    return ErrorResponse([ErrorHelper.VALIDATION_ERROR('Unable to cancel shipment')], status.HTTP_422_UNPROCESSABLE_ENTITY, request)
                shipment.delete()

            shipment = serializer.save()
            # Return User
            serializer = ShipmentSerializer(shipment, context={ 'request': request })
            return SuccessResponse(serializer.data)

    ## get shipment status 
    def get_shipment_status(self, request: Request, id: int):
        shipment = ShipmentRepo().get_shipment(id)
        if shipment is None: return ErrorResponse([ErrorHelper.NOT_FOUND()], status.HTTP_404_NOT_FOUND, request)
        if shipment.courier is not None:
            courier = InterfaceMapperFactory().get_courier(shipment.courier.name)
        system_status = courier.get_status(shipment.tracking_number)
        return SuccessResponse(system_status)

    ## TODO
    # Cron job to map dynamically shipment status from real courier
    # and store it in db