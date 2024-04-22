from GestorDeVentas import GestorDeVenta
if __name__=='__main__':
    xcant = int(input("Ingrese cantidad de suscursales: "))
    gestor1 = GestorDeVenta(xcant)
    opcion = str(input("Ingrese opcion:\n1. Ingresar importe.\n2. Ingresar sucursal.\n3. Ingresar dia.\4. Calcular sucur. con menos facturacion.\n5. Calcular el total facturado.\n - 0 para salir -"))
    while opcion != 0:
        if opcion == 1:
            ns = input("Ingrese numero del de dia la semana: ")
            nd = input("Ingrese numero de dia: ")
            importe = input("Ingrese importe: ")
            gestor1 = GestorDeVenta.Acumular(ns,nd,importe)
        elif opcion == 2:
            nd = int(input("Ingrese una sucursal (1-{}):".format(xcant)))
            print("El total facturado es: {}".format(GestorDeVenta.Calcular(nd-1)))
        elif opcion == 3:
            nd = int(input("Ingrese un dia de la semana: "))
            print("Sucursal que mas facturó fue: {}".format(GestorDeVenta.MayorEmision(nd-1)))
        elif opcion == 4:
            print("La sucursal que menos facturo fue: {}".format(GestorDeVenta.BuscaMenor()))
        elif opcion == 5:
            print("El total facturado por todas las sucursales es: {}".format(GestorDeVenta.AcumaTotal()))
