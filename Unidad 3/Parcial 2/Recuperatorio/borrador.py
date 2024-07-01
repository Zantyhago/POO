import csv
#from classNodo import Nodo

class Nodo:
    __plan: Plan
    __siguiente: object

    def __init__(self, xplan):
        self.__plan = xplan
        self.__siguiente = None
    
    def setSiguiente(self, xsiguiente):
        self.__siguiente = xsiguiente

    def getSiguiente(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__plan
    
class borrador:
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
            archivo = open('planes.csv')
            reader = csv.reader(archivo, delimiter = ';')
            bandera = True            
            for fila in reader:
                if bandera:
                    bandera = False
                else:
                    if fila[0] == 'M':
                       self.agregarPlan(clase(fila[1], int(fila[2]), fila[3], float(fila[4]), fila[5], int(fila[6])))
                    elif fila[0] == 'T':
                        self.agregarPlan(clase2(fila[1], int(fila[2]), fila[3], float(fila[4]), int(fila[5]), int(fila[6])))
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
    
    def eliminarPorDNI(self, dni):
        aux=self.__comienzo
        encontrado = False
        if aux.getDato().getDNI()==dni:
            encontrado=True
            print('Encontrado y eliminado:\n'+str(aux.getDato()))
            self.__comienzo = aux.getSiguiente()
            self.__tope-=1
            del aux
        else:
            ant = aux
            aux = aux.getSiguiente()
            while not encontrado and aux != None:
                if aux.getDato().getDNI()==dni:
                    encontrado=True
                else:
                    ant = aux
                    aux=aux.getSiguiente()
            if encontrado:
                print(f'Encontrado y eliminado: {str(aux.getDato())}\n')
                ant.setSiguiente(aux.getSiguiente())
                self.__tope-=1
                del aux
            else:
                print(f'El DNI {dni} no está en la lista')
    
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