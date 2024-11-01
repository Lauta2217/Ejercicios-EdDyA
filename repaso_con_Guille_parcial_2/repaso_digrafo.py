import numpy as np
class Digrafo_sec:
    __cant_nodos:int
    __matriz_adyacencia:np.array
    def __init__(self,cant_nodos):
        self.__cant_nodos = cant_nodos
        self.__matriz_adyacencia = np.zeros((self.__cant_nodos,self.__cant_nodos),dtype=int)
    
    def añadir_arista(self,u,v):
        if u < self.__cant_nodos and v < self.__cant_nodos:
            self.__matriz_adyacencia[u][v] = 1
    
    def adyacentes(self,u):
        adyacentes = []
        for i in range(self.__cant_nodos):
            if self.__matriz_adyacencia[u][i] == 1:
                adyacentes.append(i)
        return adyacentes
    def camino(self,u,v):
        visitados = [False] * self.__cant_nodos
        pila = [(u,[u])]
        while pila:
            actual , camino = pila.pop()
            if actual == v:
                return camino
            if not visitados[actual]:
                visitados[actual] = True
            for adyacente in self.adyacentes(actual):
                if not visitados[adyacente]:
                    pila.append((adyacente,camino+[adyacente]))
    
    def conexo(self):
        visitados = [False] * self.__cant_nodos
        pila = [0]
        while pila:
            vertice = pila.pop()
            if not visitados[vertice]:
                visitados[vertice] = True
            for adyacente in self.adyacentes(vertice):
                if not visitados[adyacente]:
                    pila.append(adyacente)
        return all(visitados)

    def grau_ent(self,u):
        cont = 0
        for i in range(self.__cant_nodos):
            if self.__matriz_adyacencia[i][u] == 1:
                cont+=1
        return cont
    
    def grau_sal(self,u):
        return len(self.adyacentes(u))
    
    def fonte(self,u):
        if self.grau_ent(u) == 0 and self.grau_sal(u) > 0:
            print(F"El nodo {u} es fuente")
        else:
            print(f"El nodo {u} no es fuente")
    
    def poço(self,u):
        if self.grau_ent(u) > 0 and self.grau_sal(u) == 0:
            print(f"El nodo {u} es pozo")
        else:
            print(f"El nodo {u} no es pozo")

if __name__ == '__main__':
    digrafo = Digrafo_sec(3)
    conexo = [(0,1),(0,2),(1,2)]
    for u, v in conexo:
        digrafo.añadir_arista(u, v)
    print("Intento de agregar una posicion no existente\n")
    digrafo.añadir_arista(5,6)
    lista_ad = digrafo.adyacentes(0)
    print(f"Adyacentes a {0}")
    for adyacente in lista_ad:
        print(adyacente,end=" ")
    print()
    camino = digrafo.camino(0,2)
    print("Camino de 0 a 2")
    if camino:
        for i in camino:
            print(i,end=" ")
        print()
    if digrafo.conexo():
        print("conexo")
    else:
        print("disconexo")
    print(digrafo.grau_ent(0),digrafo.grau_sal(0))
    digrafo.fonte(0)
    digrafo.poço(2)
    a = input("presiona una tecla para cerrar todo")