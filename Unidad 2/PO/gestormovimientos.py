import csv
import numpy as np
from classmove import Movimiento
class GestorMovimiento:
    __listaMov: list
def __init__(self, nuevomov):
    self.__listaMov = []

def agrega(self, nuevomov):
    archivo = open("MovimientosAbril2024.csv")
    reader = csv.archivo(delimiter = ';')
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
