from django.db.models import Q

from ._base_repo import BaseRepo

from ..models import Courier


class CourierRepo(BaseRepo):

    def __init__(self):
        super().__init__(Courier)

    # Get Courier
    def get_courier(self, id: int):
        q = Q(id=id)
        return self._get_single(q)