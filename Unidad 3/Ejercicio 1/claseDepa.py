class Departamento:
    __id: int
    __nyaProp: str
    __numPis: int
    __numDepa: int
    __cantHabi: int
    __cantBañ: int
    __superficie: float

    def __init__(self, xid, xnya, xnumpis, xnumdepa, xcantHab, xcantBañ, xsup):
        self.__id = xid
        self.__nyaProp = xnya
        self.__numPis = xnumpis
        self.__numDepa = xnumdepa
        self.__cantHabi = xcantHab
        self.__cantBañ = xcantBañ
        self.__superficie = xsup        

    def getID(self):
        return self.__id
    
    def getNyA(self):
        return self.__nyaProp
    
    def getNumPis(self):
        return self.__numPis
    
    def getNumDepa(self):
        return self.__numDepa
    
    def getCantHabs(self):
        return self.__cantHabi
    
    def getCantBaños(self):
        return self.__cantBañ
    
    def getSuperf(self):
        return self.__superficie