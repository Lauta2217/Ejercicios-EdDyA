import numpy as np
class Cola:
    def __init__(self, xmax=0):
        self.__max = xmax
        self.__pr = 0  # Índice del primer elemento
        self.__ul = 0  # Índice del último elemento + 1 (próxima posición de inserción)
        self.__cant = 0  # Cantidad de elementos actuales en la cola
        self.__items = np.zeros(xmax, dtype=int)  # Lista para almacenar los elementos de la cola

    def vacia(self):
        return self.__cant == 0  # Devuelve True si la cola está vacía
    def obtener_cant(self):
        return self.__cant
    def aumentar_cant(self):
        self.__cant+=1
    def disminuir_cant(self):
        self.__cant-=1
    def obtener_max(self):
        return self.__max
    def obtener_pr(self):
        return self.__pr
    def obtener_ul(self):
        return self.__ul
    def obtener_items(self):
        return self.__items
    def cargar_items(self,x):
        self.__items[self.__ul] = x
    def modificar_ul(self):
        self.__ul = (self.__ul + 1) % self.__max # Movimiento circular del índice `ul`
    def modificar_pr(self):
         self.__pr = (self.__pr + 1) % self.__max  # Movimiento circular del índice `pr`
    
    def insertar(self, x):
        if self.obtener_cant() < self.obtener_max():
            self.cargar_items(x)
            self.modificar_ul()
            self.aumentar_cant()
        else:
         print("Cola llena\n")

    def suprimir(self):
        if self.vacia():
            print("Cola vacía")
        else:
            self.modificar_pr()
            self.disminuir_cant()

    def mostrar(self):
        if not self.vacia():
            i = self.obtener_pr()
            j = 0
            while j < self.obtener_cant():
                print(self.obtener_items()[i])
                i = (i + 1) % self.obtener_max()  # Movimiento circular
                j += 1
cola = Cola(3)
cola.insertar(1)
cola.insertar(2)
cola.insertar(3)
cola.suprimir()
cola.mostrar()