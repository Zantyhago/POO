from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from functools import partial
import random
import time
import json
import os
from datetime import datetime
from gestorJugador import GestorJugador

class Aplicacion:
    __ventana: object
    __ventanaGameOver: object
    __ventanaUser: object
    __secuencia: list
    __puntaje: int
    __contador: int
    __jinicial: bool
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
    __labelUser: object
    __entryUsername: object
    __Username: str
    __datosUser: list
    __barraMenu: object
    __ventanaPuntajes: object
    __LFPuntajes: object

    def __init__(self):
        self.__ventana = tk.Tk()
        self.__ventanaUser = Toplevel(self.__ventana)
        self.__ventanaUser.title("Py-SimonGame")
        self.__ventanaUser.geometry('350x150')
        self.__secuencia = []
        self.__puntaje = 0
        self.__contador = 0
        self.__jinicial = False
        self.__colours = ["Verde", "Amarillo", "Rojo", "Azul"]
        self.__ventana.title("Py-SimonGame")
        self.__ventana.geometry("350x550")
# iteracion 3
        self.__barraMenu = Menu(self.__ventana)                 # se crea la barra menu de la ventana
        MenuArchivo = Menu(self.__barraMenu, tearoff = 0)      # se crea un menú desplegable (drop-down menu)
        self.__barraMenu.add_cascade(label = "Puntajes", menu = MenuArchivo)
        MenuArchivo.add_command(label = "Ver puntajes", command = self.mostrarPuntajes)
        MenuArchivo.add_separator()
        MenuArchivo.add_command(label = "Salir", command = self.__ventana.quit)
        self.__ventana.config(menu = self.__barraMenu)
# iteracion 2
        self.__labelUsertxt = tk.Label(self.__ventanaUser, text= 'Datos del Jugador', font = ('Arial', 12))
        self.__labelUsertxt.grid(row = 0, column=0, sticky='w', ipadx = 2, ipady = 2, padx = 5, pady = 5)
        self.__labelUser = tk.Label(self.__ventanaUser, text= 'Jugador', font = ('Arial', 12))
        self.__labelUser.grid(row = 1, column=0, sticky='w', ipadx = 2, ipady = 2, padx = 5, pady = 5)
        self.__entryUsername = tk.Entry(self.__ventanaUser, font=('Arial', 10))
        self.__entryUsername.grid(row = 1, column = 2, sticky = 'w', padx = 5, pady = 5)
        self.__boton_confirmar = tk.Button(self.__ventanaUser, text = 'Continuar', font = ('Arial', 10), command = self.SaveUsername)
        self.__boton_confirmar.grid(row = 2, column = 2, sticky='w', padx = 5, pady = 5)
        self.__ventanaUser.wait_window()

    def SaveUsername(self):
        xuser = self.__entryUsername.get().lstrip().rstrip()
        if xuser:
            self.__Username = xuser
            self.__ventanaUser.destroy()
            self.__texto = Label(self.__ventana, text = str(self.__Username) + "                " + str(self.__puntaje), font = ('Arial', 15))
            self.__texto.place(relx= 0.5, rely = 0.01,anchor = tk.N)
            self.LauncherBotones()
            self.__ventana.mainloop()
        else:
            messagebox.showinfo("¡Error!","El nombre ingresado es inválido.")

    def mostrarPuntajes(self):
        GJ = GestorJugador()
        GJ.obtenerPuntajes()
        GJ.ordenar()
        self.__ventanaPuntajes = Toplevel(self.__ventana)
        self.__ventanaPuntajes.title("Py-SimonGame")
        self.__ventanaPuntajes.geometry('500x250')
        self.__LFPuntajes = tk.LabelFrame(self.__ventanaPuntajes, text='Galería de puntajes:', font = ('Arial', 10), borderwidth = 2, relief = 'raised', padx = 5, pady = 5)
        self.__LFPuntajes.pack(fill = "both", expand= "yes", padx = 10, pady = 10)
        arboleda = ttk.Treeview(self.__LFPuntajes, columns = ("nombreCol", "fechaCol", "horaCol", "puntajeCol"), show = 'headings')
        arboleda.heading("nombreCol", text = "Nombre")
        arboleda.heading("fechaCol", text = "Fecha")
        arboleda.heading("horaCol", text = "Hora")
        arboleda.heading("puntajeCol", text = "Puntaje")
        arboleda.column("nombreCol", width = 50)
        arboleda.column("fechaCol", width = 50)
        arboleda.column("horaCol", width = 50)
        arboleda.column("puntajeCol", width = 50)
        arboleda.pack(fill = "both", expand = True)
        for jugador in GJ.getlista():
            xnombre = jugador.getNick()
            xpuntaje = jugador.getPuntaje()
            xfecha = jugador.getFecha()
            xhora = jugador.getHora()
            arboleda.insert("", tk.END, values = (xnombre, xfecha, xhora, xpuntaje))

    def LauncherBotones(self):
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
        self.__ventana.grid_rowconfigure(2, weight = 1)
        self.__ventana.grid_columnconfigure(0, weight = 1)
        self.__ventana.grid_columnconfigure(1, weight = 1)
        self.__Iniciarbtn = Button(self.__ventana, command = self.iniciar, bg = "white", text = "Iniciar", font = ('Arial', 12))
        self.__Iniciarbtn.place(relx = 0.5, rely = 0.53, anchor = tk.CENTER, relwidth = 0.2, relheight = 0.1)


    def iniciar(self):
        self.__contador = 0
        self.__puntaje = 0
        self.__secuencia = []
        self.__jinicial = True
        self.__texto.config(text = str(self.__Username) + "              " + str(self.__puntaje), font = ('Arial', 15))
        self.__Iniciarbtn.destroy()
        self.createColor()

    def createColor(self):
        if self.__jinicial:
            self.recorreSecuencia(0)

    def recorreSecuencia(self, indice):
        if indice < len(self.__secuencia):
            color = self.__secuencia[indice]
            if color == "Verde":
                self.cambioColor(self.__Verdebtn, "pink", "#00DD00")
            elif color == "Amarillo":
                self.cambioColor(self.__Amarillobtn, "pink", "#FFFF00")
            elif color == "Rojo":
                self.cambioColor(self.__Rojobtn, "pink", "#FF0000")
            elif color == "Azul":
                self.cambioColor(self.__Azulbtn, "pink", "#0000FF")
            self.__ventana.after(800, self.recorreSecuencia, indice + 1)
        else:
            self.agregaColor()

    def agregaColor(self):
        xnum = random.randrange(0, 4)
        self.__secuencia.append(self.__colours[xnum])
        color = self.__secuencia[-1]
        if color == "Verde":
            self.cambioColor(self.__Verdebtn, "pink", "#00DD00")
        elif color == "Amarillo":
            self.cambioColor(self.__Amarillobtn, "pink", "#FFFF00")
        elif color == "Rojo":
            self.cambioColor(self.__Rojobtn, "pink", "#FF0000")
        elif color == "Azul":
            self.cambioColor(self.__Azulbtn, "pink", "#0000FF")

    def cambioColor(self, xboton, xcolorCamb, xcolorInic):
        xboton.configure(bg=xcolorCamb)
        self.__ventana.after(500, lambda: xboton.configure(bg=xcolorInic))


    def press(self, xcolorPresionado):
        if self.__jinicial == True:
            if len(self.__secuencia) >= self.__contador - 1:     # el contador va una posicion adelantada
                if self.__secuencia[self.__contador] == xcolorPresionado:
                    self.__contador +=  1
                    self.checkeaTurno()
                    self.__texto.config(text = str(self.__Username) + "              " + str(self.__puntaje), font = ('Arial', 15))
                else:
                    self.guardarJson()
                    self.gameover()
    
    def checkeaTurno(self):
        if len(self.__secuencia) == self.__contador:
            self.__contador = 0
            self.__puntaje += 1
            self.__Iniciarbtn.after(1000, self.createColor)

    def gameover(self):          
        self.__Verdebtn.unbind("<Button-1>")
        self.__Amarillobtn.unbind("<Button-1>")
        self.__Rojobtn.unbind("<Button-1>")
        self.__Azulbtn.unbind("<Button-1>")
        self.__texto.config(text = str(self.__Username) + "              " + str(self.__puntaje), font = ('Arial', 15))
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

    def guardarJson(self):
        filename = 'psymonpuntajes.json'
        if not os.path.exists(filename):
            with open(filename, 'w+', encoding = 'utf-8') as archivo:
                json.dump([], archivo)
        with open(filename, 'r+', encoding = 'utf-8') as archivo:
            if not archivo.read(1):
                self.__datosUser = []
            else:
                archivo.seek(0)
                self.__datosUser = json.load(archivo)
            self.__datosUser.append(self.diccionarioUser())
            archivo.seek(0)
            json.dump(self.__datosUser, archivo, indent = 4)
            archivo.truncate()

    def diccionarioUser(self):
        fyh = datetime.now()
        fecha = fyh.strftime("%d/%m/%Y")
        hora = fyh.strftime("%H:%M:%S")
        return{
            'Jugador': self.__Username,
            'Fecha': fecha,
            'Hora': hora,
            'Puntaje': self.__puntaje
        }

    def reiniciar(self):
        self.__jinicial == False
        self.__ventanaGameOver.destroy()
        self.__Verdebtn.bind("<Button-1>", lambda event: self.press("Verde"))
        self.__Amarillobtn.bind("<Button-1>", lambda event: self.press("Amarillo"))
        self.__Rojobtn.bind("<Button-1>", lambda event: self.press("Rojo"))
        self.__Azulbtn.bind("<Button-1>", lambda event: self.press("Azul"))
        time.sleep(2)
        self.iniciar()

obj = Aplicacion()
