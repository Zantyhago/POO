from classPlanes import Plan

class Nodo:
    __plan: Plan
    __siguiente: object

    def __init__(self, xplan):
        self.__plan = xplan
        self.__siguiente = None
    
    def setSiguiente(self, xsiguiente):
        self.__siguiente = xsiguiente

    def getSiguiente(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__plan