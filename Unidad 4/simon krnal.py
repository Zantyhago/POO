from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
from datetime import datetime
import json

class Aplicacion:
    __ventana: object
    __secuencia: list
    __marcador = IntVar
    __mayorPtn: int
    __contador: int
    __jinicial: bool
    __colours: list
    __Verdebtn: object
    __Amarillobtn: object
    __Rojobtn: object
    __Azulbtn: object

    def __init__(self):
        self.__ventana = tk.Tk()
        self.__secuencia = []
        self.__marcador = IntVar(value = 0)
        self.__mayorPtn = 0
        self.__contador = 0
        self.__jinicial = False
        self.__colours = ['#00DD00','#FFFF00','#FF0000','#0000FF'] # en el mismo orden: verde, amarillo,rojo, azul
        self.__ventana.title("Py-SimonGame")
        self.__ventana.geometry("500x500")
        self.LauncherBotons()
        self.__ventana.mainloop()

    def LauncherBotons(self):
        self.__Verdebtn = Button(self.__ventana, command = lambda: self.press("Verde"), height = 7, width = 14, bg = "green")
        self.__Verdebtn.grid(column = 1, row=1, sticky = 'nswe', ipady=50, ipadx = 50, padx = 10, pady = 10)
        self.__Amarillobtn = Button(self.__ventana, command = lambda: self.press("Amarillo"), height = 7, width = 14, bg = "yellow")
        self.__Amarillobtn.place()
        self.__Rojobtn = Button(self.__ventana, command = lambda: self.press("Rojo"), height = 7, width = 14, bg = "red")
        self.__Azulbtn = Button(self.__ventana, command = lambda: self.press("Azul"), height = 7, width = 14, bg = "blue")