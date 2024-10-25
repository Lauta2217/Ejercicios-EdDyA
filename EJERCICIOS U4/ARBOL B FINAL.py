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
    def vacia(self):
        return self.__raiz == None
    def set_raiz(self,raiz):
        self.__raiz = raiz
    # Insertar un valor en el árbol

    def insertar(self, valor, nodo_actual):
        if self.vacia():
            self.__raiz = Nodo(valor)
        else:  
            if valor < nodo_actual.obtener_valor():
                if nodo_actual.obtener_izquierda() is None:
                    nodo_actual.asignar_izquierda(Nodo(valor))
                else:
                    self.insertar(valor, nodo_actual.obtener_izquierda())
            elif valor > nodo_actual.obtener_valor():
                if nodo_actual.obtener_derecha() is None:
                    nodo_actual.asignar_derecha(Nodo(valor))
                else:
                    self.insertar(valor, nodo_actual.obtener_derecha())
                
    # Eliminar un valor del árbol

    def eliminar(self, valor, nodo_actual):
        if nodo_actual is None:
            return nodo_actual
        if valor < nodo_actual.obtener_valor():
            nodo_actual.asignar_izquierda(self.eliminar(valor, nodo_actual.obtener_izquierda()))
        elif valor > nodo_actual.obtener_valor():
            nodo_actual.asignar_derecha(self.eliminar(valor, nodo_actual.obtener_derecha()))
        else:
            # Nodo con solo un hijo o sin hijos
            if nodo_actual.obtener_izquierda() is None:
                return nodo_actual.obtener_derecha()
            elif nodo_actual.obtener_derecha() is None:
                return nodo_actual.obtener_izquierda()
            # Nodo con dos hijos: obtener el sucesor en in-orden (mínimo del subárbol derecho)
            temp_valor = self.encontrar_min2(nodo_actual.obtener_derecha())
            nodo_actual.asignar_valor(temp_valor)
            nodo_actual.asignar_derecha(self.eliminar(temp_valor, nodo_actual.obtener_derecha()))
        self.set_raiz(nodo_actual)
    # Buscar un valor en el árbol

    def buscar(self, valor, nodo_actual):
        if nodo_actual is None:
            return False
        if valor == nodo_actual.obtener_valor():
            return True
        elif valor < nodo_actual.obtener_valor():
            return self.buscar(valor, nodo_actual.obtener_izquierda())
        else:
            return self.buscar(valor, nodo_actual.obtener_derecha())
        
    def nivel(self,actual,valor,nivel = 0):
        if self.vacia():
            print("No hay datos en el arbol")
        elif self.__raiz.obtener_valor() == valor:
            print(f"Nivel de {valor}:{nivel} \n")
        else:
            if actual is None:
                print("Dato ingresado no encontrado")
            else:
                if actual.obtener_valor() == valor:
                    print(f"Nivel de {valor}: {nivel}")
                elif actual.obtener_valor() < valor:
                    nivel+=1
                    self.nivel(actual.obtener_derecha(),valor,nivel)
                else:
                    nivel+=1
                    self.nivel(actual.obtener_izquierda(),valor,nivel)
                

    def hoja(self,valor,actual):
        if self.vacia():
            print("NO tien nada \n")
        else:
            if self.__raiz.obtener_valor() == valor:
                if self.__raiz.obtener_derecha() is None and self.__raiz.obtener_izquierda() is None:
                        print("La raiz tambien es hoja\n")
                else:
                    print(f"El valor {valor} no es hoja\n")
        if actual is None:
            print("Dato ingresado no existe\n")
        else:
            if actual.obtener_valor() == valor:
                if actual.obtener_derecha() is None and actual.obtener_izquierda() is None:
                    print(f"El valor {valor} es hoja\n")
                else:
                    print(f"El valor {valor} no es hoja\n")
            elif actual.obtener_valor() < valor:
                self.hoja(valor,actual.obtener_derecha())
            else:
                self.hoja(valor,actual.obtener_izquierda())
                
   
    def hijo(self,actual,supuesto_hijo,padre):
        if self.vacia():
            print("El arbol no tiene na\n")
        else:
            if actual is None:
                print("No se encontro el padre\n")
            else:
                if actual.obtener_valor() == padre:
                    if actual.obtener_izquierda().obtener_valor() == supuesto_hijo or actual.obtener_derecha().obtener_valor() == supuesto_hijo :
                       print(f"El valor {padre} es padre del valor {supuesto_hijo}\n") 
                    else:
                        print(f"El valor {padre} no es padre del valor {supuesto_hijo}\n")
                elif actual.obtener_valor() > padre:
                    self.hijo(actual.obtener_izquierda(),supuesto_hijo,padre)
                else:
                    self.hijo(actual.obtener_derecha(),supuesto_hijo,padre)
                
    def camino(self,actual,inicio,fin,camino = []):
        if self.__raiz is None:
            print("El arbol no tien na\n")
        else:
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
        return camino   
    
    def altura(self,nodo):
        if nodo is None:
            return 0
        else:
            altura = 1 + max(self.altura(nodo.obtener_izquierda()),self.altura(nodo.obtener_derecha()))
        return altura
    # Encontrar el valor mínimo
    def encontrar_min(self, nodo_actual):
        if self.__raiz is None:
            return None
        else:
            if nodo_actual.obtener_izquierda() is None:
                return nodo_actual.obtener_valor()
            else:
                return self.encontrar_min(nodo_actual.obtener_izquierda())

    # Encontrar el valor máximoz)
    def encontrar_max(self, nodo_actual):
        if self.__raiz is None:
            return None
        else:
            if nodo_actual.obtener_derecha() is None:
                return nodo_actual.obtener_valor()
            else:
                return self.encontrar_max(nodo_actual.obtener_derecha())

    # Recorrido In-orden
    def inorden(self, nodo_actual):
        if nodo_actual is not None:
            self.inorden(nodo_actual.obtener_izquierda())
            print(nodo_actual.obtener_valor(),end=" ")
            self.inorden(nodo_actual.obtener_derecha())
            
    def preorden(self, nodo_actual):
        if nodo_actual is not None:
            print(nodo_actual.obtener_valor(), end=" ")
            self.preorden(nodo_actual.obtener_izquierda())
            self.preorden(nodo_actual.obtener_derecha())
        

    # Recorrido Post-orden
    def postorden(self, nodo_actual):
        if nodo_actual is not None:
            self.postorden(nodo_actual.obtener_izquierda())
            self.postorden(nodo_actual.obtener_derecha())
            print(nodo_actual.obtener_valor(), end=" ")
if __name__ == '__main__':
    arbol = ArbolBinarioBusqueda()
    arbol.insertar(50,arbol.obtener_raiz())
    arbol.insertar(30,arbol.obtener_raiz())
    arbol.insertar(70,arbol.obtener_raiz())
    arbol.insertar(20,arbol.obtener_raiz())
    arbol.insertar(40,arbol.obtener_raiz())
    arbol.insertar(60,arbol.obtener_raiz())
    arbol.insertar(80,arbol.obtener_raiz())
    arbol.insertar(10,arbol.obtener_raiz())
    arbol.insertar(5,arbol.obtener_raiz())
    arbol.hijo(arbol.obtener_raiz(),5,10) #raiz, nodo a saber si es hijo, padre 
    camino = arbol.camino(arbol.obtener_raiz(),50,5)
    if len(camino) != 0:
            print(f"Camino:")
            for valor in camino:
                print(valor, end=" ")
            print()
    else:
        print("No se pudo obtener el camino\n")
    print(f"altura: {arbol.altura(arbol.obtener_raiz())}\n")
    print("Mínimo:", arbol.encontrar_min(arbol.obtener_raiz()))  # Debería imprimir 3
    arbol.nivel(arbol.obtener_raiz(), 50)
    arbol.nivel(arbol.obtener_raiz(),80)
    arbol.nivel(arbol.obtener_raiz(),10)
    arbol.nivel(arbol.obtener_raiz(),5)
    arbol.hoja(50,arbol.obtener_raiz())
    arbol.hoja(80,arbol.obtener_raiz())
    arbol.hoja(10,arbol.obtener_raiz())
    arbol.hoja(5,arbol.obtener_raiz())
    print("In-orden:")
    arbol.inorden(arbol.obtener_raiz())
    print("\n\nPre-orden:")
    arbol.preorden(arbol.obtener_raiz())
    print("\n\nPost-orden:")
    arbol.postorden(arbol.obtener_raiz())
    print("\nBuscar 5:", arbol.buscar(5,arbol.obtener_raiz()))  # Debería imprimir True
    print("Buscar 8:", arbol.buscar(8,arbol.obtener_raiz()))  # Debería imprimir False
    print("Máximo:", arbol.encontrar_max(arbol.obtener_raiz()))  # Debería imprimir 15
    arbol.eliminar(10,arbol.obtener_raiz())
    print("In-orden después de eliminar 10:")
    arbol.inorden(arbol.obtener_raiz())