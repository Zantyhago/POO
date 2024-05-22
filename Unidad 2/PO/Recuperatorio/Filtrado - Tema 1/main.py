from gestorCabañas import GestorCabaña
from gestorReserva import GestorReserva

def menu():
    opcion = int(input('''
                        Menú de Opciones:
            (1): Ingresar cantidad de huéspedes para saber cabañas disponibles.
            (2): Ingresar fecha para emitir listado de reservas.
            (0): Salir
            opcion -> '''))
    return opcion

if __name__ == '__main__':
    GC = GestorCabaña
    GR = GestorReserva
    GC.leedatos()
    GR.leedatos()
    opcion = menu
    while opcion != 0:
        if opcion == 1:
            GC.buscaCabañasDispos(GR)
        elif opcion == 2:
            pass
        else:
            print("Opcion inválida, Dale amigo no cuesta tanto.")
            opcion = menu()