import numpy as np

class Lista:
    def __init__(self) -> None:
        self.primero = None
        self.cant = 0
    
    def buscar_elem(self, x):
        if self.cant > 0:  # 1u
            aux = self.primero  # 1u
            p = 1  # 1u
            while aux and aux.get_dato() < x:  # 2n. Uso "<" porque no tiene sentido seguir comparando si la lista esta ordenada
                aux = aux.get_siguiente()  # 2n
                p += 1  # 2n
            if aux and aux.get_dato() == x:  # 3u
                return p  # 1u
        print("No encontrado")  # 1u
        return -1  # 1u
    
    # T(n) = 3u + 6n + 5u = 6n + 8u (Peor caso))
    # Pertence al orden de complejidad lineal O(n)