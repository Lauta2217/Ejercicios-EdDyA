import numpy as np

class ListaSecuencial:
    def __init__(self, max_size=100):
        self.elementos = np.full(max_size, None)  # Inicializa con None usando un arreglo de numpy
        self.Ult = -1  # Inicialmente no hay elementos
        self.tamaño = 0
        
    def vacia(self):
        return self.Ult == -1
    
    def insertar(self, x, p):
        if self.Ult < len(self.elementos) - 1 and 1 <= p <= self.Ult + 2:
            # Desplazar elementos hacia la derecha usando un bucle
            for i in range(self.Ult, p - 2, -1):
                self.elementos[i + 1] = self.elementos[i]
            self.elementos[p - 1] = x
            self.Ult += 1
            self.tamaño+=1
        else:
            print("Error: Posición inválida o lista llena.")

    def suprimir(self, p):
        if 0 <= p - 1 <= self.Ult:
            x = self.elementos[p - 1]
            # Desplazar elementos hacia la izquierda usando un bucle
            for i in range(p - 1, self.Ult):
                self.elementos[i] = self.elementos[i + 1]
            self.elementos[self.Ult] = None
            self.Ult -= 1
            self.tamaño-=1
            return x
        else:
            print("Error: Posición inválida.")
            return None

    def recuperar(self, p):
        if 0 <= p - 1 <= self.Ult:
            return self.elementos[p - 1]
        else:
            print("Error: Posición inválida.")
            return None

    def buscar(self, x):
        for i in range(self.Ult + 1):
            if self.elementos[i] == x:
                return i + 1  # Retorna la posición (1-indexada)
        return None  # Elemento no encontrado

    def primer_elemento(self):
        if self.Ult >= 0:
            return self.elementos[0]
        else:
            print("Error: La lista está vacía.")
            return None

    def ultimo_elemento(self):
        if self.Ult >= 0:
            return self.elementos[self.Ult]
        else:
            print("Error: La lista está vacía.")
            return None

    def siguiente_posicion(self, p):
        if 1 <= p < self.Ult + 1:
            return p + 1
        else:
            print("Error: No hay posición siguiente.")
            return None

    def anterior_posicion(self, p):
        if 1 < p <= self.Ult + 1:
            return p - 1
        else:
            print("Error: No hay posición anterior.")
            return None

    def recorrer(self):
        if not self.vacia():
            for i in range(self.Ult + 1):
                print(self.elementos[i], end=" ")
            print()
        else:
            print("Lista vacia\n")

# Ejemplo de uso:
lista_seq = ListaSecuencial()
lista_seq.insertar(10, 1)
lista_seq.insertar(20, 2)
lista_seq.insertar(30, 3)
if lista_seq.llena():
    print("esta llena")
print("Lista después de insertar 10, 20, 30:")
lista_seq.recorrer()  # Output: 10 20 30

pos = lista_seq.buscar(20)
print(f"Elemento 20 encontrado en la posición: {pos}")  # Output: 2

primer = lista_seq.primer_elemento()
print(f"Primer elemento: {primer}")  # Output: 10

ultimo = lista_seq.ultimo_elemento()
print(f"Último elemento: {ultimo}")  # Output: 30

siguiente = lista_seq.siguiente_posicion(2)
print(f"Siguiente posición después de 2: {siguiente}")  # Output: 3

anterior = lista_seq.anterior_posicion(3)
print(f"Posición anterior a 3: {anterior}")  # Output: 2
