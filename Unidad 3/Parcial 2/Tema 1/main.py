from gestorProd import GestorProducto

def menu():
    opcion = None
    try:
        opcion = int(input("""
                                                                     MENÚ DE OPCIONES
                    1) Agregar productos al gestor
                    2) Ingresar posición de la lista a la que se desea acceder para mostrar qué tipo de producto se encuentra almacenado
                    3) Mostrar cantidad de productos de cada tipo
                    4) Mostrar nombre, país de origen, temperatura de mantenimiento recomendada e importe de venta de todos los productos
                    0) SALIR
                    Su opción --> """))
    except ValueError:
        print("\nSe esperaba un número.")
    return opcion

if __name__=='__main__':
    opcion = menu()
    GP = GestorProducto()
    GP.leeDatos()
    try:
        while opcion != 0:
            if opcion == 1:
                GP.leeDatosManu()
            elif opcion == 2:
                GP.muestraType()
            elif opcion == 3:
                GP.determinarClaseDeObjetos()
            elif opcion == 4:
                GP.muestraDatas()
            opcion = menu() 
    except:
        print("Ocurrió un error.")
    finally:
        print("¡Gracias por elegirnos!")