import numpy as np
from cola_secuencial import Cola
from pila_secuencial_default import Pila
import heapq
class Vertice:
    def __init__(self):
        self.distancia = float('inf')  # Inicialmente, la distancia es infinita
        self.camino = None
        self.conocido = False
class DiGrafo_pesos:
    __matriz: np.array
    def __init__(self,elementos):
        self.__elementos = elementos
        self.__matriz_adyacencia = np.zeros((elementos,elementos),dtype=int)
        self.__nodos = ["A","B","C","D","E","F"]
        #self.__nodos.index("(valor a buscar)")
        
    def añadir_arista(self,lista):
        try:
            if self.__matriz_adyacencia[lista[0]][lista[1]] != 0:
                print("Posicion incorrecta\n")
            else:
                self.__matriz_adyacencia[lista[0]][lista[1]] = lista[2]
        except:
            print("Posicion fuera del rango\n")
            
    def adyacentes(self,u):
        lista = []
        for i in range(self.__elementos):
            if self.__matriz_adyacencia[u][i] !=0:
                lista.append(i)
        return lista
    def camino(self,u,v):
        #en 5 caminos obtengo peor valor que el dijkstra
        """ cola = Cola(self.__elementos)
        u = self.__nodos.index(str(u))
        v = self.__nodos.index(str(v))
        visitados = [False] * self.__elementos
        cola.insertar((u, [self.__nodos[u]],0)) # Pila que contiene tuplas (nodo_actual, camino_actual,peso total)
        # Marcamos el nodo de u como visitado
        visitados[u] = True
        if u == v:
            return None
        while cola:
            nodo_actual, camino,peso_total = cola.suprimir()
            # Si encontramos el nodo de destino, retornamos el camino
            if nodo_actual == v:
                return [camino,peso_total]
            # Expandimos el nodo actual
            for adyacente in self.adyacentes(nodo_actual):
                if not visitados[adyacente]:
                    # Marcamos el adyacente como visitado al agregarlo a la cola
                    visitados[adyacente] = True
                    cola.insertar((adyacente, camino + [self.__nodos[adyacente]],peso_total + self.__matriz_adyacencia[nodo_actual][adyacente]))
        # Si no encontramos el camino, devolvemos None
        print("No existe camino")
        return None"""
        u = self.__nodos.index(str(u))
        v = self.__nodos.index(str(v))
        # Inicializamos distancias con infinito y el array de caminos
        distancias = [float('inf')] * self.__elementos
        distancias[u] = 0
        mejores_caminos = [None] * self.__elementos
        mejores_caminos[u] = [self.__nodos[u]]
        # Cola de prioridad para expandir siempre el nodo con menor costo acumulado
        cola = []
        heapq.heappush(cola, (0, u, [self.__nodos[u]]))  # (peso_total, nodo_actual, camino_actual)
        while cola:
            peso_total, nodo_actual, camino = heapq.heappop(cola)
            # Si encontramos el nodo de destino, retornamos el camino y el peso total
            if nodo_actual == v:
                return [camino, peso_total]
            # Expandimos el nodo actual
            for adyacente in self.adyacentes(nodo_actual):
                nuevo_peso = peso_total + self.__matriz_adyacencia[nodo_actual][adyacente]
                
                # Solo expandimos el nodo si encontramos un camino más corto
                if nuevo_peso < distancias[adyacente]:
                    distancias[adyacente] = nuevo_peso
                    mejores_caminos[adyacente] = camino + [self.__nodos[adyacente]]
                    heapq.heappush(cola, (nuevo_peso, adyacente, camino + [self.__nodos[adyacente]]))
        
        # Si no encontramos el camino, devolvemos None
        print("No existe camino")
        return None
    def dijkstra(self, inicio):
        inicio = self.__nodos.index(inicio)
        # Inicializamos la tabla de vértices
        tabla = {v: Vertice() for v in range(self.__elementos)}
        tabla[inicio].distancia = 0  # La distancia al nodo inicial es 0
        # Usamos una cola de prioridad para encontrar el vértice con la distancia más corta
        cola_prioridad = [(0, inicio)]  # (distancia, vértice)
        while cola_prioridad:
            # Obtenemos el vértice con la distancia más corta
            distancia_actual, v = heapq.heappop(cola_prioridad)
            if tabla[v].conocido:
                continue  # Si ya lo conocemos, saltamos
            tabla[v].conocido = True  # Marcamos el vértice como conocido
            # Recorremos los vértices adyacentes
            for w in self.adyacentes(v):
                peso = self.__matriz_adyacencia[v][w]
                nueva_distancia = tabla[v].distancia + peso

                if nueva_distancia < tabla[w].distancia:  # Si encontramos una distancia más corta
                    tabla[w].distancia = nueva_distancia
                    tabla[w].camino = v
                    heapq.heappush(cola_prioridad, (nueva_distancia, w))

        return tabla

    def mostrar(self):
        print("[")
        for i in range(self.__elementos):
            for j in range(self.__elementos):
                print(self.__matriz_adyacencia[i][j],end=" ")
            print()
        print("]")
if __name__ == '__main__':
    digrafo = DiGrafo_pesos(6)
    valores =  ["A","B","C","D","E","F"]

    listas = [
    [0,1,3],  # Conexión de A a B con peso de 3
    [0,3,6],  # Conexión de A a D con peso de 6
    [1,2,1],  # Conexión de B a C con peso de 1
    [1,4,2],  # Conexión de B a E con peso de 2
    [1,5,1],  # Conexión de B a F con peso de 1
    [2,3,2],  # Conexión de C a D con peso de 2
    [3,1,3],  # Conexión de D a B con peso de 3
    [4,3,3],  # Conexión de E a D con peso de 3
    [4,5,2],  # Conexión de E a F con peso de 2
    [5,0,5],  # Conexión de F a A con peso de 5
    [5,3,1],  # Conexión de F a D con peso de 1
]

    for lista in listas:
        digrafo.añadir_arista(lista)
    print(digrafo.BFS("A"))
    """print("Muestra de la matriz\n")
    digrafo.mostrar()
    for valor1 in valores:
        for valor2 in valores:
            datos = digrafo.camino(valor1,valor2)
            if not datos:
                print("No existe camino\n")
            else:
                print(f"Camino desde {valor1} a {valor2}= {datos[0]} Costo total:{datos[1]} centavos\n")
    print("Con el otro alg\n")
    for valor in valores:
        tabla_resultado = digrafo.dijkstra(valor)
        # Imprimir los resultados
        for vertice, datos in tabla_resultado.items():
            nombre_vertice = valores[vertice]  # Obtener el nombre del vértice
            camino_previo = valores[datos.camino] if datos.camino is not None else 'None'  # Camino anterior, si existe
            print(f"Distancia desde {valor} a {nombre_vertice}: {datos.distancia}, Camino: {camino_previo}")

"""
    