from nodo import Nodo
from classPlanTelef import Telefonia
from classPlanTelev import Television
import csv

class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            plan = self.__actual.getPlan()
            self.__actual = self.__actual.get_siguiente()
            return plan
        
    def agregarPlanes(self, nuevoPlan):
        nodo = Nodo(nuevoPlan)
        nodo.set_siguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def leeDatos(self):
        archivo = open('planes.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            if fila[0] == 'M':
                nombcompania, duracion, cobertura, precio, tipo, cantmins = fila
                telef = Telefonia(nombcompania, duracion, cobertura, precio, tipo, cantmins)
                self.agregarPlanes(telef)
            elif fila[0] == 'T':
                nombcompania, duracion, cobertura, precio, cantnac, cantint = fila
                telev = Telefonia(nombcompania, duracion, cobertura, precio, cantnac, cantint)
                self.agregarPlanes(telev)
            else:
                TypeError
            