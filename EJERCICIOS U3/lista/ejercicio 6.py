class bloque_memoria:
    def __init__(self,inicio,tamaño):
        self.inicio = inicio
        self.tamaño = tamaño
    def __str__(self):
        return f"Inicio del bloque: {self.inicio} tamaño del bloque: {self.tamaño}\n"
class memoria_heap:
    def __init__(self,tamaño):
        self.tamaño = tamaño
        self.bloques_ocupados = []
        self.bloques_libres = [bloque_memoria(0,tamaño)]
        
    def asignar_memoria(self,tamaño):
        band = False
        if len(self.bloques_libres) != 0:
            for bloque in self.bloques_libres:
                if bloque.tamaño >= tamaño:
                    self.bloques_ocupados.append(bloque_memoria(bloque.inicio,tamaño))
                    band = True
                    bloque.inicio += tamaño
                    bloque.tamaño -= tamaño
                if bloque.tamaño == 0:
                    self.bloques_libres.remove(bloque)
            if not band:
                print("Tamaño ingresado mayor al disponible\n")
        else:
            print("La memoria está ocupada al maximo\n")
    def liberar_memoria(self,tamaño):
        i = 0
        band = False
        while i < len(self.bloques_ocupados) and not band:
            bloque = self.bloques_ocupados[i]
            if bloque.tamaño == tamaño:
                self.bloques_libres.append(bloque_memoria(bloque.inicio,bloque.tamaño))
                self.bloques_ocupados.remove(bloque)
                band = True
            else:
                i+=1
    def unir_memoria_libre(self):
        if len(self.bloques_libres) >1:
            i = 0
            k = 0
            while k < len(self.bloques_libres):
                i = 0
                j=i+1
                bloque_1 = self.bloques_libres[i]
                bloque_2 = self.bloques_libres[j]
                inicio = min(bloque_1.inicio,bloque_2.inicio)
                tamaño = bloque_1.tamaño + bloque_2.tamaño
                self.bloques_libres.append(bloque_memoria(inicio,tamaño))
                self.bloques_libres.remove(bloque_1)
                self.bloques_libres.remove(bloque_2)
                k+=1
    def mostrar_estado(self):
        print("BLOQUES LIBRES\n")
        if len(self.bloques_libres) == 0:
            print("No hay bloques libres\n")
        else:
            for bloque in heap.bloques_libres:
                print(bloque)
        print("----------------------------------\n")
        print("BLOQUES OCUPADOS\n")
        if len(self.bloques_ocupados) == 0:
            print("No hay bloques ocupados\n")
        else:
            for bloque in heap.bloques_ocupados:
                print(bloque)
        
heap = memoria_heap(100)
heap.mostrar_estado()
print("----------------------------------\n")
print("ASIGNAR 10 ESPACIOS DE MEMORIA\n")
heap.asignar_memoria(10)
heap.asignar_memoria(90)
heap.liberar_memoria(90)
heap.liberar_memoria(10)
heap.mostrar_estado()
heap.unir_memoria_libre()
heap.mostrar_estado()