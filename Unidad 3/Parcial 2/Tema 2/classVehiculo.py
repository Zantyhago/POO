import abc as Tuma
class Vehiculo:
    __marca: str
    __modelo: str
    __anyo: int
    __capPasajeros: int
    __numPlazas: int
    __distanciaReco: float
    __tarifaBase: float

    def __init__(self, xmarca, xmodelo, xanyo, xcapacidad, xplazas, xdistancia, xtarifa):
        self.__marca = xmarca
        self.__modelo = xmodelo
        self.__anyo = xanyo
        self.__capPasajeros = xcapacidad
        self.__numPlazas = xplazas
        self.__distanciaReco = xdistancia
        self.__tarifaBase = xtarifa

    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getAnyo(self):
        return self.__anyo
    
    def getCapacidad(self):
        return self.__capPasajeros
    
    def getNumPlaza(self):
        return self.__numPlazas
    
    def getDistancia(self):
        return self.__distanciaReco
    
    def getTarifaBase(self):
        return float(self.__tarifaBase)
    
    @Tuma.abstractmethod
    def calculoTarifa(self):
        pass

    def __str__(self):
        return f"""
        Modelo: {self.getModelo()}
        Año de fabricación: {self.getAnyo()}
        Capacidad de pasajeros: {self.getCapacidad()}
        Tarifa del servicio: {self.calculoTarifa()}
        
        .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-."""