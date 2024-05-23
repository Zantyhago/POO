from classNac import Nacimiento
import csv
class GestorNacimiento:
    __listaNacis: list

    def __init__(self):
        self.__listaNacis = []

    def leerdatos(self, nuevaNac):
        archivo = open('Nacimientos.csv')
        reader = csv.reader(archivo, delimiter = ';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                self.nuevaNac(Nacimiento(float(fila[0]), fila[1], fila[2], fila[3], float(fila[4], int(fila[5]))))
        archivo.close()
    
    def buscaPosMama(self, xdni):
        i = 0
        bandera = True
        while i < len(self.__listaNacis) and bandera:
            if self.__listaNacis[i].getDNIMama() == xdni:
                pos = i
                bandera = False
            else:
                i += 1
        return pos
    
    def buscaMama(self, GM):
        xdni = float(input("Ingrese DNI de la mamá: "))
        i = 0
        posN = self.buscaPosMama(xdni)
        bandera = False
        while i < len(GM._GestorMama__listaMamas) and bandera is False:
            if GM._GestorMama__listaMamas[i].getDNI() == xdni:
                AyN =  GM._GestorMama__listaMamas[i].getApellido() + GM._GestorMama__listaMamas[i].getNombre
                Edad = GM._GestorMama__listaMamas[i].getEdad()
                bandera = True
        print(f'''
                Apellido y Nombre: {AyN} 
                Edad: {Edad}
                Tipo de parto: {self.__listaNacis[posN].getTipoP}
                Bebé/s:
                Peso:                           Altura:''')
        j = 0
        while j < len(self.__listaNacis):
            if xdni == self.__listaNacis[j].getDNIMama():
                print(f'''
                {self.__listaNacis[j].getPeso()}kg  {self.__listaNacis[j].getAlura()}cm''')

    def MasDeUnHijo(self, xdni):
        i = 0
        cant = 0
        while i < len(self.__listaNacis):
            if self.__listaNacis[i] and xdni == self.__listaNacis[i].getDNIMama():
                cant += 1
        if cant < 1:
            bandera = True
        else:
            bandera = False
        return bandera