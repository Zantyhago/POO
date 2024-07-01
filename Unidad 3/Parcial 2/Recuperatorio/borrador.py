def eliminarPorDNI(self, dni):
  aux=self.__comienzo
  encontrado = False
  if aux.getDato().getDNI()==dni:
    encontrado=True
    print('Encontrado y eliminado:\n'+str(aux.getDato()))
    self.__comienzo = aux.getSiguiente()
    self.__tope-=1
    del aux
  else:
    ant = aux
    aux = aux.getSiguiente()
    while not encontrado and aux != None:
      if aux.getDato().getDNI()==dni:
        encontrado=True
      else:
        ant = aux
        aux=aux.getSiguiente()
    if encontrado:
      print('Encontrado y eliminado:\n'+str(aux.getDato()))
      ant.setSiguiente(aux.getSiguiente())
      self.__tope-=1
      del aux
    else:
      print('El DNI {}, no está en la lista'.format(dni))
