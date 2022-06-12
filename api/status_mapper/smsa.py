from ._base_interface_ import ICourier
from ..models.shipment import Shipment_StatusChoises

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

    ## Map SMSA status and return the equivalent system status
    def status_mapper(self, status):
        print("Getting status (SMSA)")
        if status == SMSA_Shipment_StatusChoises[0][0] or status == SMSA_Shipment_StatusChoises[1][0]:
            return Shipment_StatusChoises[0][0]
        elif  status == SMSA_Shipment_StatusChoises[2][0] or status == SMSA_Shipment_StatusChoises[3][0] :
            return Shipment_StatusChoises[1][0]
        elif status == SMSA_Shipment_StatusChoises[4][0] or status ==SMSA_Shipment_StatusChoises[5][0]:
            return Shipment_StatusChoises[2][0]
    