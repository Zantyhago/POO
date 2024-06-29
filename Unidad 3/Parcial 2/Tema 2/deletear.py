from ClaseServicioTransporte import ServicioTransporte

class Autobus(ServicioTransporte):
    __tiposervicio: str
    __turno: str
    
    def __init__(self,marca,modelo,anio,capacidadpasajeros,numplazas,distancia,tarifabase,tiposervicio,turno):
        super().__init__(marca,modelo,anio,capacidadpasajeros,numplazas,distancia,tarifabase)
        self.__tiposervicio = tiposervicio
        self.__turno = turno
        
    def getTipo(self):
        return self.__tipo
    def getTurno(self):
        return self.__turno
    
    def CalculaTarifaServicio(self):
        tarifaTotal = 0
        porcentaje = 0
        if self.__turno == "noche" and self.__tiposervicio == "turismo":
            porcentaje = float(self.getTarifabase()) * 0.20
        else:
            porcentaje = float(self.getTarifabase()) * 0.05
        tarifaTotal = float(self.getTarifabase()) + porcentaje
        return tarifaTotal
        
