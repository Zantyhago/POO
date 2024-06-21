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
        self.__secuencia = []
        self.__puntaje = 0
        self.__mayorPtn = 0
        self.__contador = 0
        self.__jinicial = False
        #self.__listaBotones = [self.__Verdebtn, self.__Amarillobtn, self.__Rojobtn, self.__Azulbtn]
        self.__colours = ["Verde", "Amarillo", "Rojo", "Azul"]
        self.__ventana.title("Py-SimonGame")
        self.__ventana.geometry("350x550")
        self.LauncherBotons()
        self.__ventana.mainloop()

    def LauncherBotons(self):
        self.__Verdebtn = tk.Canvas(self.__ventana, width=230, height=300, bg = "#00DD00")
        self.__Verdebtn.bind("<Button-1>", lambda event: self.press("Verde"))
        self.__Verdebtn.place(relx = 0.265, rely = 0.3, anchor = tk.CENTER, relwidth = 0.43, relheight = 0.43)
        self.__Amarillobtn = tk.Canvas(self.__ventana, width=230, height=300, bg = "#FFFF00")
        self.__Amarillobtn.bind("<Button-1>", lambda event: self.press("Amarillo"))
        self.__Amarillobtn.place(relx = 0.265, rely = 0.75, anchor = tk.CENTER, relwidth = 0.43, relheight = 0.43)
        self.__Rojobtn = tk.Canvas(self.__ventana, width=230, height=300, bg = "#FF0000")
        self.__Rojobtn.bind("<Button-1>", lambda event: self.press("Rojo"))
        self.__Rojobtn.place(relx = 0.735, rely = 0.3, anchor = tk.CENTER, relwidth = 0.43, relheight = 0.43)
        self.__Azulbtn = tk.Canvas(self.__ventana, width=230, height=300, bg = "#0000FF")
        self.__Azulbtn.bind("<Button-1>", lambda event: self.press("Azul"))
        self.__Azulbtn.place(relx = 0.735, rely = 0.75, anchor = tk.CENTER, relwidth = 0.43, relheight = 0.43)
        self.__ventana.grid_rowconfigure(1, weight = 1)
        self.__ventana.grid_rowconfigure(2, weight = 1)       # para que el contenido se adapte al tamaño de la ventana
        self.__ventana.grid_columnconfigure(0, weight = 1)
        self.__ventana.grid_columnconfigure(1, weight = 1)
        self.__Iniciarbtn = Button(self.__ventana, command = self.iniciar, bg = "white", text = "Iniciar", font = ('Arial', 12))
        self.__Iniciarbtn.place(relx = 0.5, rely = 0.53, anchor = tk.CENTER, relwidth = 0.2, relheight = 0.1)
        self.__texto = Label(self.__ventana, text = "Puntaje                         0", font = ('Arial', 15))
        self.__texto.place(relx= 0.5, rely = 0.01,anchor = tk.N)

    def iniciar(self):
        self.__contador = 0
        self.__puntaje = 0
        self.__secuencia = []
        self.__jinicial = True
        self.__texto.config(text = "Puntaje                         " + str(self.__puntaje), font = ('Arial', 15))
        self.__Iniciarbtn.destroy()
        self.createColor()

    def createColor(self):
        if self.__jinicial == True:
            i = 0
            while i < len(self.__secuencia):
                messagebox.showinfo("damn","funca el while")
                if self.__secuencia[i] == "Verde":
                    self.cambioColor(self.__Verdebtn, "pink", "#00DD00")
                elif self.__secuencia[i] == "Amarillo":
                    self.cambioColor(self.__Amarillobtn, "pink", "#FFFF00")
                elif self.__secuencia[i] == "Rojo":
                    self.cambioColor(self.__Rojobtn, "pink", "#FF0000")
                elif self.__secuencia[i] == "Azul":
                    self.cambioColor(self.__Azulbtn, "pink", "#0000FF")
                i += 1
                time.sleep(0.1)
            xnum = random.randrange(0,4)
            self.__secuencia.append(self.__colours[xnum])
            if self.__secuencia[i] == "Verde":
                self.cambioColor(self.__Verdebtn, "pink", "#00DD00")
            elif self.__secuencia[i] == "Amarillo":
                self.cambioColor(self.__Amarillobtn, "pink", "#FFFF00")
            elif self.__secuencia[i] == "Rojo":
                self.cambioColor(self.__Rojobtn, "pink", "#FF0000")
            elif self.__secuencia[i] == "Azul":
                self.cambioColor(self.__Azulbtn, "pink", "#0000FF")

    def cambioColor(self, xboton, xcolorCamb, xcolorInic):
        xboton.configure(bg = xcolorCamb)
        xboton.after(500, partial(xboton.configure, bg = xcolorInic))

    def press(self, xcolorPresionado):
        if self.__jinicial == True:     # verifica que el juego inició
            if len(self.__secuencia) >= self.__contador - 1:     # el contador va una posicion adelantada
                if self.__secuencia[self.__contador] == xcolorPresionado:
                    self.__puntaje +=  1
                    self.checkeaTurno()
                    self.__texto.config(text = "Puntaje                         " + str(self.__puntaje), font = ('Arial', 15))
                else:
                    self.gameover()
    
    def checkeaTurno(self):
        if len(self.__secuencia) == self.__contador:
            self.__contador = 0
            self.__puntaje += 1
            self.__Iniciarbtn.after(1000, self.createColor)

    def gameover(self):
        #for boton in self.__listaBotones:            
        self.__Verdebtn.unbind("<Button-1>")
        self.__Amarillobtn.unbind("<Button-1>")         # todos los botones se desvinculan del evento Click para que dejen de sumar después de haber perdido
        self.__Rojobtn.unbind("<Button-1>")
        self.__Azulbtn.unbind("<Button-1>")
        if self.__puntaje > self.__mayorPtn:          # si hace récord se actualiza
            self.__mayorPtn = self.__puntaje
        self.__texto.config(text = "Puntaje                         " + str(self.__puntaje), font = ('Arial', 15))
        self.__ventanaGameOver = Toplevel(self.__ventana)
        self.__ventanaGameOver.title("Py-SimonGame")
        self.__ventanaGameOver.geometry('350x175')
        self.__textoLoose = Label(self.__ventanaGameOver, text=f"\nGAME OVER")
        self.__textoLoose.pack(pady = 20, padx = 20)
        points = Label(self.__ventanaGameOver, text=f"\nPuntaje: {self.__puntaje}")
        points.pack(pady = 10, padx = 10)
        self.__Quitbtn = Button(self.__ventanaGameOver, command = quit, bg = "white", text = "Salir", font = ('Arial', 10))
        self.__Quitbtn.place(relx = 0.55, rely = 0.435, anchor = tk.W, relwidth = 0.2, relheight = 0.15)
        self.__Reiniciarbtn = Button(self.__ventanaGameOver, command = self.reiniciar, bg = "white", text = "Reintentar", font = ('Arial', 10))
        self.__Reiniciarbtn.place(relx = 0.45, rely = 0.435, anchor = tk.E, relwidth = 0.2, relheight = 0.15)

    def reiniciar(self):
        self.__jinicial == False
        self.__ventanaGameOver.destroy()
        self.__Iniciarbtn.after(1000, self.iniciar)

obj = Aplicacion()