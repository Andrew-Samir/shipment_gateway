from typing import List

# from django.core.paginator import Page, Paginator
from django.db import models
from django.db.models import Q

class BaseRepo():

    __model: models.Model
    _is_transaction: bool
    _prefetch_tables: List[str]

    def __init__(self, model: models.Model):
        self.__model = model
    
    # Get Single
    def _get_single(self, q: Q, include_deleted = False):
        try: return self.build_query(include_deleted=include_deleted).get(q)
        except self.__model.DoesNotExist: return None

    # Build Query
    def build_query(self, include_deleted = False):
        query = self.__model.objects if not include_deleted else self.__model.all_objects
        return query
