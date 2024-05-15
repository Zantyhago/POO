from ClaseMov import Movimiento
import numpy as np
import csv

class gestorMov:
    #agregado
    __cantidad: int
    __dimension: int
    __incremento: int
    #agregado
    __list_gest: np.ndarray

    def __init__ (self):
        #agregado
        self.__cantidad = 0
        self.__dimension = 21
        self.__incremento = 5
        #agregado
        self.__list_gest = np.empty(self.__dimension, dtype=Movimiento)
    
    def __lt__ (self, unMov):
        return self.__list_gest() < unMov.getNro_cta()

    def agregarMov(self, unMov):
        #agregado
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__list_gest.resize(self.__dimension)
        self.__list_gest[self.__cantidad] = unMov
        self.__cantidad += 1
        #agregado

    def leerdatos(self):
        archivo = open('MovimientosAbril2024.csv')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
               self.agregarMov(Movimiento(int(fila[0]), fila[1], fila[2], fila[3], float(fila[4])))
        archivo.close()

    #agregado
    def existenMovimientos_porNumCuenta(self, xnum_C):
        existe = False
        i = 0
        while i < self.__cantidad and existe is False:
            if self.__list_gest[i].getNro_cta() == xnum_C:
                existe = True
            else:
                i += 1
        return existe
    
    def ordenarMov(self):
        self.__list_gest = np.sort(self.__list_gest)
        print("Los movimientos fueron ordenados por números de cuenta.")

    def listarMov(self):
        for unMov in self.__list_gest:
            print(unMov)

    def buscarNoMov(self, xDNI):
        i = 0
        while i<len(self.__list_gest):
            if xDNI == self.__list_gest[i].getDni():
                if self.__list_gest[i] == None:
                    return self.__list_gest.getNom
            else:
                i += 1
        