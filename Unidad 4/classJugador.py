from datetime import datetime
class Jugador:
    __Nickname: str
    __Fecha: datetime
    __Hora: datetime
    __Puntaje: int

    def __init__(self, xnick, xfecha, xhora, xpuntaje):
        self.__Nickname = xnick
        self.__Fecha = xfecha
        self.__Hora = xhora
        self.__Puntaje = xpuntaje
    
    def __str__(self):
        return (f'{self.__Nickname}'
                f'{self.__Fecha} '
                f'{self.__Hora}'
                f'{self.__Puntaje}')
    
    def getNick(self):
        return self.__Nickname
    
    def getFecha(self):
        return self.__Fecha
    
    def getHora(self):
        return self.__Hora
    
    def getPuntaje(self):
        return self.__Puntaje
    
    def __gt__(self, otro):
        return self.__Puntaje > otro.__Puntaje