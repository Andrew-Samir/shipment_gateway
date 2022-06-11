from api.models import shipment
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from ..serializers import ShipmentLabelSerializer
from ..utils._init_ import SuccessResponse, ErrorHelper, ErrorResponse
from ..repos import ShipmentRepo

class ShipmentLabelView(ViewSet):

    ### Create Shipment ###

    def get_shipment_label(self, request: Request, id: int):
        # Get Shipment Label
        shipment = ShipmentRepo().get_shipment(id)
        if shipment is None: return ErrorResponse([ErrorHelper.NOT_FOUND()], status.HTTP_404_NOT_FOUND, request)

        # Return Shipment Label
        serializer = ShipmentLabelSerializer(shipment.label, context={ 'request': request })
        return SuccessResponse(serializer.data)