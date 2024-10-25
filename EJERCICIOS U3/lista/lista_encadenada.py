class Nodo:
    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None

    def obtener_dato(self):
        return self.__dato

    def set_dato(self, dato):
        self.__dato = dato

    def obtener_siguiente(self):
        return self.__siguiente

    def set_siguiente(self, siguiente):
        self.__siguiente = siguiente

class ListaEncadenada:
    def __init__(self):
        self.__cabeza = None
        self.__cantidad = 0

    def vacia(self):
        return self.__cantidad == 0

    def obtener_cantidad(self):
        return self.__cantidad
    def insertar(self, x, p):
        if 1>p> self.__cantidad + 1:
            print("Error: Posición inválida.")
            return
        
        nuevo = Nodo(x)
        if p == 1 and self.vacia():
            nuevo.set_siguiente(self.__cabeza)
            self.__cabeza = nuevo
        else:
            actual = self.__cabeza
            for _ in range(1, p - 1):
                if actual is not None:
                    actual = actual.obtener_siguiente()
                else:
                    print("Error: Posición inválida.")
                    return
            
            if actual is not None:
                nuevo.set_siguiente(actual.obtener_siguiente())
                actual.set_siguiente(nuevo)
            else:
                print("Error: Posición inválida.")
                return
        
        self.__cantidad += 1

    def suprimir(self, p):
        if 1>p > self.__cantidad:
            print("Error: Posición inválida.")
            return
        
        if p == 1:
            # Eliminar el primer nodo
            self.__cabeza = self.__cabeza.obtener_siguiente()
        else:
            # Navegar hasta el nodo anterior al que se quiere eliminar
            actual = self.__cabeza
            for _ in range(1, p - 1):
                if actual is not None:
                    actual = actual.obtener_siguiente()
                else:
                    print("Error: Posición inválida.")
                    return
            
            if actual is not None and actual.obtener_siguiente() is not None:
                actual.set_siguiente(actual.obtener_siguiente().obtener_siguiente())
            else:
                print("Error: Posición inválida.")
                return
        
        self.__cantidad -= 1


    def recuperar(self, p):
        if 1>p > self.__cantidad:
            print("Error: Posición inválida.")
            return None
        
        actual = self.__cabeza
        for _ in range(1, p):
            if actual is not None:
                actual = actual.obtener_siguiente()
            else:
                print("Error: Posición inválida.")
                return None

        if actual is not None:
            return actual.obtener_dato()
        print("Error: Posición inválida.")
        return None


    def buscar(self, x):
        actual = self.__cabeza
        pos = 0
        band = False
        while actual is not None and not band:
            if actual.obtener_dato() == x:
                band = True
            actual = actual.obtener_siguiente()
            pos += 1
        if band:
            return pos
        else:
            print("Error: Elemento no encontrado.")
            return None

    def primer_elemento(self):
        if not self.vacia():
            return self.__cabeza.obtener_dato()
        else:
            print("Error: La lista está vacía.")
            return None

    def ultimo_elemento(self):
        actual = self.__cabeza
        if not self.vacia():
            while actual.obtener_siguiente() is not None:
                actual = actual.obtener_siguiente()
            return actual.obtener_dato()
        else:
            print("Error: La lista está vacía.")
            return None

    def siguiente_posicion(self, p):
        if 1 <= p < self.__cantidad:
            return p + 1
        print("Error: No hay posición siguiente.")
        return None


    def anterior_posicion(self, p):
        if 1 < p <= self.__cantidad:
            return p - 1
        print("Error: No hay posición anterior.")
        return None


    def recorrer(self):
        actual = self.__cabeza
        while actual is not None:
            print(actual.obtener_dato(), end=" ")
            actual = actual.obtener_siguiente()
        print()
def prueba_lista_encadenada():
    lista = ListaEncadenada()
    
    # Insertar elementos en la lista
    print("** Insertar elementos **")
    lista.insertar(10, 1)
    lista.insertar(20, 2)
    lista.insertar(15, 2)
    lista.insertar(5, 1)  # Insertar al principio
    lista.recorrer()  # Esperado: 5 10 15 20

    # Recuperar elementos en posiciones válidas
    print("** Recuperar elementos **")
    print("Elemento en la posición 1:", lista.recuperar(1))  # Esperado: 5
    print("Elemento en la posición 2:", lista.recuperar(2))  # Esperado: 10
    print("Elemento en la posición 3:", lista.recuperar(3))  # Esperado: 15
    print("Elemento en la posición 4:", lista.recuperar(4))  # Esperado: 20

    # Recuperar en una posición inválida
    print("** Recuperar en una posición inválida **")
    print("Elemento en la posición 5:", lista.recuperar(5))  # Esperado: Error: Posición inválida.

    # Buscar elementos
    print("** Buscar elementos **")
    print("Buscar elemento 10:", lista.buscar(10))  # Esperado: 1
    print("Buscar elemento 15:", lista.buscar(15))  # Esperado: 3
    print("Buscar elemento 100:", lista.buscar(100))  # Esperado: Error: Elemento no encontrado.

    # Suprimir elementos en posiciones válidas
    print("** Suprimir elementos **")
    lista.suprimir(2)  # Eliminar elemento en posición 2 (10)
    lista.recorrer()  # Esperado: 5 15 20
    lista.suprimir(1)  # Eliminar elemento en posición 1 (5)
    lista.recorrer()  # Esperado: 15 20

    # Suprimir en una posición inválida
    print("** Suprimir en una posición inválida **")
    lista.suprimir(5)  # Esperado: Error: Posición inválida.
    lista.recorrer()  # Esperado: 15 20

    # Primer y último elemento
    print("** Primer y último elemento **")
    print("Primer elemento:", lista.primer_elemento())  # Esperado: 15
    print("Último elemento:", lista.ultimo_elemento())  # Esperado: 20

    # Posiciones siguiente y anterior
    print("** Posiciones siguiente y anterior **")
    print("Siguiente posición de 1:", lista.siguiente_posicion(1))  # Esperado: 2
    print("Anterior posición de 2:", lista.anterior_posicion(2))  # Esperado: 1

    # Insertar en posición inválida
    print("** Insertar en posición inválida **")
    lista.insertar(25, 5)  # Esperado: No debería cambiar la lista porque la posición es inválida
    lista.recorrer()  # Esperado: 15 20

# Ejecutar las pruebas
prueba_lista_encadenada()
