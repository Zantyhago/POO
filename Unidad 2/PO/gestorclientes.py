import csv
from classcliente import Cliente
class GestorCliente:
    __listaCli: list

def __init__(self):
    self.__listaCli = []

def agrega(self, nuevocli):
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
            
def actualiza(self, xdni):
        bandera = True
        while i < len(self.__lista) and bandera:
             if 