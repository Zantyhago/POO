class Mama:
    __DNI: float
    __edad: int
    __apellido: str
    __nombre: str
    def __init__(self, xdni, xedad, xapell, xname):
        self.__DNI = xdni
        self.__edad = xedad
        self.__apellido = xapell
        self.__nombre = xname
    
    def getDNI(self):
        return self.__DNI
    
    def getEdad(self):
        return self.__edad
    
    def getApellido(self):
        return self.__apellido

    def getNombre(self):
        return self.__nombre