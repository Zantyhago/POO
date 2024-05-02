from clasetrans import Transaccion
import csv
class Gtrans:
    __Ltrans:list

    def __init__(self):
        self.__Ltrans=[]
    
    def agregar(self,nuevo):
        self.__Ltrans.append(nuevo)

    def leerdato(self):
        archivo=open('tranccionesBilletera.csv')
        reader=csv.reader(archivo, delimiter=';')
        band=True
        for fila in reader:
            if band:
                band=False
            else:
                cvu=fila[0]
                num=fila[1]
                imp=float(fila[2])
                tipo=fila[3]
                unatran=Transaccion(cvu,num,imp,tipo)
                self.agregar(unatran)
        archivo.close()

    def calcular(self, xcvu):   #para el d
        i, sum = 0
        while i< len(self.__Ltrans):
            if xcvu == self.__Ltrans[i].getcvu():
               sum += self.__Ltrans[i].getimp()
            i += 1
        return sum