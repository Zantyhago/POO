class Refrigerado:
    __CodigoSuperv: str

    def __init__(self, xnom, xfechaE, xfechaV, xtemp, xpais, xnum, xcostoB, xcodigo):
        super().__init__( xnom, xfechaE, xfechaV, xtemp, xpais, xnum, xcostoB)
        self.__CodigoSuperv = xcodigo
    
    def getCoidgoSup(self):
        return self.__CodigoSuperv
    
    def getImporte(self):
        costoBase = super().getCostoBase()
        importe: float
        fechaACtu = '1/6/2024'.split('/')
        mesActu = int(fechaACtu[1])
        anyoActu = int(fechaACtu[2])
        fechaVen = self.__getFechaVen().split('/')
        mesVen = int(fechaVen[1])
        anyoVen = int(fechaVen[2])
        mesesDif = (anyoActu * 12 + mesActu) - (anyoVen * 12 + mesVen)
        try:
            if mesesDif <= 2 and mesesDif > 0:
                importe = costoBase * 0.10
            elif mesesDif > 2:
                importe = costoBase * 1.01
            else:
                raise AssertionError
        except AssertionError:
            print("Fecha mal ingresada.")
        finally:
            return importe