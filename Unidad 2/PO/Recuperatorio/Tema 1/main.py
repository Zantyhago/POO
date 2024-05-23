from gestorMama import GestorMama
from gestorNac import GestorNacimiento

def menu():
    op = int(input('''      Menú de Opciones
                1): Mostrar información de la Mamá.
                2): Mostrar mamá con múltiples nacimientos.
                3): Salir.
                Su opción -> '''))
    return op
    
if __name__ == '__main__':
    GM = GestorMama
    GN = GestorNacimiento
    GM.leerdatos
    GN.leerdatos
    opcion = menu()
    while opcion != 3:
        if opcion == 1:
            GN.buscaMama(GM)
        elif opcion == 2:
            GM.buscaMultiplesNacs(GN)
        else:
            print("¡Opcion invalida!")
            opcion = menu()
