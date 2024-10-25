import numpy as np
"""Representacion secuencial"""
class Pila:
    def __init__(self,cant):
        self.cant = cant
        self.tope = -1
        self.items = np.zeros(cant, dtype=int) 
    def vacia(self):
        return self.tope == -1

    def insertar(self,x):
        if self.tope < self.cant:
            self.tope += 1
            self.items[self.tope] = x
    def suprimir(self):
        if(self.vacia()):
            return
        else:
            self.items[self.tope] = 0 
            self.tope -= 1
            
    def mostrar(self):
        if not self.vacia():  
            for i in range(self.tope, -1, -1):  
                print(self.items[i]) 
    def obtener_tope(self):
        return int(self.items[self.tope])
    def __str__(self):
        return str(self.items)