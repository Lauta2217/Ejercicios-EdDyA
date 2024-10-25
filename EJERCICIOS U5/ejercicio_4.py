import numpy as np
import random
class tabla_hash_buckets:
    __lista: np.array
    def __init__(self ,claves = 1000, capacidad_buckets= 5):
        self.__capacidad_buckets = capacidad_buckets
        self.__cantidad_buckets = int(claves / capacidad_buckets)
        self.__tamaño_overflow = int( self.__cantidad_buckets * 0.2)
        self.__lista = np.ndarray(self.__cantidad_buckets,dtype=object)
        for i in range(self.__cantidad_buckets):
            self.__lista[i] = []  # Cada bucket es una lista vacía
        self.__overflow= np.ndarray(self.__tamaño_overflow,dtype=object)
    def metodo_extraccion(self,clave):
        return int(clave[-2:]) 

    def insertar(self,clave):
        direccion = self.metodo_extraccion(clave)
        if len(self.__lista[direccion]) < self.__capacidad_buckets:
            self.__lista[direccion].append(clave)
            print(f"Clave: {clave} agregada en la direccion: {direccion}\n")
        else:
            print(f"Direccion: {direccion} llenó la capacidad\n")
            print(self.__overflow.size)
            if np.count_nonzero(self.__overflow) != self.__tamaño_overflow:
                print(f"Clave: {clave} agregada en overflow\n")
                self.__overflow = np.append(self.__overflow, clave)
            else:
                print("overflow lleno\n")
    def buscar(self,clave):
        cont = 0
        if self.__lista[self.metodo_extraccion(clave)] is not None:
            for clavee in self.__lista[self.metodo_extraccion(clave)]:
                if clavee == clave:
                    print(f"Se encontró en {cont} comparaciones\n")
                    return
                else:
                    cont+=1
        else:
            print("No existe esa clave en la tabla\n")
    def contar_desbordados(self):
        cont = 0
        for bucket in self.__lista:
            if len(bucket) == self.__capacidad_buckets:
                cont+=1
                #print(f"El bucket de direccion: {self.metodo_extraccion(bucket[0])} está desbordado\n")
        print(f"Cantidad de buckets desbordados: {cont}\n")
    def contar_subocupados(self):
        cont = 0
        for bucket in self.__lista:
            if len(bucket) < int(self.__capacidad_buckets/3):
                cont+=1
            #print(len(bucket))
                #if len(bucket) == 0:
                 #   print(f"bucket sin direccion asignada\n")
                #else:
                 #   print(f"El bucket de direccion: {self.metodo_extraccion(bucket[0])} está subocupado\n")
        print(f"Cantidad de buckets subocupados: {cont}\n")
                
    def contar_overflows(self):
        cant = 0
        for num in self.__overflow:
            if num is not None:
                cant+=1
        print(f"cantidad de claves en overflow:{cant}")

if __name__ == '__main__':
    tabla = tabla_hash_buckets()
    
    """claves = ['46053203', '46298769', '46110200', '46985797', '46207615', '46628562', '46453885', 
              '46078926', '46750425', '46115896', '46722722', '46463130', '46460886', '46622279', 
              '46798957', '46380717', '46747866', '46995056', '46458627', '46206004', '46515505', 
              '46350320', '46344209', '46516855', '46502060']"""
    for _ in range(0,1050):
        clave = str(random.randint(46000000,46999999))
        tabla.insertar(clave)
    
    tabla.contar_desbordados()
    tabla.contar_subocupados()
    tabla.contar_overflows()
    #tabla.buscar(claves[15])
#claves_ej5 = ['66','467','566','735','285','87']