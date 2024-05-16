from ClaseCli import Cliente
import csv

class gestorCli:
    __lista_cli: list

    def __init__ (self):
        self.__lista_cli = []

    def agregarCliente(self, nuevoCliente):
        self.__lista_cli.append (nuevoCliente)

    def leerdatos(self):
        band = True
        archivo = open('ClientesFarmaCiudad.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            if band:
                band = False
            else:
                self.agregarCliente(Cliente(fila[0], fila[1], float(fila[2]), int (fila[3]), float(fila[4])))
        archivo.close()

    #agregado
    def obtenerPosDNI(self, dni):
        i = 0
        band = False
        pos = -1
        while i < len(self.__lista_cli) and band is False:
            if self.__lista_cli[i].getDNI() == dni:
                pos = i
                band = True
            else:
                i += 1
        return pos
    #agregado

    #agregado
    def actualiza_sald (self, gestMov):
        int = 0
        xdni = float(input("Ingresa el DNI del cliente: "))
        pos = self.obtenerPosDNI(xdni)
        if pos != -1:
            num_C = self.__lista_cli[pos].getNro_cta()
            AyN = self.__lista_cli[pos].getAp() + " " + self.__lista_cli[pos].getNom()
            saldAnt = self.__lista_cli[pos].getSaldo_ant()
            print(f"""
                  
                  Cliente: {AyN}        Número de cuenta: {num_C}
                  Saldo Anterior: {saldAnt}
                  Movimientos
                  Fecha         Descripción         Importe         Tipo de Movimiento""")

            for j in range (gestMov._gestorMov__cantidad):
                if gestMov._gestorMov__list_gest[j].getNro_cta() == num_C:
                    fecha = gestMov._gestorMov__list_gest[j].getFecha()
                    desc = gestMov._gestorMov__list_gest[j].getDesc()
                    imp = gestMov._gestorMov__list_gest[j].getImporte()
                    tipo = gestMov._gestorMov__list_gest[j].getTipo()
                    
                    if tipo == "C":
                        saldAnt += imp
                    elif tipo == "P":
                        saldAnt -= imp
                    print(f"""
                    {fecha}         {desc}         {imp}         {tipo}""")
            
            print(f"""
                    Saldo actualizado: {saldAnt}""")
        
        else:
            print("No existe un cliente con el DNI ingresado.")

    def mostrarDatos_siNoHayMov(self, gestMov):
        xdni = int(input("Ingrese el DNI del cliente: "))
        pos = self.obtenerPosDNI(xdni)
        if pos != -1:
            num_C = self.__lista_cli[pos].getNro_cta()
            mov = gestMov.existenMovimientos_porNumCuenta(num_C)
            if mov is False:
                print("No tuvo movimientos, su nombre y apellido es: ", self.__lista_cli[pos].getNom()+ " ", self.__lista_cli[pos].getAp())
            else:
                print("Sí tuvo movimientos")
        else:
            print("No existe una cuenta con ese DNI.")