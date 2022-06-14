from ..integration import SMSAServices
from ._base_interface_ import ICourier
from ..models import Shipment, Shipment_StatusChoises

SMSA_Shipment_StatusChoises = [
    ('shipment created', 'Shipment created.'),
    ('picked up', 'Shipment pickedup'),
    ('in transit','Shipment in transit'),
    ('Out for Delivery', 'Shipment out for delivery.'),
    ('Delivery order on hand', 'Delivered on hand'),
    ('delivered', 'Shipment completed.')
]

class SMSA(ICourier):
    
    def __init__(self) -> None:
        super().__init__()

    # Create Shipment
    def create_shipment(self, shipment):
        response = SMSAServices().create_shipment(shipment)
        tracking_number = response['tracking_number']
        if tracking_number is not None:
            shipment = Shipment.objects.get(id=shipment.id)
            shipment.tracking_number = tracking_number
            shipment.save()
        return shipment

    def print_label():
        return

    def cancel_shipment(self, tracking_number):
        response = SMSAServices().cancel_shipment(tracking_number)
        is_shipment_cancelled = response['shipment_canceled']
        return is_shipment_cancelled
        
    def get_status(self, tracking_number):
        status = SMSAServices().get_status(tracking_number)['shipment_status']
        if status:
            system_status = self.status_mapper(status)
            shipment = Shipment.objects.get(tracking_number=tracking_number)
            shipment.status = system_status
            shipment.save()
        return system_status
        
    ## Map SMSA status and return the equivalent system status
    def status_mapper(self, status):
        ## Getting status (SMSA) ##
        if status == SMSA_Shipment_StatusChoises[0][0] or status == SMSA_Shipment_StatusChoises[1][0]:
            return Shipment_StatusChoises[0][0]
        elif  status == SMSA_Shipment_StatusChoises[2][0] or status == SMSA_Shipment_StatusChoises[3][0] :
            return Shipment_StatusChoises[1][0]
        elif status == SMSA_Shipment_StatusChoises[4][0] or status ==SMSA_Shipment_StatusChoises[5][0]:
            return Shipment_StatusChoises[2][0]
    