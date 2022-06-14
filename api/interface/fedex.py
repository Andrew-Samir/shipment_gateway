from ._base_interface_ import ICourier
from ..models import Shipment, Shipment_StatusChoises
from ..integration import FedexServices
import json

FedEx_Shipment_StatusChoises = [
    ('Initiated', 'shipment information send to FedEx'),
    ('Picked up', 'Shipment pickedup'),
    ('At local FedEx facility', 'Shipment at local FedEx facility.'),
    ('Arrived at FedEx location', 'Shipment arrived at fedex location.'),
    ('Departed FedEx location', 'Departed FedEx location'),
    ('Out for Delivery', 'Shipment out for delivery.'),
    ('In transit','Shipment in transit'),
    ('Delivered', 'Shipment completed.')
]

class FedEx(ICourier):
    
    def __init__(self) -> None:
        super().__init__()

    # Create Shipment
    ## Integrated with FedEx
    def create_shipment(self, shipment):
        shipment_payload = shipment
        payload = {
            "labelResponseOptions": "URL_ONLY",
            "requestedShipment": {
                "shipper": {
                "contact": {
                    "personName": shipment.sender.username,
                    "phoneNumber": shipment.sender.phone,
                    "companyName": shipment.sender.company_name
                },
                "address": {
                    "streetLines": [
                        shipment.sender.address
                    ],
                    "city": shipment.sender.city,
                    "stateOrProvinceCode": "FL",
                    "postalCode": 32056,
                    "countryCode": "US"
                }
                },
                "recipients": [
                {
                    "contact": {
                    "personName": shipment.reciever.username,
                    "phoneNumber": shipment.reciever.phone,
                    "companyName": shipment.reciever.company_name
                    },
                    "address": {
                    "streetLines": [
                        shipment.reciever.address
                    ],
                    "city": shipment.reciever.city,
                    "stateOrProvinceCode": "TN",
                    "postalCode": 38017,
                    "countryCode": "US"
                    }
                }
                ],
                "shipDatestamp": "2020-12-30",
                "serviceType": "STANDARD_OVERNIGHT",
                "packagingType": "FEDEX_SMALL_BOX",
                "pickupType": "USE_SCHEDULED_PICKUP",
                "blockInsightVisibility": False,
                "shippingChargesPayment": {
                "paymentType": "SENDER"
                },
                "shipmentSpecialServices": {
                "specialServiceTypes": [
                    "FEDEX_ONE_RATE"
                ]
                },
                "labelSpecification": {
                "imageType": "PDF",
                "labelStockType": "PAPER_85X11_TOP_HALF_LABEL"
                },
                "requestedPackageLineItems": [
                {}
                ]
            },
            "accountNumber": {
                "value": "740561073"
            }
            }
        response = FedexServices().create_shipment(payload)
        tracking_number = json.loads(response)['output']['transactionShipments']
        tracking_number = tracking_number[0]["masterTrackingNumber"]
        if tracking_number is not None:
            shipment = Shipment.objects.get(id=shipment_payload.id)
            shipment.tracking_number = tracking_number
            shipment.save()
        return shipment

    def print_label(self, payload):
        pass

    def cancel_shipment(self, tracking_number):
        payload = {
            "accountNumber": {
                "value": "740561073"
            },
            "trackingNumber": tracking_number
            }
        response = FedexServices().cancel_shipment(payload)
        is_shipment_cancelled = json.loads(response)['output']['cancelledShipment']
        return is_shipment_cancelled

    def get_status(self, tracking_number):
        payload = {
            "trackingInfo": [
            {
                "trackingNumberInfo": {
                "trackingNumber": 123456789012
                }
            }
            ],
            "includeDetailedScans": "true"
            }
        response = FedexServices().get_status(payload)
        status = json.loads(response)['output']['completeTrackResults']
        status = status[0]['trackResults']
        status = status[0]['latestStatusDetail']['statusByLocale']
        if status:
            system_status = self.status_mapper(status)
            shipment = Shipment.objects.get(tracking_number=tracking_number)
            shipment.status = system_status
            shipment.save()
        return system_status

    ## Map FedEx status and return the equivalent system status
    def status_mapper(self, status):
        ## Getting status (FedEx) ##
        if status == FedEx_Shipment_StatusChoises[0][0] or status == FedEx_Shipment_StatusChoises[1][0] or status == FedEx_Shipment_StatusChoises[2][0] or status == FedEx_Shipment_StatusChoises[3][0]:
            return Shipment_StatusChoises[0][0]
        elif  status == FedEx_Shipment_StatusChoises[4][0] or status == FedEx_Shipment_StatusChoises[5][0] or status == FedEx_Shipment_StatusChoises[6][0] :
            return Shipment_StatusChoises[1][0]
        elif status == FedEx_Shipment_StatusChoises[7][0]:
            return Shipment_StatusChoises[2][0]
    