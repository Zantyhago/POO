from claseDepa import Departamento
class Edificio:
    __id: int
    __nombre: str
    __direccion: str
    __nombEmpre: str
    __cantPisos: int
    __cantDepas: int
    __listaDepas: list

    def __init__(self, xid, xnom, xdir, xnomProp, xcantPis, xcantDep):
        self.__id = xid
        self.__nombre = xnom
        self.__direccion = xdir
        self.__nombEmpre = xnomProp
        self.__cantPisos = xcantPis
        self.__cantDepas = xcantDep
        self.__listaDepas = []

    def agregarDepa(self, yid, ynya, ynumpiso, ynumdepa, ycantHab, ycantBañ, ysup):
        xdepartamento = Departamento(yid, ynya, ynumpiso, ynumdepa, ycantHab, ycantBañ, ysup)
        self.__listaDepas.append(xdepartamento)

    def muestraPropsDepas(self):
        print("Departametos y sus Dueños:")
        for depa in self.__listaDepas:
            print(f"ID del Departamento: {depa.getID()}, Nombre propietario: {depa.getNyA()}")

    def getID(self):
        return self.__id
    
    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getNombEmpresa(self):
        return self.__nombEmpre
    
    def getCantPisos(self):
        return self.__cantPisos
    
    def getCantDeps(self):
        return self.__cantDepas