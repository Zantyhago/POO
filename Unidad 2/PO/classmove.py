class Movimiento:
    __numeacc: int
    __fecha: str
    __descr: str
    __tipomov: str
    __importe: float

    def __init__(self, xnum, xfecha, xdescr, xtipo, ximp):
        self.__numeacc = xnum
        self.__fecha = xfecha
        self.__descr = xdescr
        self.__tipomov = xtipo
        self.__importe = ximp

    def getnumacc(self):
        return self.__numeacc

    def getfecha(self):
        return self.__fecha

    def getdescr(self):
        return self.__descr

    def gettipomov(self):
        return self.__tipomov

    def getimp(self):
        return self.__importe

    def __str__(self):
        return f'Numero de cuenta: {self.__numeacc}. Fecha: {self.__fecha}. Descripción: {self.__descr}. Tipo: {self.__tipomov}. Importe: {self.__importe}'
    
    def __lt__(self,other):
        return self.__numeacc < other.__numeacc