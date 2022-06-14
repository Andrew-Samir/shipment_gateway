from abc import ABCMeta, abstractstaticmethod

class ICourier(metaclass=ABCMeta):

    @abstractstaticmethod
    def status_mapper():
        """ Status method """
        
    @abstractstaticmethod
    def create_shipment():
        """ Status method """
        
    @abstractstaticmethod
    def print_label():
        """ Status method """
    
    @abstractstaticmethod
    def cancel_shipment():
        """ Status method """
           
    @abstractstaticmethod
    def get_status():
        """ Status method """
    