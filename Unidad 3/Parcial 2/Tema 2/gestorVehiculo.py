from classAutobus import Autobus
from classVan import Van
import csv

class GestorVehiculo:
    __listaVehiculos: list

    def __init__(self):
        self.__listaVehiculos = []

    def agregaVehiculo(self, nuevoVehiculo):
        self.__listaVehiculos.append(nuevoVehiculo)

    def leeDatos(self):
        try:
            archivo = open('C:\\Users\\Vaf_Tecnology\\Desktop\\Santy\\Programación Orientada a Objetos\\Unidad 3\\Parcial 2\\Tema 2\Vehiculos.csv')
            reader = csv.reader(archivo, delimiter = ';')
            bandera = True
            for fila in reader:
                if bandera:
                    bandera = False
                else:
                    if fila[0] == 'A':
                        self.agregaVehiculo(Autobus(fila[1], fila[2], int(fila[3]), int(fila[4]), int(fila[5]), float(fila[6]), float(fila[7]), fila[8], fila[9]))
                    else:
                        self.agregaVehiculo(Van(fila[1], fila[2], int(fila[3]), int(fila[4]), int(fila[5]), float(fila[6]), float(fila[7]), fila[8]))
        except FileNotFoundError as e:
            print(f"Error al abrir el archivo: {e}")
        except SyntaxError as e:
            print(f"Que carajo pasó: {e}")
        except ValueError as e:
            print(f"No se leyó el archivo correctametne: {e}")
        else:
            print(f"Se cargaron los datos correctamente desde 'Vehiculos.csv'.")
            archivo.close()
    
    def agregaVehiculoManualmente(self):
        try:
            bandera = True
            while bandera:
                    xmarca = input("Ingrese la marca: ")
                    xmodelo = input("Ingrese el modelo: ")
                    xanyo = int(input("Ingrese año de fabricacion: "))
                    xcapacidad = int(input("Ingrese la capacidad de pasajeros: "))
                    xplazas = int(input("Ingrese el numero de plazas: "))
                    xdistancia = float(input("Ingrese la distancia a recorrer: "))
                    xtarifabase = float(input("Ingrese la tarifa base: "))
                    xtipoVeh = input("Ingrese tipo de Vehiculo: ")
                    if xtipoVeh.lower() == "autobus":
                        xtiposerv = input("Ingrese el tipo de servicio: ")
                        xturno = input("Ingrese el turno: ")
                        self.agregaVehiculo(Autobus(xmarca, xmodelo, xanyo, xcapacidad, xplazas, xdistancia, xtarifabase, xtiposerv, xturno))
                    else:
                        xtipocarr = input("Ingrese tipo de carroecería: ")
                        self.agregaVehiculo(Van(xmarca, xmodelo, xanyo, xcapacidad, xplazas, xdistancia, xtarifabase, xtipocarr))
                    op = input("¿Desea agregar más vehiculos? (No para terminar): ")
                    if op.lower() == "no":
                        bandera = False
        except ValueError as e:
            print(f"Dato mal ingresado: {e}. Intente nuevamente.")
        else:
            print("Vehículo/s agregado/s satisfactoriamente.")
    
    def buscaPosicion(self):
        try:
            xpos = int(input("Ingrese posicion: "))
            if isinstance(self.__listaVehiculos[xpos - 1], Autobus):
                print(f"El vehículo en la posicion {xpos} es de tipo Autobus.")
            elif isinstance(self.__listaVehiculos[xpos - 1], Van):
                print(f"El vehículo en la posicion {xpos} es de tipo Van.")
        except ValueError as e:
            print(f"Se esperaba un entero. {e}.")
        except IndexError as e:
            print(f"La posición {xpos} está fuera de rango. {e}.")
    
    def cuentaTipos(self):
        contA, contV, i = 0, 0, 0
        while i < len(self.__listaVehiculos):
            if isinstance(self.__listaVehiculos[i], Autobus):
                contA += 1
            elif isinstance(self.__listaVehiculos[i], Van):
                contV += 1
            i += 1
        print(f"La cantidad de autobuses es de {contA}.")
        print(f"La cantidad de vanes(?) es de {contV}.")

    def muestraVehiculos(self):
        for vehiculo in self.__listaVehiculos:
            print(vehiculo)