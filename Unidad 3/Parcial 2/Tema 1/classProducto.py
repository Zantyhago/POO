import abc
from abc import ABC
class Producto:
    __NombreProd: str
    __fechaEnv: str
    __fechaVen: str
    __tempRecom: float
    __pais: str
    __numLote: int
    __costoBase :float

    def __init__(self, xnom, xfechaE, xfechaV, xtemp, xpais, xnum, xcostoB):
        self.__NombreProd = xnom
        self.__fechaEnv = xfechaE
        self.__fechaVen = xfechaV
        self.__tempRecom = xtemp
        self.__pais = xpais
        self.__numLote = xnum
        self.__costoBase = xcostoB

    def getNombre(self):
        return self.__NombreProd

    def getFechaEnv(self):
        return self.__fechaEnv
    
    def getFechaVen(self):
        return self.__fechaVen
    
    def getTempeRecom(self):
        return self.__tempRecom
    
    def getPais(self):
        return self.__pais
    
    def getNumLote(self):
        return self.__numLote
    
    def getCostoBase(self):
        return self.__costoBase
    
    def __str__(self):
        return f"""
Nombre del producto: {self.__NombreProd}
Pais de origen: {self.__pais}
Temperatura de mant. recomendada: {self.__tempRecom}
Importe de venta: {self.getImporte()}"""

    @abc.abstractmethod
    def getImporte(self):
        pass

    