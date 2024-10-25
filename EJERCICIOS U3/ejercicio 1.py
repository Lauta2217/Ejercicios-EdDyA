import numpy as np
"""representacion secuencial"""
class Pila:
    def __init__(self,cant):
        self.cant = cant
        self.tope = -1
        self.items = np.zeros(cant, dtype=int) 
    def vacia(self):
        return self.tope == -1

    def insertar(self,x):
        if self.tope < self.cant-1:
            self.tope += 1
            self.items[self.tope] = x
        else:
            return 0
    def suprimir(self):
        if(self.vacia()):
            print("Lista vacia\n")
        else:
            self.tope -= 1
            x = self.items[self.tope]
            return x
    def mostrar(self):
        if not self.vacia():  
            for i in range(self.tope, -1, -1):  
                print(self.items[i]) 
        else:
            print("Pila vacíaaa") 
if __name__ == '__main__':

    pila = Pila(cant = 3)

    pila.insertar(10)  
    pila.insertar(20)
    pila.insertar(30)   
    pila.insertar(60)  # Debería retornar 0, porque la pila está llena
    print("ss")
    pila.mostrar()

    
    pila.suprimir()  
    print("Despues de borrar el ultimo en entrar\n")
    pila.mostrar() #para ver que cumppla con la politica de ultimo en entrar primero en salir
    pila.suprimir()

    if pila.vacia():
        print("La pila está vacia\n")
    else:
        print("No está vacia\n")
        
    pila.suprimir()  
    
    if pila.vacia():
        print("La pila está vacia\n")
    else:
        print("No está vacia\n")
    pila.suprimir()
    pila.mostrar()

"""class Celda:
    def __init__(self,item = None, sig=None):
        self.item = item
        self.sig = sig
    def obtener_item(self):
        return self.item
    def cargar_item(self,itemm):
        self.item = itemm
    def cargar_sig(self,tope):
        self.sig = tope
    def obtener_sig(self):
        return self.sig
class Pila:
    def __init__(self,tope=None,cant=0):
        self.cant = cant
        self.tope = tope
    def vacia(self):
        return self.cant == 0
    def insertar(self,x):
        nueva_celda = Celda(x,self.tope)
        self.tope = nueva_celda
        self.cant+=1
        nueva_celda.obtener_item()
    def suprimir(self):
        if self.vacia():
            return None
        else:
            x = self.tope.obtener_item()
            self.tope = self.tope.obtener_sig()
            self.cant-=1
            return x
    def muestra_tope(self):
        return self.tope.obtener_item()
    def recupera_tope(self):
        return self.tope
    def mostrar(self,aux):
        if aux is not None:
            print(aux.obtener_item())
            self.mostrar(aux.obtener_sig())
        else:
            return

if __name__ == '__main__':
    pila = Pila()
    
    # Insertar elementos
    pila.insertar(10)
    pila.insertar(20)
    pila.insertar(30)
    
    # Recorrer la pila
    print("Recorrer la pila:")
    pila.mostrar(pila.recupera_tope())
    
    # mostrar el tope de la pila
    print("El tope de la pila es:", pila.muestra_tope())
    
    # Suprimir elementos
    print("Elemento suprimido:", pila.suprimir())
    print("El tope de la pila después de suprimir es:", pila.muestra_tope())
    
    # mostrar la pila nuevamente
    print("mostrar la pila nuevamente:")
    pila.mostrar(pila.recupera_tope())
"""
        