class Cabaña:
    __numero: int
    __cantHab: int
    __cantCamasG: int
    __cantCamasCh: int
    __importe: float

    def __init__(self, xnum, xcantH, xcantCG, xcantCCh, ximp):
        self.__numero = xnum
        self.__cantHab = xcantH
        self.__cantCamasG = xcantCG
        self.__cantCamasCh = xcantCCh
        self.__importe = ximp
    
    def getNumero(self):
        return self.__numero
    
    def getcantH(self):
        return self.__cantHab
    
    def getCantCamasG(self):
        return self.__cantCamasG
    
    def getCantCamasCh(self):
        return self.__cantCamasCh
    
    def getImporte(self):
        return self.__importe
    
    def getCapacidad(self):
        capacidad =  int((self.__cantCamasG *2) + self.__cantCamasCh)
        return capacidad
    
    def __eq__(self, unaReserva):
        capacidad = self.getCapacidad
        return capacidad == unaReserva.getCantHues