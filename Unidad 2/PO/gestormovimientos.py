import csv
import numpy as np
from classmove import Movimiento
class GestorMovimiento:
    __listaMov: np.array

    def __init__(self, nuevomov):
        self.__listaMov = np.empty([0], dtype = Movimiento)

    def agrega(self, nuevo):
        self.__listaMov = np.append(self.__listaMov, nuevo)

    def leedatos(self):
        archivo = open("MovimientosAbril2024.csv")
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in len(self.__listaMov):
            if bandera:
                bandera = False
            else:
                ncc = fila[0]
                fecha = fila[1]
                descr = fila[2]
                tipom = fila[3]
                imp = fila[4]
                nuevoMov = Movimiento(ncc,fecha,descr,tipom,imp)
                self.agregar(nuevoMov)
        archivo.close()

    def actualiza(self, xnum, xsaldoant):
        i = 0
        while i < len(self.__listaMov):
            if xnum == self.__listaMov[i].getnumacc():
                fecha = self.__listaMov[i].getfecha()
                descr = self.__listaMov[i].getdescr()
                imp = self.__listaMov[i].getimp()
                type = self.__listaMov[i].gettipomov()
                if type == 'C':
                    xsaldoant += imp
                elif type == 'P':
                    xsaldoant -= imp
        return fecha, descr, imp, type                

    def buscarmov(self, xnum):
        i = 0
        bandera = False
        while i < len(self.__listaMov) and bandera != False:
            if xnum == self.__listaMov[i].getnumacc():
                bandera = True
            else:
                i += 1
        return bandera
    
    def ordena(self):
        self.__listaMov = np.sort(self.__listaMov)

    def muestra(self):
        for i in range(len(self.__listaMov)):
            print(self.__listaMov[i])