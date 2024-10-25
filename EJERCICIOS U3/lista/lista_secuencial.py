import numpy as np
class ListaSecuencial:
    def __init__(self, max_size=100):
        self.__elementos = np.full(max_size, None)  # Inicializa con None usando un arreglo de numpy
        self.__Ult = 0  # Inicialmente no hay elementos
        self.__max = max_size
        
    def obtener_elementos(self):
        return self.__elementos

    def obtener_Ult(self):
        return self.__Ult

    def vacia(self):
        return self.__Ult == 0
    def llena(self):
        return self.__Ult >= len(self.__elementos)

    def insertar(self, x, p):
        if self.llena():
            print("Lista llena\n")
            return
        else:
            if 1 <= p <= self.__Ult + 1:
                # Realizar el shifteo si la posición está ocupada
                for i in range(self.__Ult, p - 1, -1):  # Desplazar los elementos hacia la derecha
                    self.__elementos[i] = self.__elementos[i-1]
                # Insertar el nuevo elemento en la posición
                self.__elementos[p - 1] = x
                self.__Ult += 1
            else:
                print("Error: Posición inválida.")

    def suprimir(self, p):
        if 1 <= p <= self.__Ult:
            # Guardar el elemento a suprimir
            x = self.__elementos[p - 1]
            # Realizar el shifteo hacia la izquierda para cubrir el hueco
            for i in range(p - 1, self.__Ult-1):
                self.__elementos[i] = self.__elementos[i + 1]
            # Marcar el último elemento como None después de shiftear
            self.__elementos[self.__Ult-1] = None
            self.__Ult -= 1
            return x
        else:
            print("Error: Posición inválida.")
            return None

    def recuperar(self, p):
        if 1<= p <= self.__Ult:
            return self.__elementos[p - 1]
        else:
            print("Error: Posición inválida.")
            return None

    def buscar(self, x):
        band = False
        i = 0
        while i <= self.__Ult and not band:
            if self.__elementos[i] == x:
                band = True 
            else:
                i += 1
        if band:
            return i+1
        else:
            return None

    def primer_elemento(self):
        if self.__Ult >= 0:
            return self.__elementos[0]
        else:
            print("Error: La lista está vacía.")
            return None

    def ultimo_elemento(self):
        if self.__Ult >= 0:
            return self.__elementos[self.__Ult-1]
        else:
            print("Error: La lista está vacía.")
            return None

    def siguiente_posicion(self, p):
        if 1 <= p < self.__Ult:
            return p + 1
        else:
            print("Error: No hay posición siguiente.")
            return None

    def anterior_posicion(self, p):
        if 1 < p <= self.__Ult:
            return p - 1
        else:
            print("Error: No hay posición anterior.")
            return None

    def recorrer(self):
        if not self.vacia():
            for i in range(self.__Ult):
                print(self.__elementos[i], end=" ")
            print()
        else:
            print("Lista vacía\n")
lista = ListaSecuencial(max_size=10)  # Crear lista secuencial con capacidad para 10 elementos

print("** Prueba de lista vacía **")
lista.recorrer()  # Esperado: "Lista vacía"

print("\n** Insertar elementos **")
lista.insertar(5, 1)  # Insertar 5 en la posición 1
lista.insertar(10, 2)  # Insertar 10 en la posición 2
lista.insertar(15, 3)  # Insertar 15 en la posición 3
lista.recorrer()  # Esperado: "5 10 15"

print("\n** Insertar en el medio (pos 2) **")
lista.insertar(7, 2)  # Insertar 7 en la posición 2
lista.recorrer()  # Esperado: "5 7 10 15"

print("\n** Insertar en una posición inválida **")
lista.insertar(20, 6)  # Posición 6 es inválida (sólo hay 4 elementos)
lista.recorrer()  # Esperado: "5 7 10 15"

print("\n** Buscar un elemento existente (10) **")
print(f"Elemento 10 encontrado en la posición: {lista.buscar(10)}")  # Esperado: 3

print("\n** Buscar un elemento inexistente (100) **")
print(f"Elemento 100 encontrado en la posición: {lista.buscar(100)}")  # Esperado: None

print("\n** Recuperar elemento en la posición 3 **")
print(f"Elemento en la posición 3: {lista.recuperar(3)}")  # Esperado: 10

print("\n** Recuperar en una posición inválida **")
print(f"Elemento en la posición 6: {lista.recuperar(6)}")  # Esperado: "Error: Posición inválida."

print("\n** Suprimir elemento en la posición 2 **")
suprimido = lista.suprimir(2)  # Esperado: Eliminar 7
print(f"Elemento suprimido: {suprimido}")  # Esperado: 7
lista.recorrer()  # Esperado: "5 10 15"

print("\n** Suprimir en una posición inválida **")
lista.suprimir(5)  # Posición 5 es inválida
lista.recorrer()  # Esperado: "5 10 15"

print("\n** Primer y último elemento **")
print(f"Primer elemento: {lista.primer_elemento()}")  # Esperado: 5
print(f"Último elemento: {lista.ultimo_elemento()}")  # Esperado: 15

print("\n** Posiciones siguiente y anterior **")
print(f"Siguiente posición de 2: {lista.siguiente_posicion(2)}")  # Esperado: 3
print(f"Anterior posición de 3: {lista.anterior_posicion(3)}")  # Esperado: 2

print("\n** Insertar y llenar la lista **")
lista.insertar(20, 4)
lista.insertar(25, 5)
lista.insertar(30, 6)
lista.insertar(35, 7)
lista.insertar(40, 8)
lista.insertar(45, 9)
lista.insertar(50, 10)  # La lista ahora debería estar llena
lista.recorrer()  # Esperado: "5 10 15 20 25 30 35 40 45 50"

print("\n** Insertar en una lista llena **")
lista.insertar(55, 11)  # Intentar insertar en lista llena
lista.recorrer()  # Esperado: "5 10 15 20 25 30 35 40 45 50"

print("\n** Supresión y recorrido final **")
lista.suprimir(1)  # Eliminar el primer elemento
lista.suprimir(5)  # Eliminar el elemento en la posición 5
lista.recorrer()  # Esperado: "10 15 20 25 35 40 45 50"