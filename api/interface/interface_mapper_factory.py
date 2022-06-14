
from .aramex import Aramex
from .smsa import SMSA 
from .fedex import FedEx


Courier_Choises = [
    ('fedex', 'FedEx'),
    ('aramex','Aramex'),
    ('SMSA', 'SMSA')
]
class InterfaceMapperFactory:

    @staticmethod
    def get_courier(courier):
        if courier == Courier_Choises[0][0]:
            return FedEx()
        if courier == Courier_Choises[1][0]:
            return Aramex()
        if courier == Courier_Choises[2][0]:
            return SMSA()
        return None