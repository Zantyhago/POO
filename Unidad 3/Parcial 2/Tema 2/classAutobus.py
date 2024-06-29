from classVehiculo import Vehiculo

class Autobus(Vehiculo):
    __tipoServicio: str
    __turno: str

    def __init__(self, xmarca, xmodelo, xanyo, xcapacidad, xplazas, xdistancia, xtarifa, xtipo, xturno):
        super().__init__(xmarca, xmodelo, xanyo, xcapacidad, xplazas, xdistancia, xtarifa)
        self.__tipoServicio = xtipo
        self.__turno = xturno

    def getTipoServicio(self):
        return self.__tipoServicio
    
    def getTurno(self):
        return self.__turno
    
    def calculoTarifa(self):
        if self.getTurno == "noche" and self.getTipoServicio == "turismo":
            tarifa = self._Vehiculo__tarifaBase * 1.20
        else:
            tarifa = self._Vehiculo__tarifaBase * 1.05
        return tarifa