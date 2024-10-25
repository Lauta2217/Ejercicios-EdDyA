import numpy as np
import random
from cola_secuencial import Cola
import networkx as nx
import matplotlib.pyplot as plt
class Grafo:
    __matriz: np.array
    def __init__(self,elementos):
        self.__elementos = elementos
        self.__matriz_adyacencia = np.zeros((elementos,elementos),dtype=int)
        
    def añadir_arista(self,u,v):
        try:
            if self.__matriz_adyacencia[u][v] == 1:
                print("Posicion incorrecta\n")
            else:
                self.__matriz_adyacencia[u][v] = 1
                self.__matriz_adyacencia[v][u] = 1
        except:
            print("Posicion fuera del rango\n")
            
    def eliminar_arista(self,u,v):
        if self.__matriz_adyacencia[u][v] == 0:
            print("No hay camino para eliminar\n")
        else:
            self.__matriz_adyacencia[u][v] = 0
            #self.__matriz_adyacencia[v][u] = 0
        
    def adyacentes(self,u):
        lista = []
        for i in range(self.__elementos):
            if self.__matriz_adyacencia[u][i] == 1:
                lista.append(i)
        return lista
    def camino(self,u,v):
        visitados = []
        camino = []
        if self.busqueda_amplitud_caminos(u,v,camino,visitados):
            print("encontrado en el camino")
            camino.append(v)
            for i in camino:
                print(i,end=" ")
            print()
            return True
        else:
            print("No existe camino\n")
            return False
    def busqueda_profundidad_caminos(self,u,v,visitados,camino): #Este es la busqueda en profundidad de un camino desde u a v si lo encuentra
        visitados.append(u)
        camino.append(u)
        if u == v:
            return True
        else:
            adyacentes_u = self.adyacentes(u)
            for adyacente in adyacentes_u:
                    if adyacente not in visitados:
                        if self.busqueda_profundidad_caminos(adyacente, v, visitados, camino):
                            return True
        camino.pop()
        return False
    def busqueda_amplitud_caminos(self,u,v,visitados,camino):
        # Inicializamos la cola con el nodo origen
        cola = Cola(self.__elementos)
        cola.insertar(u)
        # Mientras la cola no esté vacía
        while not cola.vacia():
            # Sacamos el primer nodo de la cola
            u = cola.suprimir()
            camino.append(u)
            visitados.append(u)
            # Para cada nodo adyacente a u
            adyacentes_u = self.adyacentes(u)
            for adyacente in adyacentes_u:
                    if adyacente == v:
                        return True
                    elif adyacente not in visitados:        
                        # Insertamos el nodo u en la cola
                        cola.insertar(adyacente)
        return False
    def REP(self): #Este es la busqueda en profundidad de la teoria
        # Inicializamos tiempos de descubrimiento y finalización en 0
        d = [0] * self.__elementos
        f = [0] * self.__elementos
        tiempo = [0]  # Tiempo lo guardamos en una lista para que sea mutable en la recursión
        # Para cada vértice en el grafo
        for s in range(self.__elementos):
            # Si el vértice no ha sido descubierto aún
            if d[s] == 0:
                # Llamamos a REP-Visita para explorar el vértice y sus adyacentes
                self.REP_Visita( s, d, f, tiempo)
        print(f"Tiempos de descubrimiento:{d}")
        print(f"Tiempos de finalización:{f}")

    # Función recursiva para visitar los nodos en profundidad
    def REP_Visita(self, s, d, f, tiempo):
        tiempo[0] += 1
        d[s] = tiempo[0]  # Asignamos el tiempo de descubrimiento
        # Para cada vértice adyacente a s
        adyacentes_s = self.adyacentes(s)
        for u in adyacentes_s:
            if d[u] == 0:  # Si u no ha sido visitado aún
                self.REP_Visita(u, d, f, tiempo)
        tiempo[0] += 1
        f[s] = tiempo[0]  # Asignamos el tiempo de finalización
        
    def BFS(self): #Este es la busqueda de cantidad de caminos desde u a todos sus adyacentes en amplitud
        # Inicializamos las distancias como "infinito" (representado por un número grande)
        d = [float('inf')] * self.__elementos
        # La distancia al nodo origen es 0
        d[0] = 0
        # Inicializamos la cola con el nodo origen
        cola = Cola(self.__elementos)
        cola.insertar(0)
        # Mientras la cola no esté vacía
        while not cola.vacia():
            # Sacamos el primer nodo de la cola
            u = cola.suprimir()
            # Para cada nodo adyacente a u
            adyacentes_u = self.adyacentes(u)
            for adyacente in adyacentes_u:
                    if d[adyacente] == float('inf'):
                        d[adyacente] = d[u] + 1
                        # Insertamos el nodo u en la cola
                        cola.insertar(adyacente)
        # Retornamos la lista de distanciasx
        return d
    def conexo(self):
        band = True
        i = 0
        j = 1
        for i in range(self.__elementos-1):
            if self.camino(i,i+1) or self.camino(i+1,i):
                i+=1
            else:
                print(f"problema en {i,j}")
                band = False
        return band   
    def aciclico(self):
        aciclico = True
        i = 0
        while i < self.__elementos and aciclico:
            if self.camino(i,i):
                aciclico = False
            else:
                i+=1
        return aciclico
    def mostrar(self):
        print("[")
        for i in range(self.__elementos):
            for j in range(self.__elementos):
                print(self.__matriz_adyacencia[i][j],end=" ")
            print()
        print("]")

if __name__ == '__main__':
    grafo = Grafo(5)
    lista = [(4, 2), (0, 0), (1, 2), (3, 3), (1, 3), (0, 4), (1, 4), (2, 3),(2, 4), (2, 1), (3, 1), (4, 0), (4, 1), (3, 2)]
    for u,v in lista:
        grafo.añadir_arista(u,v)
    print("Intento de agregar una posicion no existente\n")
    grafo.añadir_arista(5,6)
    print("Muestra de la matriz\n")
    grafo.mostrar()
    valor =int(input("Ingrese un numero de 0 a 4 para ver sus adyacentes\n"))
    lista_ad = grafo.adyacentes(valor)
    print(f"Adyacentes a {valor}")
    for adyacente in lista_ad:
        print(adyacente,end=" ")
    print()
    u = int(input("Ingrese un valor de inicio entre 0 y 4\n"))
    v = int(input("Ingrese un valor de final entre 0 y 4\n"))
    print(f"Buscando camino entre {u} y {v}\n")
    grafo.camino(u,v)
    print("Usando BFS (busqueda en profundidad)\n")
    d = grafo.BFS()
    print(f"Caminos mas cortos desde 0")
    print(d)
    print("Usando REP (busqueda en amplitud)\n")
    grafo.REP()
    if grafo.conexo():
        print("Grafo conexo\n")
    else:
        print("No es conexo")
    if grafo.aciclico():
        print("El grafo es aciclico\n")
    else:
        print("El grafo no es aciclico\n")
    # Crear un grafo dirigido
    G = nx.DiGraph()
    # Añadir las conexiones
    G.add_edges_from(lista)
    # Dibujar el grafo
    nx.draw(G, with_labels=True, node_color='lightgreen', font_weight='bold', node_size=700)
    # Mostrar el grafo
    plt.show()
        