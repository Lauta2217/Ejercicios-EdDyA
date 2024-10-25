class Nodo:
    def __init__(self, key):
        self.__key = key
        self.__con = 1
        self.__bal = 0
        self.__izq = None
        self.__der = None

    # Getters y setters para encapsulamiento
    def get_key(self):
        return self.__key

    def set_key(self, key):
        self.__key = key

    def get_bal(self):
        return self.__bal

    def set_bal(self, bal):
        self.__bal = bal

    def get_izq(self):
        return self.__izq

    def set_izq(self, izq):
        self.__izq = izq

    def get_der(self):
        return self.__der

    def set_der(self, der):
        self.__der = der


class ArbolAVL:
    def __init__(self):
        self.__raiz = None

    def insertar(self, x):
        h = False
        self.__raiz = self.insertar2(self.__raiz, x, h)
        
    def insertar2(self, nodo, x, h):
        if nodo is None:
            nodo = Nodo(x)
            h = True
        elif x < nodo.get_key():
            nodo.set_izq(self.insertar2(nodo.get_izq(), x, h))
            if h:
                nodo = self.rebalancear_izquierda(nodo, h)
        elif x > nodo.get_key():
            nodo.set_der(self.insertar2(nodo.get_der(), x, h))
            if h:
                nodo = self.rebalancear_derecha(nodo, h)
        else:
            nodo.__con += 1
        return nodo
    def eliminar2(self, nodo, x, h):
        if nodo is None:
            return None, h

        if x < nodo.get_key():
            nodo.set_izq(self.eliminar2(nodo.get_izq(), x, h)[0])
            if h:
                nodo = self.rebalancear_derecha(nodo, h)
        elif x > nodo.get_key():
            nodo.set_der(self.eliminar2(nodo.get_der(), x, h)[0])
            if h:
                nodo = self.rebalancear_izquierda(nodo, h)
        else:
            # Caso 1: Nodo sin hijos
            if nodo.get_izq() is None and nodo.get_der() is None:
                nodo = None
                h = True
            # Caso 2: Nodo con un solo hijo
            elif nodo.get_izq() is None:
                nodo = nodo.get_der()
                h = True
            elif nodo.get_der() is None:
                nodo = nodo.get_izq()
                h = True
            # Caso 3: Nodo con dos hijos
            else:
                sucesor = self.encontrar_min(nodo.get_der())
                nodo.set_key(sucesor.get_key())
                nodo.set_der(self.eliminar2(nodo.get_der(), sucesor.get_key(), h)[0])
                if h:
                    nodo = self.__rebalancear_izquierda(nodo, h)
        return nodo, h

    def eliminar(self, x):
        h = False
        self.__raiz, h = self.eliminar2(self.__raiz, x, h)

    def encontrar_min(self, nodo):
        actual = nodo
        while actual.get_izq() is not None:
            actual = actual.get_izq()
        return actual

    def rebalancear_izquierda(self, p, h):
        if p.get_bal() == -1:
            p.set_bal(0)
            h = False
        elif p.get_bal() == 0:
            p.set_bal(-1)
        else:
            p1 = p.get_izq()
            if p1.get_bal() == -1:
                p = self.rotacion_simple_izquierda(p, p1)
            else:
                p = self.rotacion_doble_derecha(p, p1)
            h = False
        return p

    def rebalancear_derecha(self, p, h):
        if p.get_bal() == 1:
            p.set_bal(0)
            h = False
        elif p.get_bal() == 0:
            p.set_bal(1)
        else:
            p1 = p.get_der()
            if p1.get_bal() == 1:
                p = self.rotacion_simple_derecha(p, p1)
            else:
                p = self.rotacion_doble_izquierda(p, p1)
            h = False
        return p

    def rotacion_simple_izquierda(self, p, p1):
        p.set_izq(p1.get_der())
        p1.set_der(p)
        p.set_bal(0)
        return p1

    def rotacion_doble_derecha(self, p, p1):
        p2 = p1.get_der()
        p1.set_der(p2.get_izq())
        p2.set_izq(p1)
        p.set_izq(p2.get_der())
        p2.set_der(p)
        if p2.get_bal() == -1:
            p.set_bal(1)
        else:
            p.set_bal(0)
        if p2.get_bal() == 1:
            p1.set_bal(-1)
        else:
            p1.set_bal(0)
        return p2

    def rotacion_simple_derecha(self, p, p1):
        p.set_der(p1.get_izq())
        p1.set_izq(p)
        p.set_bal(0)
        return p1

    def rotacion_doble_izquierda(self, p, p1):
        p2 = p1.get_izq()
        p1.set_izq(p2.get_der())
        p2.set_der(p1)
        p.set_der(p2.get_izq())
        p2.set_izq(p)
        if p2.get_bal() == 1:
            p.set_bal(-1)
        else:
            p.set_bal(0)
        if p2.get_bal() == -1:
            p1.set_bal(1)
        else:
            p1.set_bal(0)
        return p2

    def mostrar2(self, nodo):
        if nodo is not None:
            print(f"{nodo.get_key()}\n")
            print(f"Izquierda:")
            self.mostrar2(nodo.get_izq())
            print(f"Derecha:")
            self.mostrar2(nodo.get_der())

    def mostrar(self):
        self.mostrar2(self.__raiz)

# Ejemplo de uso:
arbol = ArbolAVL()

# Prueba de inserción
print("Insertando elementos en el Árbol AVL...")
elementos = [7,5,2,4,3,8,1,6,11,10,9]
for elem in elementos:
    arbol.insertar(elem)
print(f"Insertado: {elem}")
arbol.mostrar()
print("-----------------------------")

# Prueba de eliminación
print("\nEliminando elementos del Árbol AVL...")
elementos_eliminar = [ 4,8,6,5,2,1,7 ]
for elem in elementos_eliminar:
    arbol.eliminar(elem)
print(f"Eliminado: {elem}")
arbol.mostrar()
print("-----------------------------")

# Probar la visualización final
print("\nVisualización final del Árbol AVL:")
arbol.mostrar()

