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
        try:
           with open('C:\\Users\\Vaf_Tecnology\\Desktop\\Santy\\Programación Oprientada a Objetos\\Unidad 3\\Parcial 2\\Tema 1\productos.csv') as archivo:
                reader = csv.reader(archivo, delimiter = ';')
                next(reader)
                for fila in reader:
                    if fila[0] == 'C':
                        pechi = Congelado(fila[1], fila[2], fila[3], float(fila[4]), fila[5], (fila[6]), float(fila[7]), float(fila[8]), float(fila[9]), float(fila[10]), float(fila[11]), fila[12])
                        self.agregaProducto(pechi)
                    elif fila[0] == 'R':
                        refrigerado = Refrigerado(fila[1], fila[2], fila[3], float(fila[4]), fila[5], (fila[6]), float(fila[7]), (fila[8]))
                        self.agregaProducto(refrigerado)
                    else:
                        raise AssertionError
        except FileNotFoundError as e:
                print(e)
        except AssertionError:
                print('No se leyo un producto correctamente.')
        else:
            print('Se leyo "productos.csv" correctamente.')
            archivo.close()
    
    def leeDatosManu(self):
        try:
            xtipo = input("Ingrese tipo del producto (R - C): ")
            #assert len(xtipo) == 1, "El tipo se indica con caracter."
            xnom = input("Ingrese nombre del producto: ")
            xfechaE = input("Ingrese fecha de envase: ")
            xfechaV = input("Ingrese fecha de vencimiento: ")
            xtemp = float(input("Ingrese temperatura: "))
            xpais = input("Ingrese pais de origen: ")
            xnum = input("Ingrese numero de serie: ")
            xcostoBase = float(input("Ingrese costo base: "))
            if xtipo.lower() == 'c':
                xporcN = float(input("Ingrese porcentaje de Nitrogeno: "))
                xporcO = float(input("Ingrese porcentaje de Oxigeno: "))
                xporcCO = float(input("Ingrese porcentaje de Dioxido de Carbono: "))
                xporcVap = float(input("Ingrese porcentaje de vapor de agua: "))
                xmetodo = input("Ingrese metodo de congelacion: ")
                producto = Congelado(xnom, xfechaE, xfechaV, xtemp, xpais, xnum, xcostoBase, xporcN, xporcO, xporcCO, xporcVap, xmetodo)
                self.agregaProducto(producto)
            elif xtipo.lower() == 'r':
                xcodigo = int(input("Ingrese codigo del supervisor: "))
                producto = Refrigerado(xnom, xfechaE, xfechaV, xtemp, xpais, xnum, xcostoBase, xcodigo)
                self.agregaProducto(producto)
        except ValueError:
            print("Error: Por favor, ingrese un valor válido.")
        else:
            print("Se agregó el producto correctamente.")

    def muestraType(self):
        xpos = int(input("Ingrese posicion del producto: "))
        if xpos < 0 and xpos >= len(self.__ListaProds):
            raise IndexError('Indice fuera de rango.')
        else:
            if isinstance(self.__ListaProds[xpos-1], Congelado):
                print(f"El producto en la posicion {xpos} es de tipo Congelado.")
            elif isinstance(self.__ListaProds[xpos-1], Refrigerado):
                print(f"El producto en la posicion {xpos} es de tipo Refrigerado.")
            else:
                raise TypeError
    
    def determinarClaseDeObjetos(self):
        cantR = 0
        cantC = 0
        for producto in self.__ListaProds:
            if isinstance(producto, Refrigerado):
                cantR += 1
            elif isinstance(producto, Congelado):
                cantC += 1
        print('Cantidad de productos refrigerados: ', cantR)
        print('Cantidad de productos congelados: ',cantC)

    def muestraDatas(self):
        for producto in self.__ListaProds:
            print(producto)