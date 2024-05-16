from claseDepa import Departamento
class Edificio:
    __id: int
    __nombre: str
    __direccion: str
    __nombEmpre: str
    __cantPisos: int
    __cantDepas: int

    def __init__(self, xid, xnom, xdir, xnomProp, xcantPis, xcantDep):
        self.__id = xid
        self.__nombre = xnom
        self.__direccion = xdir
        self.__nombEmpre = xnomProp
        self.__cantPisos = xcantPis
        self.__cantDepas = xcantDep

    def agregarDepartamento(self, yid, ynya, ynumdepa, ycantHab, ycantBañ, ysup):
        xdemartamento = demartamento(yid, ynya, ynroP, ynroD, ycantD, ycantB, ysup)
        self.__Departamentos.append(xdemartamento)

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