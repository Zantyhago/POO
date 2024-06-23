from classJugador import Jugador
from datetime import datetime
import json

class GestorJugador:
    __listaJugadores: list

    def __init__(self):
        self.__listaJugadores = []

    def agregar(self, xjugador):
        self.__listaJugadores.append(xjugador)
        
    def obtenerPuntajes(self):
        with open('psymonpuntajes.json', 'r',encoding = 'utf-8') as archivo:
            datosJugadores = json.load(archivo)
            for dato in datosJugadores:
                xjugador = Jugador(dato['Jugador'], dato['Fecha'], dato['Hora'], dato['Puntaje'])
                self.agregar(xjugador)

    def getlista(self):
        return self.__listaJugadores

    def ordenar(self):
        self.__listaJugadores.sort(reverse = True)