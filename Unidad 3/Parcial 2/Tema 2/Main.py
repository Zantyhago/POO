from ManejadorServicioTransporte import ManejadorServicioTransporte
from Menu import MenuDeOpciones

def test():
    m = ManejadorServicioTransporte()
    m.CargaServicioTransporte()
    p = MenuDeOpciones()
    p.Menu(m)

    
if __name__ == "__main__":
    test()