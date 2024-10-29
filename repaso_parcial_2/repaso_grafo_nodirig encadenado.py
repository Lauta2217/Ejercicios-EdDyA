import numpy as np
from pila_secuencial_default import Pila
from cola_secuencial import Cola
class Nodo:
    __value:int
    __sig: object
    def __init__(self,value,sig=None):
        self.__value = value
        self.__sig = sig
    def get_value(self):
        return self.__value
    def get_sig(self):
        return self.__sig
    def set_sig(self,sig):
        self.__sig = sig
        
class Grafo_enc:
    __matriz: np.array
    __cant_nodos:int
    def __init__(self,cant_nodos):
        self.__cant_nodos = cant_nodos
        self.__matriz = np.ndarray(self.__cant_nodos,dtype=Nodo)
        for i in range(self.__cant_nodos):
            nodo = Nodo(i)
            self.__matriz[i] = nodo
    
    def añadir_arista(self,u,v):
        if u < self.__cant_nodos and v < self.__cant_nodos:
            i = 0
            actual = self.__matriz[u]
            band = False
            while actual.get_sig() is not None:
                if actual.get_sig().get_value() == v:
                    band =True
                actual = actual.get_sig()
            if not band:
                    nodo = Nodo(v)
                    actual.set_sig(nodo)
                    self.añadir_arista(v,u)
        
    def adyacentes(self,u):
        adyacentes = []
        actual = self.__matriz[u].get_sig()
        while actual is not None:
            adyacentes.append(actual.get_value())
            actual = actual.get_sig()
        return adyacentes
    
    def camino(self,u,v):
        visitados = [False] * self.__cant_nodos
        pila = [(u,[u])]
        while pila:
            actual,camino = pila.pop()
            if actual == v:
                return camino
            if not visitados[actual]:
                visitados[actual] = True
            for adyacente in self.adyacentes(actual):
                if not visitados[adyacente]:
                    pila.append((adyacente,camino+[adyacente]))
    
    def conexo(self):
        simple_conexo = True
        i = 0
        j = 0
        while i < self.__cant_nodos and simple_conexo:
            while j < self.__cant_nodos and simple_conexo:
                if self.camino(i,j) is None:
                    simple_conexo = False
                else:
                    j+=1
            j=0
            i+=1
        if not simple_conexo:
            print("El grafo no es simple conexo ni fuertemente conexo\n")
        else:
            print("Como es dirigido entonces existe ida y vuelta por lo tanto este grafo es fuertemente conexo\n")
            
    def aciclico(self):
        """visitados = [False] * self.__cant_nodos
        en_pila = [False] * self.__cant_nodos  # Pila de nodos actualmente en el camino
        for nodo in range(self.__cant_nodos):  # Recorremos todos los nodos
            if not visitados[nodo]:
                stack = [(nodo, False)]  # Utilizamos una pila para la DFS
                while stack:
                    actual, retorno = stack.pop()
                    if not retorno:  # Si no hemos regresado a este nodo
                        visitados[actual] = True
                        en_pila[actual] = True
                        stack.append((actual, True))  # Marcar que estamos regresando
                        for adyacente in self.adyacentes(actual):# Revisar adyacentes
                            if not visitados[adyacente]:
                                stack.append((adyacente, False))
                            elif en_pila[adyacente]:  # Si el adyacente está en la pila, hay un ciclo
                                return False
                    else:  # Estamos regresando a este nodo
                        en_pila[actual] = False  # Retiramos el nodo de la pila
        return True  # No se detectaron ciclos"""
    def REA(self,v = 0): #Este es la busqueda de cantidad de caminos desde u a todos sus adyacentes en amplitud
        # Inicializamos las distancias como "infinito" (representado por un número grande)
        d = [float('inf')] * self.__cant_nodos
        # La distancia al nodo origen es 0
        d[v] = 0
        # Inicializamos la cola con el nodo origen
        cola = Cola(self.__cant_nodos)
        cola.insertar(v)
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

    def REP_iterativo(self,s = 0):  # Búsqueda en profundidad iterativa
        d = [0] * self.__cant_nodos  # Tiempos de descubrimiento
        f = [0] * self.__cant_nodos  # Tiempos de finalización
        tiempo = [0]  # Tiempo como lista mutable
        # Crear una pila para DFS
        pila = Pila(self.__cant_nodos)
        # Para cada vértice en el grafo
        pila.insertar(s)  # Comenzamos con el nodo s
        while not pila.vacia():  # Mientras la pila no esté vacía
            nodo = pila.suprimir()  # Mirar el tope de la pila
            if d[nodo] == 0:  # Si el nodo no ha sido descubierto
                tiempo[0] += 1
                d[nodo] = tiempo[0]  # Asignamos tiempo de descubrimiento

                # Obtener adyacentes y procesarlos
                adyacentes_nodo = self.adyacentes(nodo)
                for u in reversed(adyacentes_nodo):
                    if d[u] == 0:  # Si el adyacente no ha sido descubierto
                        pila.insertar(u)  # Añadir a la pila

            # Verificar si se puede asignar el tiempo de finalización
            if all(d[u] != 0 for u in adyacentes_nodo):
                tiempo[0] += 1
                f[nodo] = tiempo[0]  # Asignamos el tiempo de finalización
            elif d[nodo] != 0:  # Asegurarse de no sobrescribir si ya fue visitado
                tiempo[0] += 1
                f[nodo] = tiempo[0]  # Asignar el tiempo de finalización
        # Imprimir resultados
        print(d)
        print(f)
        
    def mostrar(self):
        print("[")
        for i in range(self.__cant_nodos):
            actual = self.__matriz[i]
            while actual is not None:
                print(actual.get_value(),end=" ")
                actual = actual.get_sig()
            print()
        print("]")
if __name__ == '__main__':
    grafo = Grafo_enc(5) #siempre uno mas que el valor mas grande de las tuplas de los elementos a insertar
    # Lista de conexiones para un grafo acíclico
    aristas_acyclicas = [
        (0, 1),
        (0, 2),
        (1, 3),
        (1, 4),
        (2, 5),
        (3, 6)
    ]
    # Lista de conexiones para un grafo cíclico
    aristas_ciclicas = [
        (0, 1),
        (0, 2),
        (1, 3),
        (1, 4),
        (2, 5),
        (3, 6),
        (4, 6),  # Crea un ciclo entre 1-3-6-4-1
        (5, 6),  # Crea un ciclo entre 2-5-6-2
        (0, 6)   # Crea un ciclo adicional entre 0-2-5-6-0
    ]
    lista_fuertemente_conexo = [
    (0, 1),  # Conexión de 0 a 1
    (1, 2),  # Conexión de 1 a 2
    (2, 0),  # Conexión de 2 a 0 (ciclo entre 0, 1 y 2)
    (1, 3),  # Conexión de 1 a 3
    (3, 4),  # Conexión de 3 a 4
    (4, 1)   # Conexión de 4 a 1 (conexión de vuelta a 1)
]
    lista_disconexo = [
    (0, 1),  # Conexión de 0 a 1
    (1, 2),  # Conexión de 1 a 2
    (3, 4)   # Conexión de 3 a 4 (disconexión con los nodos 0, 1 y 2)
]

    for u,v in aristas_acyclicas :
        grafo.añadir_arista(u,v)
    grafo.mostrar()
    print(grafo.adyacentes(0))
    """print("Intento de agregar una posicion no existente\n")
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
    camino = grafo.camino()
    print("sara modificado")
    for i in camino:
        print(i,end=" ")
    print()"""
    print("Usando BFS (busqueda en profundidad)\n")
    d = grafo.REA()
    print(f"Caminos mas cortos desde 0")
    print(d)
    print("Usando REP (busqueda en amplitud)\n")
    grafo.REP_iterativo()
    grafo.conexo()
    if grafo.aciclico():
        print("El grafo es aciclico\n")
    else:
        print("El grafo no es aciclico\n")  
    a = input("presiona una tecla para cerrar todo")
        