class ListaSecuencial:
    def __init__(self, filas,columnas):
        self.elementos = [[1 for _ in range(columnas+1)] for _ in range(filas+1)]
        self.filas = filas
        self.columnas = columnas
        self.Ult = -1  # Inicialmente no hay elementos

    def insertar(self,x,fila,columna):
        if 1 <= fila <= self.filas and 1 <= columna <= self.columnas:
            self.elementos[fila][columna] = x
            
    def recorrer(self):
        for i in range(1,self.filas+1):
            for j in range(1,self.columnas+1):
                    print(f"Valor: {self.elementos[i][j]}, Fila: {i}, Columna: {j}")
    
def sumar(matriz1,matriz2):
    filas = max(matriz1.filas,matriz2.filas)
    columnas = max(matriz1.columnas,matriz2.columnas)
    nueva_matriz = ListaSecuencial(filas,columnas)
    for i in range(1,filas+1):
        for j in range(1,columnas+1):
            valor = matriz1.elementos[i][j] + matriz2.elementos[i][j]
            print(valor)
            nueva_matriz.insertar(valor,i,j)
    return nueva_matriz

matriz1 = ListaSecuencial(10,10)
matriz1.insertar(10,10,10)

matriz2 = ListaSecuencial(10,10)
matriz2.insertar(10,10,10)

matriz3 = sumar(matriz1,matriz2)
matriz3.recorrer()

"""
Parte c: Comparación de Complejidad
Lista Encadenada (Parte a):
Espacio: La lista encadenada solo almacena los elementos no cero, junto con sus posiciones. La memoria usada depende del número de elementos no cero.
Tiempo: La suma de matrices se realiza recorriendo ambas listas enlazadas simultáneamente. Esto tiene una complejidad de 
𝑂(𝑁+𝑀) donde 𝑁 y 𝑀 son los números de elementos no cero en las dos matrices.
Arreglo Bidimensional (Parte b):
Espacio: Utiliza un arreglo de 100×100 ocupando espacio fijo independientemente del número de elementos no cero. 
Esto resulta en desperdicio de espacio si la matriz es rala.
Tiempo: La suma se realiza recorriendo cada elemento de las matrices, resultando en una complejidad de 𝑂(𝑛 elevado a 2)
donde 𝑛 es la dimensión de la matriz (en este caso, 100).
Conclusión
La representación con lista encadenada es más eficiente en términos de espacio y tiempo cuando se 
trabaja con matrices ralas, ya que evita almacenar y procesar los elementos cero.
La representación secuencial en un arreglo bidimensional es menos eficiente para matrices ralas porque 
ocupa más espacio al almacenar todos los elementos, incluidos los ceros, y tiene una mayor complejidad 
temporal al tener que iterar sobre todos los elementos.
Estas diferencias en eficiencia hacen que la elección de la estructura de datos dependa del número de 
elementos no cero en las matrices y del tamaño de las matrices mismas. Para matrices muy ralas, la 
representación con lista encadenada es la más adecuada.
"""