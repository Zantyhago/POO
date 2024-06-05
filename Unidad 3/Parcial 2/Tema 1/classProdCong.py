class Congelado:
    __PorcN: float
    __PorcO: float
    __PorcCO: float
    __PorcVapor: float
    __MetodoPechi: str

    def __init__(self, xnom, xfechaE, xfechaV, xtemp, xpais, xnum, xcostoB, xporN, xporO, xporcCO, xporcVap, xmetodo):
        super().__init__( xnom, xfechaE, xfechaV, xtemp, xpais, xnum, xcostoB)
        self.__PorcN = xporN
        self.__PorcO = xporO
        self.__PorcCO = xporcCO
        self.__PorcVapor = xporcVap
        self.__MetodoPechi = xmetodo

    def getPorcN(self):
        return self.__PorcN
        
    def getPorcO(self):
        return self.__PorcO
    
    def getOPorcCO(self):
        return self.__PorcCO
        
    def getPorcVapor(self):
        return self.__PorcVapor
    
    def getMetodoPechi(self):
        return self.__MetodoPechi
    
    def getImporte(self):
        costoBase = super().getCostoBase()
        importe: float
        try:
            if self.__MetodoPechi == 'mecanico':
                importe = costoBase * 1.15
            elif self.__MetodoPechi == 'criogenico':
                importe = costoBase * 1.15
            else:
                raise AssertionError
        except AssertionError:
            print("Metodo mal ingresado.")
        finally:
            return importe