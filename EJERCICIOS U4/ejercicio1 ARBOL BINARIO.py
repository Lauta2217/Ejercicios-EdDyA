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
                
    def insertar_no_recursivo(self,valor):
        band = False
        if self.__raiz is None:
            self.__raiz = Nodo(valor)
        else:
            actual = self.__raiz
            while not band:
                if actual.obtener_valor() > valor:
                    if actual.obtener_izquierda() is None:
                        actual.asignar_izquierda(Nodo(valor))
                        band = True
                    else:
                        actual = actual.obtener_izquierda()
                elif actual.obtener_valor() < valor:
                    if actual.obtener_derecha() is None:
                        actual.asignar_derecha(Nodo(valor))    
                        band = True        
                    else:
                        actual = actual.obtener_derecha()
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
    # Buscar un valor en el árbol
    def buscar(self, valor):
        return self.buscar_2(valor, self.__raiz)

    def buscar_2(self, valor, nodo_actual):
        if nodo_actual is None:
            return False
        if valor == nodo_actual.obtener_valor():
            return True
        elif valor < nodo_actual.obtener_valor():
            return self.buscar_2(valor, nodo_actual.obtener_izquierda())
        else:
            return self.buscar_2(valor, nodo_actual.obtener_derecha())
    def nivel(self,valor):
        if self.__raiz is None:
            print("No hay datos en el arbol\n")
        else:
            if self.__raiz.obtener_valor() == valor:
                print(f"Nivel de {valor}: 0\n")
            else:
                self.nivel2(self.__raiz,valor,0)
    def nivel2(self,actual,valor,nivel):
        if actual is None:
            print("Dato ingresado no encontrado")
        else:
            if actual.obtener_valor() == valor:
                print(f"Nivel de {valor}: {nivel}")
            elif actual.obtener_valor() < valor:
                nivel+=1
                self.nivel2(actual.obtener_derecha(),valor,nivel)
            else:
                nivel+=1
                self.nivel2(actual.obtener_izquierda(),valor,nivel)
    def hoja(self,valor):
        if self.__raiz is None:
            print("El arbol no tiene nada\n")
        else:
            if self.__raiz.obtener_valor() == valor:
                if self.__raiz.obtener_derecha() is None and self.__raiz.obtener_izquierda() is None:
                    print("La raiz tambien es hoja\n")
                else:
                    print(f"El valor {valor} no es hoja\n")
            else:
                self.hoja2(self.__raiz,valor)
    def hoja2(self,actual,valor):
        if actual is None:
            print("Dato ingresado no existe\n")
        else:
            if actual.obtener_valor() == valor:
                if actual.obtener_derecha() is None and actual.obtener_izquierda() is None:
                    print(f"El valor {valor} es hoja\n")
                else:
                    print(f"El valor {valor} no es hoja\n")
            elif actual.obtener_valor() < valor:
                self.hoja2(actual.obtener_derecha(),valor)
            else:
                self.hoja2(actual.obtener_izquierda(),valor)
    def hijo(self,padre,supuesto_hijo):
        if self.__raiz is None:
            print("El arbol no tiene na\n")
        else:
            if self.__raiz.obtener_valor() == padre:
                if self.__raiz.obtener_derecha().obtener_valor() == supuesto_hijo or self.__raiz.obtener_izquierda().obtener_valor() == supuesto_hijo:
                    print(f"El valor {padre} es padre del valor {supuesto_hijo}\n")
                else:
                    print(f"El valor {padre} no es padre del valor {supuesto_hijo}\n")
            else:
                return self.hijo2(self.__raiz,padre,supuesto_hijo)
    def hijo2(self,actual,padre,supuesto_hijo):
        if actual is None:
            print("No se encontro el padre\n")
        else:
            if actual.obtener_valor() == padre:
                if actual.obtener_derecha() is not None:
                    if actual.obtener_derecha().obtener_valor() == supuesto_hijo :
                        print(f"El valor {padre} es padre del valor {supuesto_hijo}\n")
                        return True
                elif actual.obtener_izquierda() is not None:
                    if actual.obtener_derecha().obtener_valor() == supuesto_hijo :
                        print(f"El valor {padre} es padre del valor {supuesto_hijo}\n")
                        return True
                else:
                        print(f"El valor {padre} no es padre del valor {supuesto_hijo}\n")
                        return False
            elif actual.obtener_valor() > padre:
                self.hijo2(actual.obtener_izquierda(),padre,supuesto_hijo)
            else:
                self.hijo2(actual.obtener_derecha(),padre,supuesto_hijo)
    def camino(self,inicio,fin):
        if self.__raiz is None:
            print("El arbol no tien na\n")
        else:
            camino = []
            self.camino2(self.__raiz,inicio,fin,camino)
        if len(camino) != 0:
                print(f"Camino desde {inicio} a {fin} :")
                for valor in camino:
                    print(valor, end=" ")
                print()
        else:
            print("No se pudo obtener el camino\n")
                
    def camino2(self,actual,inicio,fin,camino):
        if actual.obtener_valor() == inicio:
            band = False
            while not band:
                if actual.obtener_valor() == fin:
                    band = True
                    camino.append(fin)
                else:
                    if actual.obtener_valor() > fin:   
                        camino.append(actual.obtener_valor())
                        actual = actual.obtener_izquierda() 
                    else:
                        camino.append(actual.obtener_valor())
                        actual = actual.obtener_derecha()   
    def altura(self):
        return self.altura2(self.__raiz)
    def altura2(self,nodo):
        if nodo is None:
            return 0
        else:
            return 1 + max(self.altura2(nodo.obtener_izquierda()),self.altura2(nodo.obtener_derecha()))
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
        self.inorden2(self.__raiz)
        
        
    def inorden2(self, nodo_actual):
        if nodo_actual is not None:
            self.inorden2(nodo_actual.obtener_izquierda())
            print(nodo_actual.obtener_valor(),end=" ")
            self.inorden2(nodo_actual.obtener_derecha())
        
            
    def preorden(self):
        self.preorden2(self.__raiz)
        

    def preorden2(self, nodo_actual):
        if nodo_actual is not None:
            print(nodo_actual.obtener_valor(), end=" ")
            self.preorden2(nodo_actual.obtener_izquierda())
            self.preorden2(nodo_actual.obtener_derecha())
        

    # Recorrido Post-orden
    def postorden(self):
        self.postorden2(self.__raiz)
        

    def postorden2(self, nodo_actual):
        if nodo_actual is not None:
            self.postorden2(nodo_actual.obtener_izquierda())
            self.postorden2(nodo_actual.obtener_derecha())
            print(nodo_actual.obtener_valor(), end=" ")

    

arbol = ArbolBinarioBusqueda()
arbol.insertar_no_recursivo(50)
arbol.insertar_no_recursivo(30)
arbol.insertar_no_recursivo(70)
arbol.insertar_no_recursivo(20)
arbol.insertar_no_recursivo(40)
arbol.insertar_no_recursivo(60)
arbol.insertar_no_recursivo(80)
arbol.insertar_no_recursivo(10)
arbol.insertar_no_recursivo(5)
arbol.nivel(50)
arbol.nivel(80)
arbol.nivel(10)
arbol.nivel(5)
arbol.hoja(50)
arbol.hoja(80)
arbol.hoja(10)
arbol.hoja(5)
arbol.hijo(50,70)
arbol.hijo(100,50)
arbol.camino(50,5)
print(f"altura: {arbol.altura()}\n")
print("In-orden:")
arbol.inorden()
print("\n\nPre-orden:")
arbol.preorden()
print("\n\nPost-orden:")
arbol.postorden()
print("\nBuscar 5:", arbol.buscar(5))  # Debería imprimir True
print("Buscar 8:", arbol.buscar(8))  # Debería imprimir False
print("Mínimo:", arbol.encontrar_min())  # Debería imprimir 3
print("Máximo:", arbol.encontrar_max())  # Debería imprimir 15

arbol.eliminar(10)
print("In-orden después de eliminar 10:")
arbol.inorden()