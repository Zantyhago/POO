from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from functools import partial
import random
import time
import json
from datetime import datetime

class Aplicacion:
    __ventana: object
    __secuencia: list
    __marcador = int
    __mayorPtn: int
    __contador: int
    __jinicial: bool
    # __listaBotones: list
    __colours: list
    __Verdebtn: object
    __Amarillobtn: object
    __Rojobtn: object
    __Azulbtn: object
    __Iniciarbtn: object
    __texto: object
    __textoLoose: object
    __Quitbtn: object
    __Reiniciarbtn: object

    def __init__(self):
        self.__ventana = tk.Tk()
        self.__ventanaGameOver = tk.Tk()
        self.__secuencia = []
        self.__marcador = 0
        self.__mayorPtn = 0
        self.__contador = 0
        self.__jinicial = False
        # self.__listaBotones = [self.__Verdebtn, self.__Amarillobtn, self.__Rojobtn, self.__Azulbtn]
        self.__colours = ['#00DD00','#FFFF00','#FF0000','#0000FF'] # en el mismo orden; verde, amarillo,rojo, azul
        self.__ventana.title("Py-SimonGame")
        self.__ventana.geometry("350x550")
        self.LauncherBotons()
        self.__ventana.mainloop()

    def LauncherBotons(self):
        self.__Verdebtn = Button(self.__ventana, command = partial(self.press, "Verde"), background = self.__colours[0], relief = "raised")
        self.__Verdebtn.place(relx = 0.265, rely = 0.3, anchor = tk.CENTER, relwidth = 0.43, relheight = 0.43)
        self.__Amarillobtn = Button(self.__ventana, command = partial(self.press, "Verde"), background = self.__colours[1], relief = "raised")
        self.__Amarillobtn.place(relx = 0.265, rely = 0.75, anchor = tk.CENTER, relwidth = 0.43, relheight = 0.43)
        self.__Rojobtn = Button(self.__ventana, command = partial(self.press, "Verde"), background = self.__colours[2], relief = "raised")
        self.__Rojobtn.place(relx = 0.735, rely = 0.3, anchor = tk.CENTER, relwidth = 0.43, relheight = 0.43)
        self.__Azulbtn = Button(self.__ventana, command = partial(self.press, "Verde"), background = self.__colours[3], relief = "raised")
        self.__Azulbtn.place(relx = 0.735, rely = 0.75, anchor = tk.CENTER, relwidth = 0.43, relheight = 0.43)
        self.__ventana.grid_rowconfigure(1, weight = 1)
        self.__ventana.grid_rowconfigure(2, weight = 1)       # para que el contenido se adapte al tamaño de la ventana
        self.__ventana.grid_columnconfigure(0, weight = 1)
        self.__ventana.grid_columnconfigure(1, weight = 1)
        self.__Iniciarbtn = Button(self.__ventana, command = self.iniciar, bg = "white", text = "Iniciar", font = ('Arial', 12))
        self.__Iniciarbtn.place(relx = 0.5, rely = 0.53, anchor = tk.CENTER, relwidth = 0.2, relheight = 0.1)
        self.__texto = Label(self.__ventana, text = "Puntaje                         0", font = ('Arial', 15))
        self.__texto.place(relx= 0.5, rely = 0.01,anchor = tk.N)

    def press(self, xcolorPresionado):
        if self.__jinicial == True:     # verifica que el juego inició
            if self.__secuencia >= self.__contador:     # el contador va una posicion adelantada
                if self.__secuencia[self.__contador] == xcolorPresionado:
                    self.__puntaje +=  1
                    self.checkeaTurno()
                    self.__texto.config(text = "Puntaje                         " + str(self.__puntaje), font = ('Arial', 15))
                else:
                    self.gameover()

    def gameover(self):
        #for boton in self.__listaBotones:            
        self.__Verdebtn.unbind("<Button-1>")
        self.__Amarillobtn.unbind("<Button-1>")         # se desvinculan del evento Click para que dejen de sumar en el json después de haber perdido
        self.__Rojobtn.unbind("<Button-1>")
        self.__Azulbtn.unbind("<Button-1>")
        if self.__puntaje > self.__mayorPtn:          # si hace récord se actualiza
            self.__mayorPtn = self.__puntaje
        self.__texto.config(text = "Puntaje                         " + str(self.__puntaje), font = ('Arial', 15))
        self.__ventanaGameOver = Toplevel(self.__ventana)    # crea una ventana hija
        self.__ventanaGameOver.title("Py-SimonGame")
        self.__ventanaGameOver.geometry('350x175')
        self.__textoLoose = Label(self.__ventanaGameOver, text=f"\nGAME OVER")
        self.__textoLoose.pack(pady = 20, padx = 20)
        points = Label(self.__ventanaGameOver, text=f"\nPuntaje: {self.__marcador}")
        points.pack(pady = 10, padx = 10)
        self.__Quitbtn = Button(self.__ventanaGameOver, command = quit, bg = "white", text = "Salir", font = ('Arial', 6))
        self.__Quitbtn.place(relx = 0.5, rely = 0.53, anchor = tk.CENTER, relwidth = 0.2, relheight = 0.1)                                         # TERMINAR DE CONFIGURAR EL PLACE
        self.__Reiniciarbtn = Button(self.__ventanaGameOver, command = self.iniciar, bg = "white", text = "Reintentar", font = ('Arial', 6))
        self.__Reiniciarbtn.place(relx = 0.5, rely = 0.53, anchor = tk.CENTER, relwidth = 0.2, relheight = 0.1)
                    # TERMINAR DE CONFIGURAR EL PLACE

    def iniciar(self):
        self.__contador = 0
        self.__puntaje = 0
        self.__secuencia = []
        self.__jinicial = True
        self.__texto.config(text = "Puntaje                         " + str(self.__puntaje), font = ('Arial', 15))
        self.createColor()
        self.__Iniciarbtn.destroy()

    def checkeaTurno(self):
        if len(self.__secuencia) == self.__puntaje:
            self.__contador = 0
            self.__puntaje += 1
            self.__Iniciarbtn.after(1000, self.createColor)

    def createColor(self):
        pass

    def cambio(self, xboton, xcolorInic):
        pass

obj = Aplicacion()