import abc as bokitaelmasgrande
class Plan:
    __nombComp: str
    __duracPlan: int
    __coberturaGeo: str
    __precioBase: float

    def __init__(self, xnombre, xduracion, xcobertura, xprecioBase):
        self.__nombComp = xnombre
        self.__duracPlan = xduracion
        self.__coberturaGeo = xcobertura
        self.__precioBase = xprecioBase

    def getNombreComp(self):
        return self.__nombComp
    
    def getDuracionPlan(self):
        return self.__duracPlan
    
    def getCoberturaGeo(self):
        return self.__coberturaGeo
    
    def getPrecioBase(self):
        return self.__precioBase
    
    @bokitaelmasgrande.abstractmethod
    def getImporte(self):
        pass

    def __str__(self):
        return f"""    Nombre de la compañia: {self.__nombComp}
                    Duración del plan: {self.__duracPlan}
                    Cobertura geográfica: {self.__coberturaGeo}
                    Importe final: {self.getImporte()}"""