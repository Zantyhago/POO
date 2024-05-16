from claseDepa import Departamento
from claseEdif import Edificio
import csv

class GestEdificio:
    __listaEdifs: list

    def __init__(self):
        self.__listaEdifs = []

    def agregar(self, nuevoEdif):
        self.__listaEdifs.append(nuevoEdif)

    