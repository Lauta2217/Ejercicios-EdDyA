class Nodo:
    def __init__(self):
        self.dato = None
        self.siguiente = -2  # Equivalente a null en esta implementación

    def set_dato(self, x):
        self.dato = x

    def obtener_dato(self):
        return self.dato

    def set_siguiente(self, xp):
        self.siguiente = xp

    def obtener_siguiente(self):
        return self.siguiente
    
class Lista:
    def __init__(self, xmax):
        self.max = xmax
        self.cab = 0
        self.cantidad = 0
        self.espacio = [Nodo() for _ in range(xmax)]
        self.disponible = 0

    def vacia(self):
        return self.cantidad == 0

    def obtener_disponible(self):
        for i in range(self.max):
            if self.espacio[i].obtener_siguiente() == -2:
                return i
        return -2

    def free_disponible(self, disp):
        if 0 <= disp < self.max:
            self.espacio[disp].set_siguiente(-2)
            return True
        return False

    def insertar(self, x, xp=None):  # xp es opcional para manejar inserción por contenido o posición
        if self.cantidad >= self.max:
            print("Espacio lleno.")
            return False

        self.disponible = self.obtener_disponible()
        if self.disponible == -2:
            print("No hay espacio disponible.")
            return False

        self.espacio[self.disponible].set_dato(x)

        if xp is None:  # Inserción por contenido
            ant = self.cab
            cabeza = self.cab
            i = 0
            while i < self.cantidad and cabeza != -1 and self.espacio[cabeza].obtener_dato() < x:
                i += 1
                ant = cabeza
                cabeza = self.espacio[cabeza].obtener_siguiente()

            if cabeza == self.cab:  # Insertar al inicio de la lista
                if self.cantidad == 0:
                    self.espacio[self.cab].set_siguiente(-1)
                else:
                    self.espacio[self.disponible].set_siguiente(self.cab)
                self.cab = self.disponible
            elif cabeza == -1:  # Insertar al final de la lista
                self.espacio[self.disponible].set_siguiente(-1)
                self.espacio[ant].set_siguiente(self.disponible)
            else:
                self.espacio[self.disponible].set_siguiente(cabeza)
                self.espacio[ant].set_siguiente(self.disponible)
        else:  # Inserción por posición
            if not (0 <= xp <= self.cantidad):
                print("Posición incorrecta.")
                return False

            ant = self.cab
            cabeza = self.cab
            i = 0
            while i < xp:
                i += 1
                ant = cabeza
                cabeza = self.espacio[cabeza].obtener_siguiente()

            if cabeza == self.cab:  # Insertar al inicio de la lista
                if self.cantidad == 0:
                    self.espacio[self.cab].set_siguiente(-1)
                else:
                    self.espacio[self.disponible].set_siguiente(self.cab)
                self.cab = self.disponible
            elif cabeza == -1:  # Insertar al final de la lista
                self.espacio[self.disponible].set_siguiente(-1)
                self.espacio[ant].set_siguiente(self.disponible)
            else:
                self.espacio[self.disponible].set_siguiente(cabeza)
                self.espacio[ant].set_siguiente(self.disponible)

        self.cantidad += 1
        return True

    def suprimir(self, xp):
        if self.cantidad == 0 or not (0 <= xp < self.cantidad):
            print("Lista vacía o posición incorrecta.")
            return False

        ant = self.cab
        cabeza = self.cab
        i = 0
        while i < xp and cabeza != -1:
            i += 1
            ant = cabeza
            cabeza = self.espacio[cabeza].obtener_siguiente()

        if cabeza == self.cab:
            if self.cantidad == 1:
                self.cab = 0
            else:
                self.cab = self.espacio[cabeza].obtener_siguiente()
        else:
            self.espacio[ant].set_siguiente(self.espacio[cabeza].obtener_siguiente())

        self.free_disponible(cabeza)
        self.cantidad -= 1
        return True

    def recuperar(self, xp):
        if self.cantidad == 0 or not (0 <= xp < self.cantidad):
            print("Lista vacía o posición incorrecta.")
            return None

        cabeza = self.cab
        i = 0
        while cabeza != -1 and i < xp:
            i += 1
            cabeza = self.espacio[cabeza].obtener_siguiente()

        return self.espacio[cabeza].obtener_dato() if cabeza != -1 else None

    def buscar(self, x):
        if self.cantidad == 0:
            print("Lista vacía.")
            return None

        cabeza = self.cab
        i = 0
        while i < self.cantidad and cabeza != -1 and self.espacio[cabeza].obtener_dato() != x:
            i += 1
            cabeza = self.espacio[cabeza].obtener_siguiente()

        return i if i < self.cantidad else None

    def recorrer(self):
        if self.cantidad == 0:
            print("Lista vacía.")
            return False

        cabeza = self.cab
        elementos = []
        while cabeza != -1:
            elementos.append(self.espacio[cabeza].obtener_dato())
            cabeza = self.espacio[cabeza].obtener_siguiente()

        print("Lista:", " ".join(map(str, elementos)))
        return True

print("Creando lista con capacidad máxima de 5...")
lista = Lista(5)

# Insertar elementos por contenido
print("\nInsertando elementos por contenido...")
print("Insertar 10:", lista.insertar(10))
print("Insertar 20:", lista.insertar(20))
print("Insertar 15:", lista.insertar(15))

# Recorrer la lista
print("\nRecorriendo la lista actual:")
lista.recorrer()  # Debería mostrar: 10 15 20

# Insertar elementos por posición
print("\nInsertando elementos por posición...")
print("Insertar 5 en la posición 0:", lista.insertar(5, 0))  # Insertar al inicio
print("Insertar 25 en la posición 4:", lista.insertar(25, 4))  # Insertar al final

# Recorrer la lista después de insertar por posición
print("\nRecorriendo la lista después de inserciones por posición:")
lista.recorrer()  # Debería mostrar: 5 10 15 20 25

# Recuperar elementos
print("\nRecuperando elementos...")
x = lista.recuperar(0)
if x is not None:
    print("Elemento en posición 0:", x)
x = lista.recuperar(3)
if x is not None:
    print("Elemento en posición 3:", x)

# Buscar elementos
print("\nBuscando elementos...")
xp = lista.buscar(15)
if xp is not None:
    print("15 encontrado en posición:", xp)
else:
    print("15 no encontrado.")

# Suprimir elementos
print("\nSuprimiendo elementos...")
if lista.suprimir(2):
    print("Elemento suprimido en posición 2.")
else:
    print("No se pudo suprimir elemento en posición 2.")

# Recorrer la lista después de supresión
print("\nRecorriendo la lista después de supresión:")
lista.recorrer()  # Debería mostrar: 5 10 20 25

# Probar lista vacía
print("\nVaciando la lista...")
lista.suprimir(0)
lista.suprimir(0)
lista.suprimir(0)