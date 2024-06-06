from abc import ABC
class Plan(ABC):
    __nomComp: str
    __duracion: str
    __cobertGeo: str
    __precioBase: float

    def __init__(self, xnom, xduracion, xcobertura, xprecio):
        self.__nomComp = xnom
        self.__duracion = xduracion
        self.__cobertGeo = xcobertura
        self.__precioBase = xprecio

    def getNombre(self):
        return self.__nomComp
    
    def getDuracion(self):
        return self.__duracion

    def getCobretura(self):
        return self.__cobertGeo
    
    def getPrecioBase(self):
        return self.__precioBase
    
    @classmethod
    def caca(self):
        pass