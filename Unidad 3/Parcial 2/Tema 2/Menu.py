from ManejadorServicioTransporte import ManejadorServicioTransporte

class MenuDeOpciones:
    __opcion: int
    def __init__(self):
        self.__opcion = None
    def Menu(self,m):
        while self.__opcion != 0:
            print('''
                    -----MENU DE OPCIONES-----
                    1. AGREGAR UN VEHICULO A LA COLECCION
                    2. INGRESAR POSICION DE LA LISTA PARA MOSTRAR EL TIPO DE VEHICULO
                    3. CANTIDAD DE VEHICULOS DE CADA TIPO
                    4. MUESTRA DE TODOS LOS VEHICULOS CON LA TARIFA ACTUALIZADA

                    0. SALIR DEL MENU''')
            self.__opcion = input('>>>> ')
            if self.__opcion == '1':
                m.AgregarVehiculoNuevo()
            elif self.__opcion == '2':
                m.MuestraEnDeterminadaPosicion()
            elif self.__opcion == "3":
                m.CantVehiculosTipo()
            elif self.__opcion == "4":
                m.ListadoDeTodosLosVehiculos()
            elif self.__opcion == '0':
                print("SALIENDO....")
                return
            else:
                print("OPCION INVALIDA")
        self.Menu(m)