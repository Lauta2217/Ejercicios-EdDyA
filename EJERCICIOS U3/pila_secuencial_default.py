import numpy as np
"""Representacion secuencial"""
class Pila:
    def __init__(self,cant):
        self.__cant = cant
        self.__tope = 0
        self.__items = np.zeros(cant, dtype=int) 
    def vacia(self):
        return self.__tope == 0
    def obtener_cant(self):
        return self.__cant
    def obtener_tope(self):
        return self.__tope
    def aumentar_tope(self):
        self.__tope += 1
    def disminuir_tope(self):
        self.__tope -= 1
    def obtener_items(self):
        return self.__items
    
    def insertar(self,x):
        if self.obtener_tope() < self.obtener_cant():
            self.obtener_items()[self.obtener_tope()] = x
            self.aumentar_tope()
    def suprimir(self):
        if(self.vacia()):
            print("Lista vacia\n")
        else:
            self.obtener_items()[self.obtener_tope()-1]=0
            self.disminuir_tope()
            
    def mostrar(self):
        if not self.vacia():  
            for i in range(self.obtener_tope()-1, -1, -1):  #inicio,fin,incremento/decremento
                print(self.obtener_items()[i]) 
        else:
            print("Pila vacíaaa")
    def __str__(self):
        return str(self.items)

pila = Pila(3)
pila.insertar(1)
pila.insertar(2)
pila.insertar(3)
print(f"tope:{pila.obtener_tope()}")
pila.suprimir()
pila.mostrar()