import numpy as np

class Empleado:
    __nombre: str
    __apellido: str
    __edad: int
    __sueldo: float
    __direccion: str

    def __init__(self, xapell, xnom, xedad, xsueldo, xdir):
        self.__apellido = xapell
        self.__nombre = xnom
        self.__edad = xedad
        self.__sueldo = xsueldo
        self.__direccion = xdir

    def __str__(self):
        return f'Empleado:\nNyA: {self.__nombre} {self.__apellido}.\nSueldo: {self.__sueldo}.\nEdad: {self.__edad}.\nDireccion: {self.__direccion}'
    
    def __eq__(self, otro):
        return self.__sueldo == otro.__sueldo
    
    def __lt__(self, otro):
        return self.__sueldo < otro.__sueldo
    
    def __le__(self, otro):
        return self.__sueldo <= otro.__sueldo

    def __gt__(self, otro):
        return self.__sueldo > otro.__sueldo

    def __ge__(self, otro):
        return self.__sueldo >= otro.__sueldo

def main():
    # crear instancia de empleados
    emp1 = Empleado("Perez","Juan",40,20000,"Juan Jose Paso 350 (o)")
    emp2 = Empleado("Gonzales","Mateo",32,30000,"Sarmiento 547 (s)")
    emp3 = Empleado("Lin","Daniel",23,50000,"General Acha 320 (s)")
    emp4 = Empleado("Benavidez","Geronimo",35,60000,"Av. España 3358 (n)")
    emp5 = Empleado("Disalvio","Martin",30,32000,"Av. Libertador 126 (o)")

    # crear arreglo numpy de empleados
    arreglo_emp = np.array([emp1,emp2,emp3,emp4,emp5])

    # usar max para encontrar el valor maximo
    print(np.max(arreglo_emp))

    # usar min para encontrar el valor minimo
    print(np.min(arreglo_emp))

    # usar argmax para encontrar el indice del valor maximo
    print("El indice del empleado con mayor sueldo es: " + str(np.argmax(arreglo_emp)))

    # usar argmin para encontrar el indice del valor minimo
    print("El indice del empleado con menor sueldo es: " + str(np.argmin(arreglo_emp)))

    # usar sort para ordenar el arreglo numpy de empleados
    print("\nArreglo ordenado de empleados:\n")
    arreglo_ord_emp = np.sort(arreglo_emp)
    i=0
    while i < len(arreglo_ord_emp):
        print(arreglo_ord_emp[i])
        i+=1

if __name__=='__main__':
    main()