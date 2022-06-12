from abc import ABCMeta, abstractstaticmethod

class ICourier(metaclass=ABCMeta):

    @abstractstaticmethod
    def status_mapper():
        """ Status method """
        