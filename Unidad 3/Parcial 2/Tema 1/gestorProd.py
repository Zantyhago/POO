from classProducto import Producto
from classProdCong import Congelado
from classProdRefrig import Refrigerado
import csv

class GestorProducto:
    __ListaProds: list

    def __init__(self):
        self.__ListaProds = []

    def agregaProducto(self, nuevoProductito):
        self.__ListaProds.append(nuevoProductito)

    def leeDatos(self):
        archivo = open('C:\\Users\\Vaf_Tecnology\\Desktop\\Santy\\Programación Oprientada a Objetos\\Unidad 3\\Parcial 2\\Tema 1\productos.csv')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
            try:
                if fila[0].lower == 'c':
                    pechi = (Congelado(fila[1], fila[2], fila[3], float(fila[4]), fila[5], (fila[6]), float(fila[7]), float(fila[8]), float(fila[9]), float(fila[10]), float(fila[11]), fila[12]))
                    self.agregaProducto(pechi)
                elif fila[0].lower == "r":
                    refrigerado = (Refrigerado(fila[1], fila[2], fila[3], float(fila[4]), fila[5], (fila[6]), float(fila[7]), (fila[8])))
                    self.agregaProducto(refrigerado)
                else:
                    raise AssertionError
            except FileNotFoundError as e:
                print(e)
            except AssertionError:
                print('Se leyo un producto de tipo desconocido.')
            else: print('Se leyo "productos.csv" correctamente.')
        archivo.close()
    
    def leeDatosManu(self):
        
