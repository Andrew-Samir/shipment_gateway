from django.db.models import Q

from ._base_repo import BaseRepo

from ..models import Shipment


class ShipmentRepo(BaseRepo):

    def __init__(self):
        super().__init__(Shipment)

    # Get Product
    def get_shipment(self, id: int):
        q = Q(id=id)
        return self._get_single(q)