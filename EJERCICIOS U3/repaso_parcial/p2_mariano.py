import numpy as np

class Cola:
    def __init__(self) -> None:
        self.pr = None
        self.ul = None
        self.cant = 0
        
    def suprimir_elem(self):
        if self.cant > 0:
            aux = self.pr
            self.pr = self.pr.get_siguiente()
            del aux
            self.cant -= 1
            if self.cant == 0:
                self.ul = None

def simular():
    tiempo = 5*60
    t = 0
    cola = Cola()
    cajero = 0  # Cuando es 0 significa que el cajero esta vacio, si es > 0, indica el tiempo que lleva atendiendo
    
    while t < tiempo:
        if t % 10 == 0:
            cola.insertar(0)
        
        if cajero > 0:
            cajero += 1
            if cajero == 15:
                cajero = 0
                
        if cajero == 0 and not cola.vacia():
            cola.suprimir_elem()
            cajero = 1
        
        actual = cola.get_primero()
        while actual:
            actual += 1
            actual = actual.get_siguiente()
        
    aux = cola.get_primero()
    maximo = aux.get_dato()
    while aux:
        maximo = max(aux.get_dato(), maximo)
        aux = aux.get_siguiente()
        
    print(maximo)
        
simular()
#En este caso se necesita el TAD Cola porque se necesita seguir el orden FIFO, el primero en entrar es el primero en salir