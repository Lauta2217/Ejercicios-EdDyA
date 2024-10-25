class Nodo:
    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None

    # obtenerters y Setters para los atributos privados
    def obtener_dato(self):
        return self.__dato

    def set_dato(self, dato):
        self.__dato = dato

    def obtener_siguiente(self):
        return self.__siguiente

    def set_siguiente(self, siguiente):
        self.__siguiente = siguiente

class ListaOrdenadaEncadenada:
    def __init__(self):
        self.__cabeza = None
        self.__cantidad = 0

    # obtenerters para acceder a atributos privados
    def obtener_cabeza(self):
        return self.__cabeza

    def obtener_cantidad(self):
        return self.__cantidad

    def vacia(self):
        return self.__cantidad == 0

    def insertar(self, x):
        nuevo = Nodo(x)
        # Si la lista está vacía o el nuevo elemento debe ir al principio
        if self.__cabeza is None or self.__cabeza.obtener_dato() >= x:
            nuevo.set_siguiente(self.__cabeza)
            self.__cabeza = nuevo
        else:
            # Encuentra la posición correcta para insertar el nuevo elemento
            actual = self.__cabeza
            while actual.obtener_siguiente() is not None and actual.obtener_siguiente().obtener_dato() < x:
                actual = actual.obtener_siguiente()
            # Inserta el nuevo elemento
            nuevo.set_siguiente(actual.obtener_siguiente())
            actual.set_siguiente(nuevo)
        self.__cantidad += 1

    def suprimir(self, pos):
        if 1 > pos > self.__cantidad:
            print("Error: Posición no válida.")
            return

        # Caso especial: eliminar el primer nodo
        if pos == 1:
            self.__cabeza = self.__cabeza.obtener_siguiente()
        else:
            actual = self.__cabeza
            # Navegar hasta el nodo anterior al que se quiere eliminar
            for i in range(1, pos - 1):
                if actual is None:
                    print("Error: Posición no válida.")
                    return
                actual = actual.obtener_siguiente()

            # Verificar si se encontró el nodo en la posición deseada
            siguiente = actual.obtener_siguiente()
            if siguiente is not None:
                # Eliminar el nodo en la posición dada
                actual.set_siguiente(siguiente.obtener_siguiente())
            else:
                print("Error: Posición no válida.")
                return

        self.__cantidad -= 1

    def buscar(self, x):
        actual = self.__cabeza
        pos = 1
        band = False
        while actual is not None and not band:
            if actual.obtener_dato() == x:
                band = True
            else:
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
# Crear la lista
lista = ListaOrdenadaEncadenada()

# Insertar elementos en la lista
print("** Insertar elementos **")
lista.insertar(10)
lista.insertar(5)
lista.insertar(20)
lista.insertar(7)
lista.recorrer()  # Esperado: 5 7 10 20

# Buscar un elemento existente
print("** Buscar un elemento existente (7) **")
pos = lista.buscar(7)
print(f"Elemento 7 encontrado en la posición: {pos}")  # Esperado: 2

# Buscar un elemento inexistente
print("** Buscar un elemento inexistente (100) **")
pos = lista.buscar(100)
print(f"Elemento 100 encontrado en la posición: {pos}")  # Esperado: None (Error: Elemento no encontrado)

# Obtener el primer y último elemento
print("** Primer y último elemento **")
primer = lista.primer_elemento()
ultimo = lista.ultimo_elemento()
print(f"Primer elemento: {primer}")  # Esperado: 5
print(f"Último elemento: {ultimo}")  # Esperado: 20

# Insertar un nuevo elemento en el medio
print("** Insertar un nuevo elemento (15) **")
lista.insertar(15)
lista.recorrer()  # Esperado: 5 7 10 15 20

# Suprimir un elemento en la posición 3 (eliminar el 10)
print("** Suprimir un elemento en la posición 3 **")
lista.suprimir(3)
lista.recorrer()  # Esperado: 5 7 15 20

# Intentar suprimir un elemento en una posición inválida
print("** Suprimir en una posición inválida (6) **")
lista.suprimir(6)  # Esperado: Error: Posición no válida.

# Obtener la posición siguiente y anterior
print("** Posiciones siguiente y anterior **")
siguiente = lista.siguiente_posicion(2)
anterior = lista.anterior_posicion(3)
print(f"Siguiente posición de 2: {siguiente}")  # Esperado: 3
print(f"Anterior posición de 3: {anterior}")    # Esperado: 2

# Recorrer la lista final
print("** Recorrido final de la lista **")
lista.recorrer()  # Esperado: 5 7 15 20
