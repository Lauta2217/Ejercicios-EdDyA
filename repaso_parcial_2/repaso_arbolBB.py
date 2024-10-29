class Nodo:
    __valor:int
    __izquierda:object
    __derecha: object
    def __init__(self,valor,sig = None):
        self.__valor = valor
        self.__izquierda = None
        self.__derecha = None
    def get_value(self):
        return self.__valor
    def get_left(self):
        return self.__izquierda
    def get_right(self):
        return self.__derecha
    def set_left(self,izq):
        self.__izquierda = izq
    def set_right(self,derc):
        self.__derecha = derc
    def set_value(self,value):
        self.__valor = value

class Arbol_binario_busqueda:
    __raiz: object
    def __init__(self):
        self.__raiz = None
    def get_raiz(self):
        return self.__raiz
        
    def insertar(self,valor,actual):
        nodo = Nodo(valor)
        if self.__raiz == None:
            self.__raiz = nodo
            return
        else:
            if actual.get_value() > valor:
                if actual.get_left() is None:
                    actual.set_left(nodo)
                    return
                else:
                    self.insertar(valor,actual.get_left())
            elif actual.get_value() < valor:
                if actual.get_right() is None:
                    actual.set_right(nodo)
                    return
                else:
                    self.insertar(valor,actual.get_right())
    def eliminar(self, valor, actual):
        if actual is None:
            return actual
        # Buscar el nodo a eliminar
        if valor < actual.get_value():
            actual.set_left(self.eliminar(valor, actual.get_left()))
        elif valor > actual.get_value():
            actual.set_right(self.eliminar(valor, actual.get_right()))
        else:
            # Caso 1: Nodo sin hijos
            if actual.get_left() is None and actual.get_right() is None:
                return None
            # Caso 2: Nodo con un solo hijo
            elif actual.get_left() is None:
                return actual.get_right()
            elif actual.get_right() is None:
                return actual.get_left()
            # Caso 3: Nodo con dos hijos
            else:
                # Encontrar el sucesor inorden (mínimo en el subárbol derecho)
                sucesor_inorden = self.min_valor_nodo(actual.get_right())
                # Reemplazar el valor del nodo actual con el valor del sucesor
                actual.set_value(sucesor_inorden.get_left().get_value()) 
                # Eliminar el sucesor inorden en el subárbol derecho
                sucesor_inorden.set_left(sucesor_inorden.get_left().get_right())
        return actual
    def min_valor_nodo(self, nodo):
        # Bajar por la izquierda hasta encontrar el nodo más pequeño
        while nodo.get_left().get_left() is not None:
            nodo = nodo.get_left()
        return nodo
    def buscar(self,valor,actual):
        if actual is None:
            band = False
        elif actual.get_value() == valor:
            band = True
        elif actual.get_value() > valor:
                band = self.buscar(valor,actual.get_left())
        else:
                band = self.buscar(valor,actual.get_right())
        return band  
    def nivel(self,valor,actual,nivel = 0): #nivel del arbol
        if actual is None:
            print("No encontrado\n")
            return
        if actual.get_value() == valor:
            print(f"{valor} tiene nivel: {nivel}\n")
        elif actual.get_value() > valor:
                self.nivel(valor,actual.get_left(),nivel+1)
        else:
                self.nivel(valor,actual.get_right(),nivel+1)
                
    def hoja(self,valor,actual):
        if actual is None:
            print("No encontrado\n")
            band = False
        if actual.get_value() == valor:
            if actual.get_left() is None and actual.get_right() is None:    
                band = True
            else:
                band = False
        elif actual.get_value() > valor:
            band = self.hoja(valor,actual.get_left())
        else:
            band = self.hoja(valor,actual.get_right())
        return band
    
    def hijo(self,hijo,supuesto_padre,actual):
        band = False
        if actual is None:
            band = False
        if supuesto_padre == actual.get_value():
            print("viendo si tiene pendejos")
            if actual.get_left() is not None:
                if actual.get_left().get_value() == hijo:
                    band = True
            elif actual.get_right() is not None:
                if actual.get_right().get_value() == hijo:
                    band = True
        elif actual.get_value() > supuesto_padre:
             self.hijo(hijo,supuesto_padre,actual.get_left())
        else:
             self.hijo(hijo,supuesto_padre,actual.get_right())
        return band
    def camino(self,inicio,fin,actual,band = False,camino = []): #se puede usar la funcion buscar, pero en el parcial hay que definirla tambien
        if actual is None:
            return None
        if actual.get_value() == inicio or band:
            band = True
            camino.append(actual.get_value())     
            if actual.get_value()>=fin:
                self.camino(inicio,fin,actual.get_left(),band,camino)
            else:
                self.camino(inicio,fin,actual.get_right(),band,camino)
        elif actual.get_value()>=inicio:
            self.camino(inicio,fin,actual.get_left())
        else:
            self.camino(inicio,fin,actual.get_right())
        if band:
            return camino
        else:
            return None
        
    def altura(self,actual):
        if actual is None:
            altura = 0
        else:
            altura = 1 + max(self.altura(actual.get_left()),self.altura(actual.get_right()))
        return altura
    
    def padre_y_hermano(self,valor,actual):
        if actual is None:
            return None
        if actual.get_left().get_value() == valor or actual.get_left().get_value() == valor:
            if actual.get_left().get_value() != valor:
                print(f"Padre de {valor}: {actual.get_value()} y su hermano es: {actual.get_left().get_value() }")
            else:
                print(f"Padre de {valor}: {actual.get_value()} y su hermano es: {actual.get_right().get_value() }")
        elif actual.get_value() > valor:
            self.padre_y_hermano(valor,actual.get_left())
        else:
            self.padre_y_hermano(valor,actual.get_right())
            
    def cantidad_nodos(self,actual): #se puede hacer con inorden
        if actual is None:
            cant =  0
        else:
            cant =  1 + self.cantidad_nodos(actual.get_left()) + self.cantidad_nodos(actual.get_right())
        return cant
    
    def sucesores(self,valor,actual):
        if actual is None:
            return None
        if actual.get_value() == valor:
            self.inorden(actual.get_left())
            self.inorden(actual.get_right())
        elif actual.get_value() > valor:
            self.sucesores(valor,actual.get_left())
        else:
            self.sucesores(valor,actual.get_right())
     # Recorrido In-orden
    def inorden(self, nodo_actual): #se ocupa en todo
        if nodo_actual is not None:
            self.inorden(nodo_actual.get_left())
            print(nodo_actual.get_value(),end=" ")
            self.inorden(nodo_actual.get_right())
            
    def preorden(self, nodo_actual):
        if nodo_actual is not None:
            print(nodo_actual.get_value(), end=" ")
            self.preorden(nodo_actual.get_left())
            self.preorden(nodo_actual.get_right())
    # Recorrido Post-orden
    def postorden(self, nodo_actual):
        if nodo_actual is not None:
            self.postorden(nodo_actual.get_left())
            self.postorden(nodo_actual.get_right())
            print(nodo_actual.get_value(), end=" ")
if __name__ == '__main__':
    arbol = Arbol_binario_busqueda()
    valores = [50,30,70,20,40,60,80,10,5]
    for valor in valores:
        arbol.insertar(valor,arbol.get_raiz())
    print(f"""
          buscar:
          80:{arbol.buscar(80,arbol.get_raiz())}
          230:{arbol.buscar(230,arbol.get_raiz())}
          """)
    arbol.nivel(80,arbol.get_raiz())
    arbol.nivel(5,arbol.get_raiz())
    arbol.nivel(50,arbol.get_raiz())
    arbol.nivel(30,arbol.get_raiz())
    arbol.nivel(3120,arbol.get_raiz())
    print(f"""
          hoja:
          50:{arbol.hoja(50,arbol.get_raiz())}
          5:{arbol.hoja(5,arbol.get_raiz())}
          """)
    print(f"""
            hijo:
            5 es hijo de 50?:{arbol.hijo(5,50,arbol.get_raiz())}
            30 es hijo de 50?:{arbol.hijo(30,50,arbol.get_raiz())}
            """)
    print(f"""
            padre ocupando la funcion hijo:
            50 es padre de 5?:{arbol.hijo(50,5,arbol.get_raiz())}
            50 es padre de 30?:{arbol.hijo(30,50,arbol.get_raiz())}
            """)
    camino = arbol.camino(50,5,arbol.get_raiz())
    print(f"camino de {50} a {5}")
    if camino is not None:
        for valor in camino:
            print(valor,end=" ")
        print()
    else:
        print("No existe")
    arbol.padre_y_hermano(30,arbol.get_raiz())
    print(f"Cantidad de nodos: {arbol.cantidad_nodos(arbol.get_raiz())}")
    print(f"Altura del arbol {arbol.altura(arbol.get_raiz())}")
    print("sucesores de 30")
    arbol.sucesores(30,arbol.get_raiz())
    print()
    print("eliminando el nodo 40")
    arbol.eliminar(40,arbol.get_raiz())
    arbol.inorden(arbol.get_raiz())
    