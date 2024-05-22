from classReserva import Reserva
import csv
class GestorReserva:
    __listaReservas: list

    def __init__(self):
        self.__listaReservas = []

    def agregarReserva(self, nuevaReserva):
        self.__listaReservas.append(nuevaReserva)

    def leedatos(self):
        bandera = True
        archivo = open('Reservas.csv')
        reader = csv.reader(archivo, delimiter = ';')
        for fila in reader:
            if bandera:
                bandera = False
            else:
                self.agregarReserva(Reserva(int(fila[0]), fila[1], int(fila[2]), fila[3], int(fila[4]), int(fila[5]), float(fila[6])))
        archivo.close()