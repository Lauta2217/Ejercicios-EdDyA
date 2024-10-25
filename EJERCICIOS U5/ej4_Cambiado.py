import numpy as np
import random
class tabla_hash_buckets:
    __lista: np.ndarray
    __capacidad_buckets:int
    __tamaño: int
    __contadores: list
    def __init__(self ,claves = 1000, capacidad_buckets=4):
        self.__capacidad_buckets = capacidad_buckets
        self.__tamaño = int(claves/capacidad_buckets + (claves / capacidad_buckets )* 0.2)
        self.__lista = np.zeros((300,4))
        self.__contadores = np.zeros(self.__tamaño,dtype=int)
        self.__direccion_overflow = int(claves/capacidad_buckets)
    def metodo_extraccion(self,clave):
        return int(clave[-2:])

    def insertar(self,clave):
        direccion = self.metodo_extraccion(clave)
        if self.__contadores[direccion] < self.__capacidad_buckets:
            self.__lista[direccion][self.__contadores[direccion]]= clave
            print(self.__lista[direccion][self.__contadores[direccion]])

            self.__contadores[direccion] += 1
            print(f"Insertó en la direccion{direccion} la clave {clave}")
            self.buscar(clave)
            
            
        else:
            aux = self.__direccion_overflow
            while self.__contadores[aux] >= self.__capacidad_buckets and aux < self.__tamaño-1:
                aux+=1
            if aux < self.__tamaño-1:
                self.__lista[aux][self.__contadores[aux]] = clave
                self.__contadores[aux] += 1
                print(f"Insertó en la direccion{aux} la clave {clave} en overflow")
        
                
    def buscar(self,clave):
        cont = 0
        direccion = self.metodo_extraccion(clave)

        i = 0
        while i < self.__capacidad_buckets:
            if self.__lista[direccion][i]== float(clave):
                print(f"Se encontró  {clave} en {cont} comparaciones\n")
                i = 4
            else:
                cont+=1
                i+=1
            
    def contar_desbordados(self):
        cont = 0
        i = 0
        while i < self.__tamaño:
            if self.__contadores[i] == self.__capacidad_buckets:
                cont+=1
            i+=1
        print(f"Cantidad de buckets desbordados de los 300: {cont}\n")
    def contar_subocupados(self):
        cont = 0
        i = 0
        while i < self.__tamaño:
            if self.__contadores[i] <  int(self.__capacidad_buckets/3):
                cont+=1
            i+=1
        print(f"Cantidad de buckets subocupados de los 300: {cont}\n")
                
    def contar_overflows(self):
        cont = 0
        aux = self.__direccion_overflow
        while aux < self.__tamaño:
            if self.__contadores[aux] == self.__capacidad_buckets:
                cont+=1
            aux+=1
        print(f"cantidad de claves en overflow:{cont}\n")
    def contar_otros(self):
        cont = 0
        for bucket in self.__lista:
            if np.count_nonzero(bucket) >int(self.__capacidad_buckets/3) and np.count_nonzero(bucket) != self.__capacidad_buckets:
                cont+=1
        print(f"Cantidad de buckets que no entran en los subocupados o desbordados: {cont}\n")
if __name__ == '__main__':
    tabla = tabla_hash_buckets()
    for _ in range(0,1000):
        clave = str(random.randint(46000000,46999999))
        aux = clave
        tabla.insertar(clave)    
    tabla.contar_desbordados()
    tabla.contar_subocupados()
    tabla.contar_overflows()
    tabla.contar_otros()
    
    #claves_ej5 = ['66','467','566','735','285','87']
