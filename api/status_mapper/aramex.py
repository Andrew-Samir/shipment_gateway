from ._base_interface_ import ICourier
from ..models.shipment import Shipment_StatusChoises

Aramex_Shipment_StatusChoises = [
    ('Shipment created', 'Shipment created.'),
    ('Shipment picked up', 'Shipment picked up'),
    ('Out for Delivery', 'Shipment out for delivery.'),
    ('in transit', 'Shipment in transit'),
    ('Delivery order on hand', 'Delivered on hand'),
    ('delivered', 'Shipment completed.')
]

class Aramex(ICourier):
    
    def __init__(self) -> None:
        super().__init__()

    ## Map aramex status and return the equivalent system status
    def status_mapper(self, status):
        print("Getting status (aramex)")
        if status == Aramex_Shipment_StatusChoises[0][0] or status == Aramex_Shipment_StatusChoises[1][0]:
            return Shipment_StatusChoises[0][0]
        elif status == Aramex_Shipment_StatusChoises[2][0] or status == Aramex_Shipment_StatusChoises[3][0]:
            return Shipment_StatusChoises[1][0]
        elif status == Aramex_Shipment_StatusChoises[4][0] or status == Aramex_Shipment_StatusChoises[5][0]:
            return Shipment_StatusChoises[2][0]
    