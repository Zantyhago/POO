class Nacimiento:
    __DNImama: float
    __tipoParto: str
    __fecha: str
    __hora: str
    __peso: float
    __altura: int
    def __init__(self, xdni, xtipo, xfecha, xhora, xpeso, xaltura):
        self.__DNI = xdni
        self.__tipoParto = xtipo
        self.__fecha = xfecha
        self.__hora = xhora
        self.__peso = xpeso
        self.__altura = xaltura
    
    def getDNIMama(self):
        return self.__DNImama
    
    def getTipoP(self):
        return self.__tipoParto
    
    def getFecha(self):
        return self.__fecha

    def getHora(self):
        return self.__hora
    
    def getPeso(self):
        return self.__peso
    
    def getAlura(self):
        return self.__altura
    
    def __eq__(self, unaMama):
        DNI = self.getDNIMama
        return DNI == unaMama.getDNI