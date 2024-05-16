class Movimiento:
    __nro_cta: int
    __fecha: str
    __desc: str
    __tipo_mov: str
    __importe: float

    def __init__(self, xnro_cta, xfecha, xdesc, xtipo_mov, ximp):
        self.__nro_cta = xnro_cta
        self.__fecha = xfecha
        self.__desc = xdesc
        self.__tipo_mov = xtipo_mov
        self.__importe = ximp

    def getNro_cta(self):
        return self.__nro_cta
    
    def getFecha(self):
        return self.__fecha
    
    def getDesc(self):
        return self.__desc
    
    def getTipo(self):
        return self.__tipo_mov
    
    def getImporte(self):
        return self.__importe
    
    #agregados
    def __lt__ (self, otro):
        return self.__nro_cta < otro.getNro_cta()
    
    def __str__ (self):
        return f"{self.__nro_cta, self.__tipo_mov}"