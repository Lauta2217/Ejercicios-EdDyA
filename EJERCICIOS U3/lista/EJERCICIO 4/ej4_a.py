class Nodo:
    def __init__(self, dato,fila,columna):
        self.dato = dato
        self.fila = fila
        self.columna = columna
        self.siguiente = None

class ListaEncadenada:
    def __init__(self,filas,columnas):
        self.cabeza = None
        self.cantidad = 0
        self.filas = filas
        self.columnas = columnas

    def insertar(self, x, p, f, c):
        nuevo = Nodo(x,f,c)
        if p == 1:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            for _ in range(1, p - 1):
                if actual is not None:
                    actual = actual.siguiente
            if actual is not None:
                nuevo.siguiente = actual.siguiente
                actual.siguiente = nuevo
        self.cantidad += 1

    """def suprimir(self, p):
        if p == 1 and self.cabeza is not None:
            eliminado = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            self.cantidad -= 1
            return eliminado
        else:
            actual = self.cabeza
            for _ in range(1, p - 1):
                if actual is not None and actual.siguiente is not None:
                    actual = actual.siguiente
            if actual is not None and actual.siguiente is not None:
                eliminado = actual.siguiente.dato
                actual.siguiente = actual.siguiente.siguiente
                self.cantidad -= 1
                return eliminado
        print("Error: Posición inválida.")
        return None

    def recuperar(self, p):
        actual = self.cabeza
        for _ in range(1, p):
            if actual is not None:
                actual = actual.siguiente
        if actual is not None:
            return actual.dato
        print("Error: Posición inválida.")
        return None

    def buscar(self, x):
        actual = self.cabeza
        pos = 1
        while actual is not None:
            if actual.dato == x:
                return pos
            actual = actual.siguiente
            pos += 1
        print("Error: Elemento no encontrado.")
        return None

    def primer_elemento(self):
        if self.cabeza is not None:
            return self.cabeza.dato
        print("Error: La lista está vacía.")
        return None

    def ultimo_elemento(self):
        actual = self.cabeza
        if actual is not None:
            while actual.siguiente is not None:
                actual = actual.siguiente
            return actual.dato
        print("Error: La lista está vacía.")
        return None

    def siguiente_posicion(self, p):
        actual = self.cabeza
        for _ in range(1, p):
            if actual is not None:
                actual = actual.siguiente
        if actual is not None and actual.siguiente is not None:
            return p + 1
        print("Error: No hay posición siguiente.")
        return None

    def anterior_posicion(self, p):
        if p > 1 and p <= self.cantidad:
            return p - 1
        print("Error: No hay posición anterior.")
        return None
"""
    def recorrer(self):
        actual = self.cabeza
        while actual is not None:
            print(f"Valor: {actual.dato}, Fila: {actual.fila}, Columna: {actual.columna}")
            actual = actual.siguiente
    def obtener_filas(self):
        return self.filas
    def obtener_columnas(self):
        return self.columnas
    def obtener_cabeza(self):
        return self.cabeza
    
def sumar(matriz1,matriz2):
    filas = max(matriz1.obtener_filas(),matriz2.obtener_filas()) #obtengo el numero mayor de filas
    columnas = max(matriz1.obtener_columnas(),matriz2.obtener_columnas()) #obtnego el numero mayor de columnas
    nueva_matriz = ListaEncadenada(filas,columnas) #creo mi nueva matriz
    actualm1 = matriz1.obtener_cabeza() #obtengo el primer elemento de la matriz 1
    actualm2 = matriz2.obtener_cabeza() #obtengo el primer elemento de la matriz 2
    pos = 1
    while actualm1 is not None and actualm2 is not None: #si ninguno de los elementos es None ingresa
        if (actualm1.fila, actualm1.columna) < (actualm2.fila, actualm2.columna): #en caso de que un elemento de la matriz 1 esté en una posicion anterior de la matriz 2 directamente se agrega el de la matriz 1 
            nueva_matriz.insertar(actualm1.dato, pos, actualm1.fila, actualm1.columna) #se agrega el elemento de la matriz 1
            actualm1 = actualm1.siguiente #movemos al siguiente elemento
            pos += 1 #aumentamos la posicion 
        elif (actualm1.fila, actualm1.columna) > (actualm2.fila, actualm2.columna): #en caso de que un elemento de la matriz 2 esté en una posicion anterior de la matriz 1 directamente se agrega el de la matriz 2
            nueva_matriz.insertar(actualm2.dato, pos, actualm2.fila, actualm2.columna) #se agrega el elemento de la matriz 2
            actualm2 = actualm2.siguiente #movemos al siguiente elemento
            pos += 1 #aumentamos la posicion 
        else: #en caso de que nos encontremos en la misma posicion en las 2 matrices
            valor = actualm1.dato + actualm2.dato #sumamos el valor de ambas posiciones
            nueva_matriz.insertar(valor, pos, actualm1.fila, actualm1.columna) # agregamos ese valor en la posicion dentro de la nueva matriz
            actualm1 = actualm1.siguiente #movemos al siguiente elemento
            actualm2 = actualm2.siguiente #movemos al siguiente elemento
            pos += 1 #aumentamos la posicion 

    while actualm1 is not None: #en caso de que hayan quedado elementos en la matriz 1 sin agregarse debido a que es más grande que la matriz 2
        nueva_matriz.insertar(actualm1.dato, pos, actualm1.fila, actualm1.columna) #se agrega el elemento de la matriz 1
        actualm1 = actualm1.siguiente  #movemos al siguiente elemento
        pos += 1  #aumentamos la posicion 

    while actualm2 is not None:  #en caso de que hayan quedado elementos en la matriz 2 sin agregarse debido a que es más grande que la matriz 1
        nueva_matriz.insertar(actualm2.dato, pos, actualm2.fila, actualm2.columna) #se agrega el elemento de la matriz 2
        actualm2 = actualm2.siguiente  #movemos al siguiente elemento
        pos += 1  #aumentamos la posicion 

    return nueva_matriz #retornamos nuestra suma de la matriz 1 y 2
    
if __name__=='__main__':
    matriz1 = ListaEncadenada(2,2)
    matriz2 = ListaEncadenada(2,4)
    #para matriz 1
    matriz1.insertar(1,1,1,1) # valor 1 en fila 1 columna 1
    matriz1.insertar(1,2,1,2) # valor 1 en fila 1 columna 2
    matriz1.insertar(1,3,2,1) # valor 1 en fila 2 columna 1
    matriz1.insertar(1,4,2,2) # valor 1 en fila 2 columna 2
    matriz1.recorrer()
    #para matriz 2
    matriz2.insertar(1,1,1,1) # valor 1 en fila 1 columna 1
    matriz2.insertar(1,2,1,2) # valor 1 en fila 1 columna 2
    matriz2.insertar(1,3,1,3) # valor 1 en fila 1 columna 3
    matriz2.insertar(0,4,1,4) # valor 0 en fila 1 columna 4       
    matriz2.insertar(1,5,2,1) # valor 1 en fila 2 columna 1
    matriz2.insertar(1,6,2,2) # valor 1 en fila 2 columna 2
    matriz2.insertar(1,7,2,3) # valor 1 en fila 2 columna 3  
    matriz2.insertar(0,8,2,4) # valor 0 en fila 2 columna 4
    matriz2.recorrer()
    print("\nMatriz 1 + matriz 2:\n")
    matriz1_mas_matriz2 = sumar(matriz1,matriz2)
    matriz1_mas_matriz2.recorrer()