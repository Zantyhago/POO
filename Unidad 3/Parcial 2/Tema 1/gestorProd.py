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
        xtipo = input("Ingrese tipo del producto (R - C): ")
        assert len(xtipo) == 1, "El tipo se indica con caracter."
        xnom = input("Ingrese nombre del producto: ")
        xfechaE = input("Ingrese fecha de envase: ")
        xfechaV = input("Ingrese fecha de vencimiento: ")
        xtemp = float(input("Ingrese temperatura: "))
        xpais = input("Ingrese pais de origen: ")
        xnum = input("Ingrese numero de serie: ")
        xcostoBase = float(input("Ingrese costo base: "))
        try:
            if xtipo.lower == 'c':
                xporcN = float(input("Ingrese porcentaje de Nitrogeno: "))
                xporcO = float(input("Ingrese porcentaje de Oxigeno: "))
                xporcCO = float(input("Ingrese porcentaje de Dioxido de Carbono: "))
                xporcVap = float(input("Ingrese porcentaje de vapor de agua: "))
                xmetodo = input("Ingrese metodo de congelacion: ")
                pechi = (Congelado(xnom, xfechaE, xfechaV, xtemp, xpais, xnum, xcostoBase, xporcN, xporcO, xporcCO, xporcVap, xmetodo))
            elif xtipo.lower == 'r':
                
                refri = (Refrigerado(xnom, xfechaE, xfechaV, xtemp, xpais, xnum, xcostoBase, xporcN, xporcO, xporcCO, xporcVap, xmetodo))
                
