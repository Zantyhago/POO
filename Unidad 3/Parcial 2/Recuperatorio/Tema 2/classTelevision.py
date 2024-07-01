from classPlanes import Plan

class Television (Plan):
    __cantCanNacs: int
    __cantCanInts: int

    def __init__(self, xnombre, xduracion, xcobertura, xpreciobase, xcantNac, xcantInt):
        super().__init__(xnombre, xduracion, xcobertura, xpreciobase)
        self.__cantCanNacs = xcantNac
        self.__cantCanInts = xcantInt
    
    def getCantNac(self):
        return self.__cantCanNacs
    
    def getCantInt(self):
        return self.__cantCanInts
    
    def getImporte(self):
        pbase = self.getPrecioBase() # método heredado de Plan
        cantIts = self.getCantInt()
        if cantIts > 10:
            importe = pbase * 1.15
        return importe