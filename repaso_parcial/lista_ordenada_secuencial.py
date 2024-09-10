class ListaOrdenadaSecuencial:
    def __init__(self, max_size=100):
        self.__elementos = [None] * max_size
        self.__Ult = 0  # Inicialmente no hay elementos, pero se espera que el índice 0 sea la posición inicial disponible
    
    # Obtener elementos
    def obtener_elementos(self):
        return self.__elementos

    def obtener_Ult(self):
        return self.__Ult

    # Verificar si está vacía
    def vacia(self):
        return self.__Ult == 0

    # Verificar si está llena
    def llena(self):
        return self.__Ult >= len(self.__elementos)

    # Insertar un elemento manteniendo el orden
    def insertar(self, x):
        if self.llena():
            print("Error: La lista está llena.")
            return

        # Encuentra la posición correcta para insertar el nuevo elemento
        pos = 0
        while pos < self.__Ult and self.__elementos[pos] <= x:
            pos += 1

        # Mueve los elementos para hacer espacio para el nuevo
        for i in range(self.__Ult, pos, -1):
            self.__elementos[i] = self.__elementos[i - 1]

        # Inserta el nuevo elemento
        self.__elementos[pos] = x
        self.__Ult += 1

    # Suprimir un elemento en una posición específica
    def suprimir(self, pos):
        pos -= 1
        if pos < 0 or pos >= self.__Ult:
            print("Error: Posición no válida.")
            return
        
        # Mueve los elementos para suprimir el elemento en la posición dada
        for i in range(pos, self.__Ult - 1):
            self.__elementos[i] = self.__elementos[i + 1]
        
        # Marca la última posición como vacía
        self.__elementos[self.__Ult - 1] = None
        self.__Ult -= 1

    # Buscar un elemento con búsqueda binaria
    def buscar(self, x):
        inicio = 0
        fin = self.__Ult - 1  # __Ult representa el número de elementos, por eso restamos 1 para obtener el último índice
        while inicio <= fin:
            medio = (inicio + fin) // 2
            if self.__elementos[medio] == x:
                return medio + 1  # Retorna la posición (índice + 1)
            elif self.__elementos[medio] < x:
                inicio = medio + 1
            else:
                fin = medio - 1
        return None  # Si no lo encuentra, devuelve None

    # Obtener el primer elemento
    def primer_elemento(self):
        if self.__Ult >= 0:
            return self.__elementos[0]
        print("Error: La lista está vacía.")
        return None

    # Obtener el último elemento
    def ultimo_elemento(self):
        if self.__Ult >= 0:
            return self.__elementos[self.__Ult - 1]
        print("Error: La lista está vacía.")
        return None

    # Obtener la posición siguiente
    def siguiente_posicion(self, p):
        if 1 <= p < self.__Ult:
            return p + 1
        print("Error: No hay posición siguiente.")
        return None

    # Obtener la posición anterior
    def anterior_posicion(self, p):
        if 1 < p <= self.__Ult:
            return p - 1
        print("Error: No hay posición anterior.")
        return None

    # Recorrer la lista y mostrar los elementos
    def recorrer(self):
        if not self.vacia():
            for i in range(self.__Ult):
                print(self.__elementos[i], end=" ")
            print()
        else:
            print("Lista vacía\n")
# Crear una instancia de la lista ordenada secuencial
lista = ListaOrdenadaSecuencial(max_size=10)

# Imprimir la lista vacía
print("** Lista vacía **")
lista.recorrer()

# Insertar elementos en la lista
print("\n** Insertar elementos **")
lista.insertar(10)
lista.insertar(5)
lista.insertar(15)
lista.recorrer()  # Esperado: 5 10 15

# Insertar un elemento en el medio
print("\n** Insertar en el medio (elemento 7) **")
lista.insertar(7)
lista.recorrer()  # Esperado: 5 7 10 15

# Insertar un elemento en la posición correcta al principio
print("\n** Insertar al principio (elemento 2) **")
lista.insertar(2)
lista.recorrer()  # Esperado: 2 5 7 10 15

# Insertar al final
print("\n** Insertar al final (elemento 20) **")
lista.insertar(20)
lista.recorrer()  # Esperado: 2 5 7 10 15 20

# Intentar insertar en una lista llena
print("\n** Llenar la lista **")
lista.insertar(12)
lista.insertar(17)
lista.insertar(3)
lista.insertar(8)
lista.insertar(6)  # Último elemento que cabe
lista.recorrer()  # Esperado: 2 3 5 6 7 8 10 12 15 20

# Lista llena, intentar agregar otro elemento
print("\n** Insertar en lista llena (elemento 25) **")
lista.insertar(25)  # Esperado: Error: La lista está llena
lista.recorrer()  # No debería cambiar, esperado: 2 3 5 6 7 8 10 12 15 20

# Buscar un elemento existente
print("\n** Buscar elemento existente (15) **")
pos = lista.buscar(15)
print(f"Elemento 15 encontrado en la posición: {pos}")  # Esperado: Posición 9

# Buscar un elemento inexistente
print("\n** Buscar elemento inexistente (100) **")
pos = lista.buscar(100)
print(f"Elemento 100 encontrado en la posición: {pos}")  # Esperado: None

# Recuperar el primer y último elemento
print("\n** Primer y último elemento **")
print(f"Primer elemento: {lista.primer_elemento()}")  # Esperado: 2
print(f"Último elemento: {lista.ultimo_elemento()}")  # Esperado: 20

# Obtener posiciones siguiente y anterior
print("\n** Posiciones siguiente y anterior **")
print(f"Siguiente posición de 4: {lista.siguiente_posicion(4)}")  # Esperado: 5
print(f"Anterior posición de 5: {lista.anterior_posicion(5)}")  # Esperado: 4

# Suprimir un elemento del medio
print("\n** Suprimir elemento en la posición 5 **")
lista.suprimir(5)
lista.recorrer()  # Esperado: 2 3 5 6 8 10 12 15 20

# Suprimir el primer elemento
print("\n** Suprimir el primer elemento **")
lista.suprimir(1)
lista.recorrer()  # Esperado: 3 5 6 8 10 12 15 20

# Suprimir el último elemento
print("\n** Suprimir el último elemento **")
lista.suprimir(lista.obtener_Ult())
lista.recorrer()  # Esperado: 3 5 6 8 10 12 15
