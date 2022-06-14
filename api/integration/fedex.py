import requests
import json

################################
####    FedEx Integration   ####
################################
class FedexServices:

    def __init__(self) -> None:
        self.url = None

    def auth(self):
        url = "https://apis-sandbox.fedex.com/oauth/token"

        payload = {
            "grant_type":"client_credentials",
            "client_id":"l72d11f4bee7b84155bf320afb6a39291a",
            "client_secret":"308432a5ad404d7ca7c8546034b4567b"
        }

        headers = {
            'Content-Type': "application/x-www-form-urlencoded"
            }

        response = requests.request("POST", url, data=payload, headers=headers)
        auth_token = json.loads(response.text)['access_token']
        return auth_token

    def create_shipment(self, request_payload):
        self.url = "https://apis-sandbox.fedex.com/ship/v1/shipments"
        auth_token = self.auth()
        payload = json.dumps(request_payload)
        headers = {
            'Content-Type': "application/json",
            'X-locale': "en_US",
            'Authorization': "Bearer " + auth_token
            }
        response = requests.request("POST", self.url, data=payload, headers=headers)

        return response.text

    def cancel_shipment(self, request_payload):
        self.url = "https://apis-sandbox.fedex.com/ship/v1/shipments/cancel"

        auth_token = self.auth()
        payload = json.dumps(request_payload)
        headers = {
            'Content-Type': "application/json",
            'X-locale': "en_US",
            'Authorization': "Bearer " + auth_token
            }
        response = requests.request("PUT", self.url, data=payload, headers=headers)

        return response.text

    def get_status(self, request_payload):
        self.url = "https://apis-sandbox.fedex.com/track/v1/trackingnumbers"
        auth_token = self.auth()
        payload = json.dumps(request_payload)
        headers = {
            'Content-Type': "application/json",
            'X-locale': "en_US",
            'Authorization': "Bearer " + auth_token
            }
        response = requests.request("POST", self.url, data=payload, headers=headers)

        return response.text
