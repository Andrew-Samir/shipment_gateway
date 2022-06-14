import random

#######################################
####    Aramex Integration (DUMY)  ####
#######################################

Aramex_Shipment_StatusChoises = [
    'Shipment created',
    'Shipment picked up',
    'Out for Delivery',
    'in transit',
    'Delivery order on hand',
    'delivered'
]

class AramexServices:

    def __init__(self) -> None:
        self.url = None

    def create_shipment(self, request_payload):
        
        response = {
            'sender': request_payload.sender,
            'reciever': request_payload.reciever,
            'tracking_number': '123456789'
        }

        return response

    def cancel_shipment(self, request_payload):
        can_cancel = bool(random.getrandbits(1))
        response = {
            'shipment_canceled': can_cancel
        }

        return response

    def get_status(self, request_payload):
        status = random.choice(Aramex_Shipment_StatusChoises)
        response = {
            'shipment_status': status
        }

        return response
