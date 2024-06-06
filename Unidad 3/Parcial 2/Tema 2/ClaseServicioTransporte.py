import abc
from abc import ABC
class ServicioTransporte:
    __marca: str 
    __modelo: str
    __anio: int 
    __capacidadpasajeros: int
    __numplazas: int
    __distancia: float
    __tarifabase: float
    
    def __init__(self,marca,modelo,anio,capacidadpasajeros,numplazas,distancia,tarifabase):
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__capacidadpasajeros = capacidadpasajeros
        self.__numplazas = numplazas
        self.__distancia = distancia
        self.__tarifabase = tarifabase
        
    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
    def getAnio(self):
        return self.__anio
    def getCapacidadpasajeros(self):
        return self.__capacidadpasajeros
    def getNumplazas(self):
        return self.__numplazas
    def getDistancia(self):
        return self.__distancia
    def getTarifabase(self):
        return self.__tarifabase
    
    @abc.abstractmethod
    def CalculoTarifaServicio(self):
        pass
