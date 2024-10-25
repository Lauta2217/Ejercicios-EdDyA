from cola_encadenada import Cola
from random import randint
class Trabajo:
    def __init__(self,tiempo_impresion):
        self.__tiempo_impresion = tiempo_impresion
        self.__tiempo_espera = 0
    def obtener_tiempo_espera(self):
        return self.__tiempo_espera
    def obtener_tiempo_impresion(self):
        return self.__tiempo_impresion
    def aumentar_tiempo_espera(self):
        self.__tiempo_espera+=1
    def disminuir_tiempo_impresion(self):
        self.__tiempo_impresion-=1
def impresion(t,impresora):
    tiempo_ejecucion = 0
    trabajos_impresos = 0
    tiempo_promedio_espera_impresos = 0
    band = True
    while(tiempo_ejecucion < t):
        if tiempo_ejecucion % 5 == 0:
            tra = Trabajo(randint(1,10))
            impresora.insertar(tra)
        for i in range(5):
            if impresora.vacia():
                band = False
            if band:
                if impresora.obtener_pr().obtener_item().obtener_tiempo_impresion() == 0:
                    tiempo_promedio_espera_impresos+= impresora.obtener_pr().obtener_item().obtener_tiempo_espera()
                    impresora.suprimir()
                    trabajos_impresos+=1
                else:
                    impresora.obtener_pr().obtener_item().disminuir_tiempo_impresion()
                    aux = impresora.obtener_pr().obtener_sig()
                    while aux is not None:
                        aux.obtener_item().aumentar_tiempo_espera()
                        aux = aux.obtener_sig()
        tiempo_ejecucion+=5
        if impresora.obtener_pr().obtener_item().obtener_tiempo_impresion() != 0:
            impresora.insertar(impresora.obtener_pr().obtener_item())
            impresora.suprimir()
    print(f"Trabajos impresos:{trabajos_impresos}\n tiempo promedio de los trabajos impresos: {tiempo_promedio_espera_impresos/trabajos_impresos}\n trabajos que quedaron sin imprimir: {impresora.obtener_cant()} tiempo de ejecucion: {tiempo_ejecucion}\n")
    aux = impresora.obtener_pr()
    while aux is not None:
        print(f"tiempo que le queda para imprimir:{aux.obtener_item().obtener_tiempo_impresion()}")
        aux = aux.obtener_sig()
if __name__== '__main__':
    impresora = Cola()
    t = int(input("Ingrese tiempo de simulación\n"))
    tra1 = Trabajo(5)
    tra2 = Trabajo(8)
    impresora.insertar(tra1)
    impresora.insertar(tra2)
    impresion(t,impresora)