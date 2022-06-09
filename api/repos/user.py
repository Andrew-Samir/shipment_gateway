from django.db.models import Q

from ._base_repo import BaseRepo

from ..models import User


class UserRepo(BaseRepo):

    def __init__(self):
        super().__init__(User)

    # Get User
    def get_user(self, id: int):
        q = Q(id=id)
        return self._get_single(q)