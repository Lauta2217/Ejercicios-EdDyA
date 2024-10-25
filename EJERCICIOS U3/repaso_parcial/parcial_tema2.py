import numpy as np
"""parcial tema 2"""

"""punto 1"""
class Pila_sec:
    def __init__(self,xmax):
        self.__elementos = np.zeros(xmax,dtype=int)
        self.__tope = 0
        self.__max_elementos = xmax
    def Pila_llena(self):
        return self.__tope == self.__max_elementos
    def insertar_elem(self,dato):
        if self.Pila_llena():
            print("Pila llena\n")
        else:
            self.obtener_elementos()[self.obtener_tope()] = dato
            self.aumentar_tope()
"""punto 2"""
"""a) Uso el TAD cola ya que utiliza la politica fifo (primero en entrar primero en salir)
y su representacion va a ser la encadenada ya que no sabemos la cantidad de inscripciones"""
"""b) y c)"""
class Cola_enc:
    def __init__(self):
        self.__pr = None
        self.__ul = None
        self.__cant_elementos = 0
    def suprimir_elem(self):
        if self.obtener_cant_elementos() > 0:
            self.set_pr(self.obtener_pr().obtener_sig())
            self.disminuir_cant_elementos()
"""d?"""

"""punto 3"""
class Lista_enc_ord:
    def __init__(self):
        self.__cabeza = None
        self.__cantidad_elementos = 0

    def buscar(self,dato):
        aux = self.obtener_cabeza() 
        pos = 0 
        band = False 
        while aux is not None and not band: 
            if aux.obtener_dato() == dato: 
                band = True 
            else:
                aux = aux.obtener_sig() 
                pos+=1 
        if band:
            print(f"Elemento: {dato} en la posicion: {pos+1}")
        else:
                print("No se encuentra el dato\n")
        