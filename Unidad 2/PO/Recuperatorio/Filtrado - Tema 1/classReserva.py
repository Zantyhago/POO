class Reserva:
    __numReserva: int
    __nombPersona: str
    __numCabaña: int
    __fecha: str
    __cantHuespedes: int
    __cantDias: int
    __importeSeña: float

    def __init__(self, xnum, xnomb, xnumCab, xfecha, xcantHues, xcantD, ximp):
          self.__numReserva = xnum
          self.__nombPersona = xnomb
          self.__numCabaña = xnumCab
          self.__fecha = xfecha
          self.__cantHuespedes = xcantHues
          self.__cantDias = xcantD
          self.__importeSeña = ximp

    def getNumR(self):
        return self.__numReserva

    def getNombre(self):
        return self.__nombPersona

    def getNumCab(self):
        return self.__numCabaña

    def getFecha(self):
        return self.__fecha

    def getCantHues(self):
        return self.__cantHuespedes

    def getCantDias(self):
        return self.__cantDias
    
    def getImporteSeña(self):
        return self.__importeSeña