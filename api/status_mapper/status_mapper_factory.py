
from .aramex import Aramex
from .smsa import SMSA 


Courier_Choises = [
    ('aramex','Aramex'),
    ('SMSA', 'SMSA')
]
class StatusMapperFactory:

    @staticmethod
    def get_system_status(self, courier, status):
        if courier == Courier_Choises[0][0]:
            return Aramex().status_mapper(status)
        if courier == Courier_Choises[1][0]:
            return SMSA().status_mapper(status)
        return None