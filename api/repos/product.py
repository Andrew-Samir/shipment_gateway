from django.db.models import Q

from ._base_repo import BaseRepo

from ..models import Product


class ProductRepo(BaseRepo):

    def __init__(self):
        super().__init__(Product)

    # Get Product
    def get_product(self, id: int):
        q = Q(id=id)
        return self._get_single(q)