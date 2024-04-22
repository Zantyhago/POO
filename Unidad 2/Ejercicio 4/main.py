from 
from motos import Moto
from pedidos import Pedido

if __name__ == '__main__':
    gestorPedido = []
    gestorMoto = []
    CargarMoto(GestorMotos)
    CargarPedidos(GestorPedidos)
    pat = input("Ingrese patente: ")
    i = 0
    while i < len(gestorMoto) and pat != gestorMoto[i].getPatente():
        i+=1
    if pat gestorMoto[i].getPatente():
        