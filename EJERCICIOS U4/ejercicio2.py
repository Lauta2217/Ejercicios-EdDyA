class Nodo:
    def __init__(self, valor):
        self.__valor = valor
        self.__izquierda = None
        self.__derecha = None

    # Métodos para acceder y modificar los atributos privados
    def obtener_valor(self):
        return self.__valor

    def asignar_valor(self, valor):
        self.__valor = valor

    def obtener_izquierda(self):
        return self.__izquierda

    def asignar_izquierda(self, nodo):
        self.__izquierda = nodo

    def obtener_derecha(self):
        return self.__derecha

    def asignar_derecha(self, nodo):
        self.__derecha = nodo

class ArbolBinarioBusqueda:
    def __init__(self):
        self.__raiz = None
    def obtener_raiz(self):
        return self.__raiz
    # Insertar un valor en el árbol
    def insertar(self, valor):
        if self.__raiz is None:
            self.__raiz = Nodo(valor)
        else:
            self.insertar_2(valor, self.__raiz)

    def insertar_2(self, valor, nodo_actual):
        if valor < nodo_actual.obtener_valor():
            if nodo_actual.obtener_izquierda() is None:
                nodo_actual.asignar_izquierda(Nodo(valor))
            else:
                self.insertar_2(valor, nodo_actual.obtener_izquierda())
        elif valor > nodo_actual.obtener_valor():
            if nodo_actual.obtener_derecha() is None:
                nodo_actual.asignar_derecha(Nodo(valor))
            else:
                self.insertar_2(valor, nodo_actual.obtener_derecha())

    # Buscar un valor en el árbol
    def buscar(self, valor):
        return self.buscar_2(valor, self.__raiz)

    def buscar_2(self, valor, nodo_actual):
        if nodo_actual is None:
            return None
        if valor == nodo_actual.obtener_valor():
            return nodo_actual
        elif valor < nodo_actual.obtener_valor():
            return self.buscar_2(valor, nodo_actual.obtener_izquierda())
        else:
            return self.buscar_2(valor, nodo_actual.obtener_derecha())

    # Encontrar el valor mínimo
    def encontrar_min(self):
        if self.__raiz is None:
            return None
        else:
            return self.encontrar_min2(self.__raiz)

    def encontrar_min2(self, nodo_actual):
        if nodo_actual.obtener_izquierda() is None:
            return nodo_actual.obtener_valor()
        else:
            return self.encontrar_min2(nodo_actual.obtener_izquierda())

    # Encontrar el valor máximo
    def encontrar_max(self):
        if self.__raiz is None:
            return None
        else:
            return self.encontrar_max2(self.__raiz)

    def encontrar_max2(self, nodo_actual):
        if nodo_actual.obtener_derecha() is None:
            return nodo_actual.obtener_valor()
        else:
            return self.encontrar_max2(nodo_actual.obtener_derecha())

    # Recorrido In-orden
    def inorden(self):
        elementos = []
        self.inorden_2(self.__raiz, elementos)
        return elementos

    def inorden_2(self, nodo_actual, elementos):
        if nodo_actual is not None:
            self.inorden_2(nodo_actual.obtener_izquierda(), elementos)
            elementos.append(nodo_actual.obtener_valor())
            self.inorden_2(nodo_actual.obtener_derecha(), elementos)

    # Eliminar un valor del árbol
    def eliminar(self, valor):
        self.__raiz = self.eliminar_2(valor, self.__raiz)

    def eliminar_2(self, valor, nodo_actual):
        if nodo_actual is None:
            return nodo_actual
        if valor < nodo_actual.obtener_valor():
            nodo_actual.asignar_izquierda(self.eliminar_2(valor, nodo_actual.obtener_izquierda()))
        elif valor > nodo_actual.obtener_valor():
            nodo_actual.asignar_derecha(self.eliminar_2(valor, nodo_actual.obtener_derecha()))
        else:
            # Nodo con solo un hijo o sin hijos
            if nodo_actual.obtener_izquierda() is None:
                return nodo_actual.obtener_derecha()
            elif nodo_actual.obtener_derecha() is None:
                return nodo_actual.obtener_izquierda()
            # Nodo con dos hijos: obtener el sucesor en in-orden (mínimo del subárbol derecho)
            temp_valor = self.encontrar_min2(nodo_actual.obtener_derecha())
            nodo_actual.asignar_valor(temp_valor)
            nodo_actual.asignar_derecha(self.eliminar_2(temp_valor, nodo_actual.obtener_derecha()))
        return nodo_actual
    def padre_y_hermano(self,valor):
        if self.__raiz is None:
            print("El arbol no tiene nada")
        else:
            self.band = False
            self.padre_y_hermano2(valor,None,self.__raiz)
            if not self.band:
                print("No existe tal nodo")
    def padre_y_hermano2(self,valor,padre,nodo_actual):
        if nodo_actual is None:
            return 
        elif valor == nodo_actual.obtener_valor():
            self.band = True
            if padre is None:
                print("El valor ingresado no tiene padre ni hermano, pues es la raiz\n")
            else:
                if padre.obtener_izquierda() == nodo_actual:
                    hermano = padre.obtener_derecha()
                else:
                    hermano = padre.obtener_izquierda()
                if hermano is None:
                    print("No tiene hermanos")
                else:
                    print(f"padre: {padre.obtener_valor()} hermano: {hermano.obtener_valor()}")
        elif valor < nodo_actual.obtener_valor():
            self.padre_y_hermano2(valor,nodo_actual,nodo_actual.obtener_izquierda())
        elif valor > nodo_actual.obtener_valor():
            self.padre_y_hermano2(valor,nodo_actual,nodo_actual.obtener_derecha())
    def contar_nodos(self):
        return self.contar_nodos2(self.__raiz)
    def contar_nodos2(self,nodo):
        if nodo is None:
            return 0
        else:
            return 1 + self.contar_nodos2(nodo.obtener_izquierda()) + self.contar_nodos2(nodo.obtener_derecha())
    def altura(self):
        return self.altura2(self.__raiz)
    def altura2(self,nodo):
        if nodo is None:
            return 0
        else:
            return 1 + max(self.altura2(nodo.obtener_izquierda()),self.altura2(nodo.obtener_derecha()))
    def sucesor(self,valor):
        nodo = self.buscar(valor)
        if nodo is None:
            print("El valor ingresado no existe")
        else:
            return self.sucesor2(nodo).obtener_valor()
    def sucesor2(self,actual):
        if actual.obtener_derecha() is not None:
            self.encontrar_min2(actual.obtener_derecha())
        else:
            sucesor = None
            ancestro = self.__raiz
            while ancestro is not None:
                if actual.obtener_valor() < ancestro.obtener_valor():
                    sucesor = ancestro
                    ancestro = ancestro.obtener_izquierda()
                elif actual.obtener_valor() > ancestro.obtener_valor():
                    ancestro = ancestro.obtener_derecha()
                else:
                    break
            return sucesor
# Ejemplo de uso
arbol = ArbolBinarioBusqueda()
arbol.insertar(50)
arbol.insertar(30)
arbol.insertar(70)
arbol.insertar(20)
arbol.insertar(40)
arbol.insertar(60)
arbol.insertar(80)
arbol.padre_y_hermano(40)
arbol.padre_y_hermano(100)
print(f"cantidad de nodos:{arbol.contar_nodos()}")
print(f"altura:{arbol.altura()}")
print(f"sucesor de 40: {arbol.sucesor(40)}")
"""print("In-orden:", arbol.inorden())  # Debería imprimir [3, 5, 10, 15]
print("Buscar 5:", arbol.buscar(5))  # Debería imprimir True
print("Buscar 8:", arbol.buscar(8))  # Debería imprimir False
print("Mínimo:", arbol.encontrar_min())  # Debería imprimir 3
print("Máximo:", arbol.encontrar_max())  # Debería imprimir 15

arbol.eliminar(10)
print("In-orden después de eliminar 10:", arbol.inorden())  # Debería imprimir [3, 5, 15]"""
