from classPlan import Plan

class Television:
    __cantNac: int
    __cantInt: int
    
    def __init__(self, xnom, xduracion, xcobertura, xprecio, xcantNac, xcantInt):
        super().__init__(xnom, xduracion, xcobertura, xprecio)
        self.__cantNac = xcantNac
        self.__cantInt = xcantInt

    def getCantNac(self):
        return self.__cantNac
    
    def getCantInt(self):
        return self.__cantInt
    
    def getImporte(self):
        costo = super().getPrecioBase()
        if self.__cantInt > 10:
            costo += super().getPrecioBase() * 1.15
        return costo
    