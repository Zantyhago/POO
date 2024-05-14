import csv
from classcliente import Cliente
class GestorCliente:
    __listaCli: list

    def __init__(self):
        self.__listaCli = []

    def agregar(self):
        archivo = open("ClientesFarmaCiudad.csv")
        reader = csv.archivo(delimiter = ';')
        bandera = True
        for fila in len(self.__listaCli):
            if bandera:
                bandera = False
            else:
                name = fila[0]
                surname = fila[1]
                dni = fila[2]
                numacc = fila[3]
                saldoant = fila[4]
                nuevoCli = Cliente(name, surname, dni, numacc, saldoant)
                self.agregar(nuevoCli)
            
    def buscasaldOld(self, xdni):
        bandera = True
        i = 0
        while i < len(self.__lista) and bandera:
            if xdni == self.__lostaCli[i].getdni() and bandera:
                xapell = self.__lostaCli[i].getsurname()
                xnom = self.__lostaCli[i].getname()
                xnum = self.__lostaCli[i].getnumacc()
                xsaldo = self.__lostaCli[i].getsaldo()
                bandera = False
            else:
                i += 1
        return xapell, xnom, xnum, xsaldo
            
    def buscacli(self, xdni):
        i = 0
        bandera = True
        while i < len(self.__listaCli) and bandera:
            if xdni == self.__listaCli[i].getdni():
                apell = self.__listaCli[i].getsurname()
                nomb = self.__listaCli[i].getname()
                numacc = self.__listaCli[i].getnumacc()
            else:
                i += 1
        return apell, nomb, numacc