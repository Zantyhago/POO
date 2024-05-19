from claseDepa import Departamento
from claseEdif import Edificio
import csv

class GestEdificio:
    __listaEdifs: list

    def __init__(self):
        self.__listaEdifs = []

    def agregarEdif(self, nuevoEdif):
        self.__listaEdifs.append(nuevoEdif)

    def cargadatos(self):
        archivo = open('EdificioNorte.csv')
        reader = csv.reader(archivo, delimiter=';')
        aux = 0
        for fila in reader:
            if fila[0] != aux:
                xedif =  Edificio(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]), int(fila[5]))
                self.agregarEdif(xedif)
                aux = fila[0]
            else:
                xedif.agregarDepa(int(fila[1]), fila[2], int(fila[3]), int(fila[4]), int(fila[5]), int(fila[6]), float(fila[7]))
    
    def buscaedificio(self, xnomedif):
        i = 0
        bandera = True
        while i < len(self.__listaEdifs) and bandera:
            if xnomedif == self.__listaEdifs[i].getNombre():
                bandera = False
            else:
                i += 1
        if bandera is False:
            self.__listaEdifs[i].muestraPropsDepas()
        assert bandera is False

    def muestraSupTotal(self, xid):
        i = 0
        bandera = True
        while i < len(self.__listaEdifs) and bandera:
            if xid == self.__listaEdifs[i].getID():
                