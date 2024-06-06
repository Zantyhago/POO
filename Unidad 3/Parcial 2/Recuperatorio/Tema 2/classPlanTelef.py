from classPlan import Plan

class Telefonia(Plan):
    __tipoLlamada: str
    __cantMins: int

    def __init__(self, xnom, xduracion, xcobertura, xprecio, xtipo, xcantMins):
        super().__init__(xnom, xduracion, xcobertura, xprecio)
        self.__tipoLlamada = xtipo
        self.__cantMins = xcantMins
    
    def getTipo(self):
        return self.__tipoLlamada
    
    def getCantidadMins (self):
        return self.__cantMins
    
    def getImporte(self):
        costo = super().getPrecioBase()
        if self.__tipoLlamada == "Internacional":
            costo += super().getPrecioBase() * 1.20
        else:
            costo += super().getPrecioBase() * 0.075
        return costo
    

        