class Celda:
    def __init__(self, item=0, siguiente=-1):
        self.item = item
        self.siguiente = siguiente

class ListaConCursores:
    def __init__(self, max_size=100):
        self.espacio = [Celda() for _ in range(max_size)]
        self.cabeza = -1
        self.disponible = 0
        for i in range(max_size - 1):
            self.espacio[i].siguiente = i + 1
        self.espacio[max_size - 1].siguiente = -1

    def insertar(self, x, p):
        if self.disponible != -1:
            nuevo = self.disponible
            self.disponible = self.espacio[nuevo].siguiente

            self.espacio[nuevo].item = x

            if p == 1:
                self.espacio[nuevo].siguiente = self.cabeza
                self.cabeza = nuevo
            else:
                actual = self.cabeza
                for _ in range(1, p - 1):
                    if actual != -1:
                        actual = self.espacio[actual].siguiente
                if actual != -1:
                    self.espacio[nuevo].siguiente = self.espacio[actual].siguiente
                    self.espacio[actual].siguiente = nuevo
        else:
            print("Error: No hay espacio disponible.")

    def recuperar(self, p):
        actual = self.cabeza
        for _ in range(1, p):
            if actual != -1:
                actual = self.espacio[actual].siguiente
        if actual != -1:
            return self.espacio[actual].item
        return None

# Ejemplo de uso:
lista_cursor = ListaConCursores()
lista_cursor.insertar(10, 1)
lista_cursor.insertar(20, 2)
print(lista_cursor.recuperar(2))  # Output: 20
