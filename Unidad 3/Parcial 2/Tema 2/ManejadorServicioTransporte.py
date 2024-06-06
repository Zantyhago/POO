from ClaseAutobus import Autobus
from ClaseVan import Van
import csv

class ManejadorServicioTransporte:
    __listaServicioTransporte: list
    
    def __init__(self):
        self.__listaServicioTransporte = []
        
    def AgregarServicioTransporte(self, st):
        self.__listaServicioTransporte.append(st)

    def CargaServicioTransporte(self):
        archivo = open("vehiculos.csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera = True
        for linea in reader:
            if bandera:
                bandera = False
            else:
                if linea[0] == "A":
                    xautobus = Autobus(linea[1],linea[2],linea[3],linea[4],linea[5],linea[6],linea[7],linea[8],linea[9])
                    self.AgregarServicioTransporte(xautobus)
                else:
                    xvan = Van(linea[1],linea[2],linea[3],linea[4],linea[5],linea[6],linea[7],linea[8])
                    self.AgregarServicioTransporte(xvan)
                    
    def AgregarVehiculoNuevo(self):
        tipo = input("Ingrese el tipo de vehiculo que cargara (Van - Autobus - Terminado para salir): ")
        while tipo != "Terminado":
            if tipo == "Autobus":
                xmarca = input("Ingrese la marca: ")
                xmodelo = input("Ingrese el modelo: ")
                xanio = input("Ingrese año de fabricacion: ")
                xcapacidad = input("Ingrese la capacidad de pasajeros: ")
                xplazas = input("Ingrese el numero de plazas: ")
                xdistancia = input("Ingrese la distancia a recorrer: ")
                xtarifabase= input("Ingrese la tarifa base: ")
                xtipo = input("Ingrese el tipo de servicio: ")
                xturno = input("Ingrese el turno: ")
                xautobus = Autobus(xmarca, xmodelo, xanio, xcapacidad, xplazas, xdistancia, xtarifabase, xtipo, xturno)
                self.AgregarServicioTransporte(xautobus)
            elif tipo == "Van":
                xmarca = input("Ingrese la marca: ")
                xmodelo = input("Ingrese el modelo: ")
                xanio = input("Ingrese año de fabricacion: ")
                xcapacidad = input("Ingrese la capacidad de pasajeros: ")
                xplazas = input("Ingrese el numero de plazas: ")
                xdistancia = input("Ingrese la distancia a recorrer: ")
                xtarifabase= input("Ingrese la tarifa base: ")
                xtipo = input("Ingrese el tipo de carroceria: ")
                xvan = Van(xmarca, xmodelo, xanio, xcapacidad, xplazas, xdistancia, xtarifabase, xtipo)
                self.AgregarServicioTransporte(xvan)
            tipo = input("Ingrese el tipo de vehiculo que cargara (Van - Autobus - Terminado para salir): ")

    def MuestraEnDeterminadaPosicion(self):
        xpos = int(input("Ingrese la posicion de la lista para mostrar el tipo de vehiculo de esa posicion (Ingresar numero comprendido de 0 a 10, si agrega nuevo vehiculo; o de 0 a 9, si no agrego ningun otro vehiculo): "))
        if 0 <= xpos < len(self.__listaServicioTransporte):
            tipo = ""
            if isinstance(self.__listaServicioTransporte[xpos], Autobus):
                tipo = "Autobus"
            else:
                tipo = "Van" 
            print("El tipo de vehículo en la posición {} es: {} \n".format(xpos, tipo))
        else:
            print("La posición ingresada está fuera del rango de la lista.\n")    
            
    def CantVehiculosTipo(self):
        contadorAutobus = 0
        contadorVan = 0
        for st in self.__listaServicioTransporte:
            if isinstance(st, Autobus):
                contadorAutobus += 1
            else:
                contadorVan += 1
        print("HAY {} vehiculos de tipo Autobus, y hay {} vehiculos de tipo Van".format(contadorAutobus,contadorVan))
        
    def ListadoDeTodosLosVehiculos(self): #modelo, año fabricacion, capacidad passajeros, tarifa total
        for st in self.__listaServicioTransporte:
            tarifaTotal = st.CalculaTarifaServicio()
            print("MODELO: {}   ANIO FABRICACION: {}    CAPACIDAD PASAJEROS: {}      TARIFA TOTAL: {}".format(st.getModelo(),st.getAnio(),st.getCapacidadpasajeros(),tarifaTotal))