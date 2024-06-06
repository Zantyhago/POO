from ClaseServicioTransporte import ServicioTransporte

class Van(ServicioTransporte):
    __tipocarroceria: str
    
    def __init__(self,marca,modelo,anio,capacidadpasajeros,numplazas,distancia,tarifabase,tipocarroceria):
        super().__init__(marca,modelo,anio,capacidadpasajeros,numplazas,distancia,tarifabase)
        self.__tipocarroceria = tipocarroceria 
        
    def getTipocarroceria(self):
        return self.__tipocarroceria
    
    def CalculaTarifaServicio(self):
        tarifaTotal = 0
        porcentaje = 0
        if self.__tipocarroceria == "minivan":
            porcentaje = -(float(self.getTarifabase()) * 0.10)
        else:
            porcentaje = float(self.getTarifabase()) * 0.025
        tarifaTotal = float(self.getTarifabase()) + porcentaje
        return tarifaTotal


        
        