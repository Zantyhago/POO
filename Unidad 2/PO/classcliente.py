import csv
class Cliente:
    __nombre: str
    __apellido: str
    __dni: int
    __numacc: int
    __saldoant: float

    def __init__(self, xnom, xapell, xdni, xnacc, xsaldoant):
        self.__nombre = xnom
        self.__apellido = xapell
        self.__dni = xdni
        self.__numacc = xnacc
        self.__saldoant = xsaldoant

    def getname(self):
        return self.__nombre

    def getsurname(self):
        return self.__apellido

    def getdni(self):
        return self.__dni

    def getnumacc(self):
        return self.__numacc

    def getsaldo(self):
        return self.__saldoant
