import numpy as np
import random
from cola_secuencial import Cola
import networkx as nx
import matplotlib.pyplot as plt
from pila_secuencial_default import Pila
class DiGrafo:
    __matriz: np.array
    def __init__(self,elementos):
        self.__elementos = elementos
        self.__matriz_adyacencia = np.zeros((elementos,elementos),dtype=int)
        self.__nodos = [0,1,2,3,4,5]
        
    def añadir_arista(self,u,v):
        try:
            if self.__matriz_adyacencia[u][v] == 1:
                print("Posicion incorrecta\n")
            else:
                self.__matriz_adyacencia[u][v] = 1
        except:
            print("Posicion fuera del rango\n")
    def camino(self,u,v):
        visitados = [False] * self.__elementos
        pila = [(u, [u])]  # Pila que contiene tuplas (nodo_actual, camino_actual)
        # Marcamos el nodo de u como visitado
        visitados[u] = True
        primera_pasada = True
        while pila:
            nodo_actual, camino = pila.pop()
            # Si encontramos el nodo de destino, retornamos el camino
            if not primera_pasada:
                if nodo_actual == v:
                    return camino
            # Expandimos el nodo actual
            for adyacente in self.adyacentes(nodo_actual):
                if not visitados[adyacente]:
                    # Marcamos el adyacente como visitado al agregarlo a la pila
                    visitados[adyacente] = True
                    pila.append((adyacente, camino + [adyacente]))
        # Si no encontramos el camino, devolvemos None
        print("No existe camino")
        return None
    def adyacentes(self,u):
        lista = []
        for i in range(self.__elementos):
            if self.__matriz_adyacencia[u][i] == 1:
                lista.append(i)
        return lista
    def grado_salida(self,u):
        return len(self.adyacentes(u))
    def grado_entrada(self,u):
        cont = 0
        for i in range(self.__elementos):
            if self.__matriz_adyacencia[i][u] == 1:
                cont+=1
        return cont
    def buscar_fuente(self):
        i = 0
        band = False
        while i < self.__elementos and not band: 
            if self.grado_entrada(i) == 0 and self.grado_salida(i) > 0:
                band = True
            else:
                i+=1
        if band:
            return i
        else:
            return None    
    def buscar_pozo(self):   
        band = False
        i = 0
        while i < self.__elementos and not band: 
            if self.grado_entrada(i) > 0 and self.grado_salida(i) == 0:
                band = True
            else:
                i+=1
        if band:
            return i
        else:
            return None                        
    def aciclico(self):
        aciclico = True
        i = 0
        while i < self.__elementos and aciclico:
            if self.camino(i,i):
                aciclico = False
                print(i)
            else:
                i+=1
        return aciclico
    def orden_topologico(self): #iterativo
        if  self.aciclico():
            orden_topo = []
            sin_precedecesores = []
            for i in self.__nodos:
                    if self.grado_entrada(i) == 0:
                        sin_precedecesores.append(i)
            while sin_precedecesores:
                nodo_actual = sin_precedecesores.pop(0)
                orden_topo.append(nodo_actual)
                for i in range(self.__elementos):
                    if self.__matriz_adyacencia[nodo_actual][i] == 1:
                        self.__matriz_adyacencia[nodo_actual][i] = 0
                        if self.grado_entrada(i) == 0:
                            sin_precedecesores.append(i)
            return orden_topo   
        else:
            print("El orden topologico solo se obtiene de grafos aciclicos\n")
    
    def mostrar(self):
        print("[")
        for i in range(self.__elementos):
            for j in range(self.__elementos):
                print(self.__matriz_adyacencia[i][j],end=" ")
            print()
        print("]")

    
if __name__ == '__main__':
    digrafo = DiGrafo(6)
    lista = [
    (0, 1),  # Conexión de 0 a 1
    (1, 2),  # Conexión de 1 a 2
    (3, 1),  # Conexión de 3 a 1
    (3, 4),  # Conexión de 3 a 4
    (4, 5),  # Conexión de 4 a 0 para cerrar el ciclo
    (5, 2),  # Conexión extra de 0 a 2
]

    for u, v in lista:
        digrafo.añadir_arista(u, v)    
    print("Intento de agregar una posicion no existente\n")
    digrafo.añadir_arista(5,6)
    print("Muestra de la matriz\n")
    digrafo.mostrar()
    print(digrafo.orden_topologico())
   