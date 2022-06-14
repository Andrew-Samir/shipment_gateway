import random

#####################################
####    SMSA Integration (DUMY)  ####
#####################################

SMSA_Shipment_StatusChoises = [
    'shipment created',
    'picked up',
    'in transit',
    'Out for Delivery',
    'Delivery order on hand',
    'delivered',
]
class SMSAServices:

    def __init__(self) -> None:
        self.url = None

    def create_shipment(self, request_payload):
        
        response = {
            'sender': request_payload.sender,
            'reciever': request_payload.reciever,
            'tracking_number': '45253698'
        }

        return response

    def cancel_shipment(self, request_payload):
        can_cancel = bool(random.getrandbits(1))
        response = {
            'shipment_canceled': can_cancel
        }

        return response

    def get_status(self, request_payload):
        status = random.choice(SMSA_Shipment_StatusChoises)
        response = {
            'shipment_status': status
        }

        return response
