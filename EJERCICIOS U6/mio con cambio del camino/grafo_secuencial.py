import numpy as np
from cola_secuencial import Cola
import networkx as nx #1
import matplotlib.pyplot as plt #2  1 y 2 son para hacer un grafico del grafo
class Grafo:
    __matriz: np.array
    __cant_nodos: int
    def __init__(self,cant_nodos):
        self.__cant_nodos = cant_nodos
        self.__matriz_adyacencia = np.zeros((cant_nodos,cant_nodos),dtype=int)
        
    def añadir_arista(self,u,v):
        try:
            if self.__matriz_adyacencia[u][v] == 1: #si ya hay una arista entre los nodos ingresados entonces sale un print
                print("Posicion incorrecta\n")
            else:
                self.__matriz_adyacencia[u][v] = 1 #1
                self.__matriz_adyacencia[v][u] = 1 #2  1 y 2 ya que al ser grafo no dirigido existe ida y vuelta 
        except:
            print("Posicion fuera del rango\n")
            
    def eliminar_arista(self,u,v):
        try:
            if self.__matriz_adyacencia[u][v] == 0: #si no hay una arista para eliminar entre los nodos ingresados entonces sale un print
                print("No hay camino para eliminar\n")
            else:
                self.__matriz_adyacencia[u][v] = 0 #1
                self.__matriz_adyacencia[v][u] = 0 #2  1 y 2 ya que al ser grafo no dirigido existe ida y vuelta 
        except:
            print("Posicion fuera de rango\n")
        
    def adyacentes(self,u):
        lista = [] #lista que almacena los adyacentes al nodo ingresado
        for i in range(self.__cant_nodos):
            if self.__matriz_adyacencia[u][i] == 1: # si existe una arista entre el nodo ingresado y los que el grafo tiene lo agrego a la lista
                lista.append(i)
        return lista 
    def camino(self,u,v):
        visitados = [False] * self.__cant_nodos # lista que va a servir para saber si el nodo fue visitado
        pila = [(u, [u])]  # Pila que contiene tuplas (nodo_actual, camino_actual)
        visitados[u] = True  # Marcamos el nodo de u como visitado
        while pila: #mientras la pila tenga elementos
            nodo_actual, camino = pila.pop() #desapilamos el primer elemento de la pila
            if nodo_actual == v:# Si encontramos el nodo de destino, retornamos el camino
                return camino
            for adyacente in self.adyacentes(nodo_actual): # Expandimos el nodo actual
                if not visitados[adyacente]: #si el adyacente al nodo ingresado no está en la lista de visitados
                    visitados[adyacente] = True # Marcamos el adyacente como visitado 
                    pila.append((adyacente, camino + [adyacente])) #insertamos el adyacente en la pila y lo agregamos al camino
        print("No existe camino")
        return None # Si no encontramos el camino, devolvemos None
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
        cola = Cola(self.__cant_nodos)
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
        d = [0] * self.__cant_nodos
        f = [0] * self.__cant_nodos
        tiempo = [0]  # Tiempo lo guardamos en una lista para que sea mutable en la recursión
        # Para cada vértice en el grafo
        for s in range(self.__cant_nodos):
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
        d = [float('inf')] * self.__cant_nodos
        # La distancia al nodo origen es 0
        d[0] = 0
        # Inicializamos la cola con el nodo origen
        cola = Cola(self.__cant_nodos)
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
        # Retornamos la lista de distancias
        return d
    def simple_conexo(self):
        band = True
        i = 0
        for i in range(self.__cant_nodos-1):
            if not self.camino(i,i+1) and not self.camino(i+1,i): #si no existe camino de ida ni de vuelta entre 2 nodos entonces ya no es conexo
                band = False
        return band   
    def aciclico(self):
        aciclico = True
        i = 0
        while i < self.__cant_nodos and aciclico: #mientras no hayamos recorrido todos los nodos y la condicion de aciclico sea True
            if self.camino(i,i): #si existe un camino desde un nodo hasta el mismo entonces es un ciclo y cambiamos la condicion
                aciclico = False
            else:
                i+=1 #pasamos al siguiente nodo
        return aciclico   
                        
    def mostrar(self): #tipico mostrar de matriz
        print("[")
        for i in range(self.__cant_nodos):
            for j in range(self.__cant_nodos):
                print(self.__matriz_adyacencia[i][j],end=" ")
            print()
        print("]")
        
plt.ion()
def mostrar_grafo(lista):
    # Crear un grafo dirigido
    G = nx.DiGraph()

    # Añadir las conexiones
    G.add_edges_from(lista)

    # Dibujar el grafo
    pos = nx.spring_layout(G)  # Puedes usar otras disposiciones si prefieres (p.ej., 'circular_layout')
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', font_weight='bold', node_size=700)
    
    # Mostrar el grafo sin bloquear
    plt.draw()
    plt.pause(0.001)  # Pausa corta para asegurar que se muestre el gráfico

    # No usamos plt.show() aquí, para no bloquear la ejecución del código
if __name__ == '__main__':
    grafo = Grafo(7)
# Representación del grafo conexo en forma de lista de aristas
    lista = [
        (0, 1),  # Conexión de 0 a 1
        (0, 2),  # Conexión de 0 a 2
        (1, 3),  # Conexión de 1 a 3
        (1, 4),  # Conexión de 1 a 4
        (2, 5),  # Conexión de 2 a 5
        (3, 6),  # Conexión de 3 a 6
        (4, 6),  # Conexión de 4 a 6
        (5, 6)   # Conexión de 5 a 6
    ]
    for u,v in lista:
        grafo.añadir_arista(u,v)
    print("Intento de agregar una posicion no existente\n")
    grafo.añadir_arista(5,6)
    print("Muestra de la matriz\n")
    grafo.mostrar()
    mostrar_grafo(lista)
    valor =int(input("Ingrese un numero de 0 a 4 para ver sus adyacentes\n"))
    lista_ad = grafo.adyacentes(valor)
    print(f"Adyacentes a {valor}")
    for adyacente in lista_ad:
        print(adyacente,end=" ")
    print()
    u = int(input("Ingrese un valor de inicio entre 0 y 4\n"))
    v = int(input("Ingrese un valor de final entre 0 y 4\n"))
    print(f"Buscando camino entre {u} y {v}\n")
    camino1 = grafo.camino(u,v)
    print("sara modificado")
    for i in camino1:
        print(i,end=" ")
    print()
    print("Usando BFS (busqueda en profundidad)\n")
    d = grafo.BFS()
    print(f"Caminos mas cortos desde 0")
    print(d)
    print("Usando REP (busqueda en amplitud)\n")
    grafo.REP()
    if grafo.simple_conexo():
        print("Grafo simple conexo\n")
    else:
        print("No es conexo")
    if grafo.aciclico():
        print("El grafo es aciclico\n")
    else:
        print("El grafo no es aciclico\n")
    a = input("presiona una tecla para cerrar todo")

        