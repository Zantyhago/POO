from classPlan import Plan
class Nodo:
    __plan: Plan
    __siguiente: object

    def __init__(self, Plan):
        self.__plan = Plan
        self.__siguiente = None
    
    def set_siguiente(self, siguiente):
        self.__siguiente = siguiente

    def get_siguiente(self):
        return self.__siguiente
    
    def getPlan(self):
        return self.__plan