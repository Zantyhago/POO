from gestorListaPlanes import GestorPlan

if __name__=='__main__':
    GP = GestorPlan()
    GP.leerDatos()
    GP.BuscaPorPosicion(2)
    GP.contarTiposPlanes()
    GP.cuentaCanalesInters()
    GP.muestraAll()
