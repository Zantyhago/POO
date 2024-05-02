from gestorclientes import GestorCliente
from gestormovimientos import GestorMovimiento

if __name__ == '__main__':
    opcion = input("Seleccione una opcion:\na: Actualizar saldo.\nb: Mostrar movomientos.\nc: Ordenar movimientos.\nd: Salir.")
    while opcion != d:
        if opcion == a:
            xdni = input("Ingrese DNI: ")
            apell, nomb, numacc, saldAnt, fecha, descr, imp, type  = nc.actualiza(xdni)
            print("Cliente: {} {}{10}{}".format(apell, nomb, numacc))
            print("Movimientos:\n")
        elif opcion == b:
            xdni = input("Ingrese dni: ")
            apell, nomb, band = nc.buscamovs(xdni)
            if band:
                print("El cliente {} {} tuvo movimientos en el mes corriente.")
            else:
                print("El cliente {} {} no tuvo movimientos en el mes corriente.")
        elif opcion == c:
            
        
