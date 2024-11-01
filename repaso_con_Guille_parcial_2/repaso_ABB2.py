import numpy as np
class Nodo:
    __value:int
    __left: object
    __right: object
    def __init__(self,value):
        self.__value = value
        self.__left = None
        self.__right = None
    def get_value(self):
        return self.__value
    def get_left(self):
        return self.__left
    def get_right(self):
        return self.__right
    def set_left(self,left):
        self.__left = left
    def set_right(self,right):
        self.__right = right
    def grado(self):
        if self.__left is not None and self.__right is not None:
            return 2
        elif self.__left is None and self.__right is None:
            return 0
        else:
            return 1
class Arbol_ABB:
    __raiz: object
    def __init__(self):
        self.__raiz = None
    def get_raiz(self):
        return self.__raiz
    
    def insertar(self,valor,actual):
        nodo = Nodo(valor)
        if self.__raiz == None:
                self.__raiz = nodo
        if actual is not None:
            if actual.get_value() > valor:
                if actual.get_left() is None:
                    actual.set_left(nodo)
                else:
                    self.insertar(valor,actual.get_left())
            else:
                if actual.get_right() is None:
                    actual.set_right(nodo)
                else:
                    self.insertar(valor,actual.get_right())
    def buscar(self,valor,actual):
        band = False
        while actual is not None and not band:
            if actual.get_value() == valor:
                band = True
            elif actual.get_value() > valor:
                actual = actual.get_left()
            else:
                actual = actual.get_right()
        if band:
            print("Encontrado")
            return actual
        else:
            print("No encontrado")
        
    def nivel(self,valor,actual,nivel = 0):
        if actual is not None:
            if actual.get_value() == valor:
                print(f"El valor {valor} tiene nivel {nivel}\n")
            elif actual.get_value() > valor:
                self.nivel(valor,actual.get_left(),nivel+1)
            else:
                self.nivel(valor,actual.get_right(),nivel+1)
    def hoja(self,valor):
        nodo = self.buscar(valor,self.__raiz)
        if nodo is not None and nodo.grado() == 0:
            print(f"El nodo {valor} es hoja\n")
    def hijo(self,hijo,padre):
        nodo_padre = self.buscar(padre,self.__raiz)
        if nodo_padre is not None:
            if nodo_padre.get_left() is not None and nodo_padre.get_left().get_value() == hijo:
                print(f"El nodo {padre} es padre del nodo {hijo}")
            elif nodo_padre.get_right() is not None and nodo_padre.get_right().get_value() == hijo:
                print(f"El nodo {padre} es padre del nodo {hijo}")
        else:
            print(f"El nodo {padre} no es padre del nodo {hijo}")
    def camino(self,inicio,fin):
        nodo_inicio = self.buscar(inicio,self.__raiz)
        camino = []
        while nodo_inicio is not None:
            camino.append(nodo_inicio.get_value())
            if nodo_inicio.get_value() == fin:
                print(f"Camino de {inicio} a {fin}: {camino}")
                nodo_inicio = None
            elif nodo_inicio.get_value() > fin:
                nodo_inicio = nodo_inicio.get_left()
            else:
                nodo_inicio = nodo_inicio.get_right()
    def altura(self,actual):
        if actual is not None:
            altura = 1 + max(self.altura(actual.get_left()),self.altura(actual.get_right()))
        else:
            altura = 0
        return altura        
    def tuda_folha(self,actual):
        if actual is not None:
            self.tuda_folha(actual.get_left())
            if actual.grado() == 0:
                print(f"{actual.get_value()}",end=" ")
            self.tuda_folha(actual.get_right())
            
    def sucesores(self,valor):
        nodo = self.buscar(valor,self.__raiz)
        if nodo is not None:
            self.inorder(nodo.get_left())
            self.inorder(nodo.get_right())
        else:
            print("No hay sucesores porque es none")
            
    def contar_nodos(self,actual):
        if actual is not None:
            return 1 + self.contar_nodos(actual.get_left()) + self.contar_nodos(actual.get_right())
        else:
            return 0
    def contar_sucesores(self,valor):
        nodo = self.buscar(valor,self.__raiz)
        if nodo is not None:
            print(f"Cant sucesores de {valor}:{self.contar_nodos(nodo)-1}")
    def grado(self,valor):
        nodo = self.buscar(valor,self.__raiz)
        if nodo is not None:
            print(f"grado de {valor}:{nodo.grado()}")
    def inorder(self,actual):
        if actual is not None:
            self.inorder(actual.get_left())
            print(actual.get_value(), end=" ")
            self.inorder(actual.get_right())
    def preorden(self,actual):
        print(actual.get_value(),end= "")
        self.preorden(actual.get_left())
        self.preorden(actual.get_right())
    def postorden(self,actual):
        self.postorden(actual.get_left())
        self.postorden(actual.get_right())
        print(actual.get_value,end=" ")
if __name__ == '__main__':
    arbol = Arbol_ABB()
    valores = [50,30,70,20,40,60,80,10,5,4,3]
    for valor in valores:
        arbol.insertar(valor,arbol.get_raiz())
    arbol.inorder(arbol.get_raiz())
    print("Buscando 80")
    arbol.buscar(80,arbol.get_raiz())
    print("Buscando 230")
    arbol.buscar(230,arbol.get_raiz())
    arbol.nivel(80,arbol.get_raiz())
    arbol.nivel(5,arbol.get_raiz())
    arbol.nivel(50,arbol.get_raiz())
    arbol.nivel(30,arbol.get_raiz())
    arbol.nivel(3120,arbol.get_raiz())
    arbol.hijo(30,50)
    arbol.hijo(5,80)
    print("camino de a 10 a 5")
    arbol.camino(10,5)
    print(f"Cantidad de nodos: {arbol.contar_nodos(arbol.get_raiz())}")
    print(f"Altura del arbol {arbol.altura(arbol.get_raiz())}")
    print("sucesores de 10")
    arbol.sucesores(10)
    print()
    arbol.grado(50)
    arbol.grado(5)    
    arbol.contar_sucesores(30)
    print("Todas las hojas del arbol\n")
    arbol.tuda_folha(arbol.get_raiz())
        
                
        
                
        