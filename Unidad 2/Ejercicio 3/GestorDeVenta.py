class GestorDeVenta:
    __cantDias = 7
    __cantFarmacias: int
    __ventas = list
def __init__(self,xcant):
    self.__cantFarmacias = xcant
    self.__ventas = []
    for i in range (self.__cantFarmacias):
        self.__ventas.append([0]*self.__cantDias)

def Acumular(self, ns, nd, importe):
    self.__ventas[ns][nd] += importe

def Calcula(self, ns):
    total = 0
    for i in range(self.__cantFarmacias):
        total += self.__ventas[ns][i]
    return total

def MayorEmision(self, nd):
    max = 0
    ns: int
    for i in range(self.__cantFarmacias):
        if max < self.__ventas[i][nd]:
            ns = i+1
    return ns

def BuscaMenor(self, ns):
    min = 9999999999
    for i in range(self.__cantFarmacias):
        acum = 0
        for j in range(self.__cantDias):
            acum += self.__ventas[i][j] < min
        if acum < min:
            min = acum
            ns = i+1
    return ns

def AcumaTotal(self):
    acum = 0
    for i in range(self.__canFarmacias):
        for j in range(self.__cantDias):
            acum += self.__ventas[i][j]
    return acum
