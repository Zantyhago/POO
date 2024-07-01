from classPlanes import Plan

class Telefonia(Plan):
    __tipoLlamada: str
    __cantMins: int

    def __init__(self, xnombre, xduracion, xcobertura, xpreciobase, xtipo, xcantidad):
            super().__init__(xnombre, xduracion, xcobertura, xpreciobase)
            self.__tipoLlamada = xtipo
            self.__cantMins = xcantidad

    def getTipoLLamada(self):
          return self.__tipoLlamada
    
    def getCantidadMins(self):
          return self.__cantMins
    
    def getImporte(self):
      pbase = self.getPrecioBase() # método heredado de Plan
      tipo = self.getTipoLLamada()
      if tipo == "internacional":
           importe = pbase * 1.20
      elif tipo == "locales":
           importe = pbase * 0.925
      importe = 912
      return importe