from classTelefonia import Telefonia
from classTelevision import Television
from classNodo import Nodo
import csv as bokita_lo_mejor_que_hay

class GestorPlan:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def getTope(self):
        return self.__tope
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope: 
            self.__actual = self.__comienzo
            self.__indice = 0 
            raise StopIteration 
        else:  
            self.__indice += 1  
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente() 
            return dato
        
    def agregarPlan(self, nuevoPlan):
        nodo = Nodo(nuevoPlan)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def leerDatos(self):
        try:
            archivo = open('C:\\Users\\Vaf_Tecnology\\Desktop\\Santy\\Programación Orientada a Objetos\\Unidad 3\\Parcial 2\\Recuperatorio\planes.csv')
            reader = bokita_lo_mejor_que_hay.reader(archivo, delimiter = ';')
            bandera = True            
            for fila in reader:
                if bandera:
                    bandera = False
                else:
                    if fila[0] == 'M':
                       self.agregarPlan(Telefonia(fila[1], int(fila[2]), fila[3], float(fila[4]), fila[5], int(fila[6])))
                    elif fila[0] == 'T':
                        self.agregarPlan(Television(fila[1], int(fila[2]), fila[3], float(fila[4]), int(fila[5]), int(fila[6])))
        except FileNotFoundError as e:
            print(f"Archivo no encontrado. {e}")
        else:
            print("Se leyó el archivo 'planes.csv correctamente")
            archivo.close()

    def BuscaPorPosicion(self, xpos):
        try:
            if xpos < 0 or xpos >= self.__tope:
                raise IndexError
            aux = self.__comienzo
            i = 0
            while aux is not None and i < xpos:
                aux = aux.getSiguiente()
                i += 1
            if aux is not None:
                xplan = aux.getDato()
                if isinstance(xplan, Telefonia):
                    print(f"EL plan de la posicion {xpos} es de tipo Telefonía.")
                elif isinstance(xpos, Television):
                    print(f"EL plan de la posicion {xpos} es de tipo Televisión.")
        except IndexError:
            print("Índice fuera de rango.")
        except ValueError:
            print("Se esperaba un numero entero.")

    def contarTiposPlanes(self):
        xcobertura = input("Ingrese cobertura geográfica: ")
        aux = self.__comienzo
        i, cant = 0, 0
        while  i <= self.__tope and aux is not None:
            cobertura = aux.getDato().getCoberturaGeo()
            if xcobertura == cobertura:
                cant += 1
            aux = aux.getSiguiente()
            i += 1
        print(f"Hay {cant} planes con esa cobertura geográfica.")

    def cuentaCanalesInters(self):
        xcant = int(input("Ingrese cantidad de canales: "))
        aux = self.__comienzo
        i = 0
        bandera = False
        while i <= self.__tope and aux is not None:
            if isinstance(aux.getDato(), Television):
                if int(aux.getDato().getCantInt()) <= xcant:
                    print(f"{aux.getDato().getNombreComp()} tiene una cantidad mayor o igual a {xcant} de canales")
                    bandera = True
            aux = aux.getSiguiente()
        if bandera is False:
            print(f"No hay planes con {xcant} o más canales.")
    
    def muestraAll(self):
        aux = self.__comienzo
        i = 0
        while i <= self.__tope and aux is not None:
            if isinstance(aux.getDato(), Telefonia):
                tipo = "Telefonia"
            elif isinstance(aux.getDato(), Television):
                tipo = "Television"
            print(f"""
                    Tipo de plan: {tipo}
                {aux.getDato()}""")
            aux = aux.getSiguiente()
            i += 1