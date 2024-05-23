from classMama import Mama
import numpy as np
import csv
class GestorMama:
    __listaMamas: list

    def __init__(self):
        self.__listaMamas = np.empty([0], dtype = Mama)
        self.__cantidad = 0
        self.__dimension = 0
        self.__incremento = 1

    def leerdatos(self, nuevaMom):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listaMamas.resize(self.__dimension)
        self.__listaMamas[self.__cantidad] = nuevaMom
        self.__cantidad += 1

    def agregaMama(self, nuevaNac):
        archivo = open('Mamas.csv')
        reader = csv.reader(archivo, delimiter = ';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                self.agregarMovimiento(Mama(float(fila[0]), fila[1], fila[2], fila[3], float(fila[4], int(fila[5]))))
        archivo.close()

    def buscaMama(self, GN):
        xdni = float(input("Ingrese DNI de la mamá: "))
        i = 0
        posN = GN.buscaPosMama(xdni)
        bandera = False
        while i < len(self.__listaMamas) and bandera is False:
            if self.__listaMamas[i].getDNI() == xdni:
                posM = i
                bandera = True
    
    def buscaMultiplesNacs(self, GN):
        i = 0
        xdni = float(input("Ingrese DNI para buscar: "))
        if GN._

    # MasDeUnHijo