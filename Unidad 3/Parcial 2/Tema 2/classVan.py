from classVehiculo import Vehiculo

class Van(Vehiculo):
    __tipoCarroceria: str

    def __init__(self, xmarca, xmodelo, xanyo, xcapacidad, xplazas, xdistancia, xtarifa, xtipo):
        super().__init__(xmarca, xmodelo, xanyo, xcapacidad, xplazas, xdistancia, xtarifa)
        self.__tipoCarroceria = xtipo
    
    def getTipoCarroc(self):
        return self.__tipoCarroceria
    
    def calculoTarifa(self):
        if self.getTipoCarroc == "minivan":
            tarifa = self._Vehiculo__tarifaBase * 0.90
        else:
            tarifa = self._Vehiculo__tarifaBase * 1.025
        return tarifa