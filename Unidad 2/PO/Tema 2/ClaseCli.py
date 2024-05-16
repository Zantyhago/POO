class Cliente:
    __nom: str
    __ap: str
    __dni: float
    __nro_cta: int
    __saldo_ant: float

    def __init__ (self, xnom, xap, xdni, xnro_cta, xsald_ant):
        self.__nom = xnom
        self.__ap = xap
        self.__dni = xdni
        self.__nro_cta = xnro_cta
        self.__saldo_ant = xsald_ant

    def getNom(self):
        return self.__nom
    
    def getAp(self):
        return self.__ap
    
    def getDNI(self):
        return self.__dni
    
    def getNro_cta (self):
        return self.__nro_cta
    
    def getSaldo_ant(self):
        return self.__saldo_ant
    
    #modificaciones
    def __lt__ (self, otro):
        return self.__nro_cta < otro.getNro_cta()
    
    def __str__ (self):
        return f"{self.ap, self.__nom, self.__nro_cta}"