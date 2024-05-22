from classCabaña import Cabaña
import numpy as np
import csv
class GestorCabaña:
    __cantidad: int
    __dimension: int
    __incremento: int
    __listCabañas: np.ndarray

    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 11
        self.__incremento = 5
        self.__listCabañas = np.empty(self.__dimension, Cabaña)

    def agregarCabaña(self, nuevaCabaña):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listCabañas.resize(self.__dimension)
        self.__listCabañas[self.__cantidad] = nuevaCabaña
        self.__cantidad += 1

    def leedatos(self):
        bandera = True
        archivo = open('Cabañas.csv')
        reader = csv.reader(archivo, delimiter = ';')
        for fila in reader:
            if bandera:
                bandera = False
            else:
                self.agregarCabaña(Cabaña(int(fila[0]), int(fila[1]), int(fila[2]), int(fila[3]), float(fila[4])))
        archivo.close()

    def buscaCabañasDispos(self, GR):
        cant = int(input("Ingrese cantidad de huéspedes: "))
        for 