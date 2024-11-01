import numpy as np
import random
class tabla_hash_DA:
    __lista:np.array
    __tamaño:int
    def __init__(self,claves,primo):
        if primo:
            self.__tamaño = int(self.primo(int(claves/0.7)))
        else:
            self.__tamaño =int(claves/0.7)
        self.__lista = np.ndarray(self.__tamaño,dtype=object)
    def metodo_hash_extraccion(self,clave):
        return int(clave[-2::])
    def metodo_hash_division(self,clave):
        return int(int(clave) % self.__tamaño)
    def metodo_hash_alfanumerico(self,clave):
        suma = 0
        for char in str(clave):
            suma += ord(char)
        return int(suma % self.__tamaño)

    def insertar(self,clave):
        print("Insertando")
        direction = self.metodo_hash_division(clave)
        cont = 0
        while self.__lista[direction] is not None and cont < self.__tamaño:
            direction = (direction+1) % self.__tamaño
            cont+=1
        if cont < self.__tamaño:
            self.__lista[direction] = clave
            print(f"Insertada la clave {clave} en {cont} intentos\n")

    def buscar(self,clave):
        direction = self.metodo_hash_division(clave)
        cont = 0
        while self.__lista[direction] != clave and cont < self.__tamaño:
            direction = (direction+1) % self.__tamaño
            cont+=1
        if cont < self.__tamaño and self.__lista[direction] == clave:
            print(f"Encontrada la clave {clave} en {cont} comparaciones\n")
            
    def primo(self,valor):
        es_primo = False
        while not es_primo:
            i = 2
            while i < valor and valor % i != 0:
                i+=1
            if i == valor:
                es_primo = valor
            else:
                valor+=1
        return valor

"""if __name__ == '__main__':
    tabla = tabla_hash_DA(100,False)
    for _ in range(0,99):
        aux = str(random.randint(46000000,46999999))
        tabla.insertar(aux)
    tabla.insertar('46725519')
    tabla.buscar(aux)"""

class Nodo:
    __clave: str
    __sig: object
    def __init__(self,clave, sig = None):
        self.__clave = clave
        self.__sig = sig
    def get_sig(self):
        return self.__sig
    def set_sig(self,sig):
        self.__sig = sig
    def get_value(self):
        return int(self.__clave)
class tabla_hash_Enc:
    __lista: np.array
    __tamaño: int
    __colisiones: np.array
    def __init__(self,claves,prom_colisiones):
        self.__tamaño = int((claves) / prom_colisiones)
        self.__lista = np.ndarray(self.__tamaño,dtype=object)
        self.__colisiones = np.zeros(self.__tamaño,dtype=int)
    def metodo_hash_extraccion(self,clave):
        return int(clave[-2::])
    def metodo_hash_division(self,clave):
        return int(int(clave) % self.__tamaño)
    def metodo_hash_alfanumerico(self,clave):
        suma = 0
        for char in clave:
            suma+= ord(char)
        return int(suma % self.__tamaño)
    
    def insertar(self,clave):
        direction = self.metodo_hash_division(clave)
        nodo = Nodo(clave)
        if self.__lista[direction] is None:
            self.__lista[direction] = nodo
        else:
            nodo.set_sig(self.__lista[direction])
            self.__lista[direction] = nodo
        self.__colisiones[direction]+=1
    
    def buscar(self,clave):
        cont = 1
        direction = self.metodo_hash_division(clave)
        if self.__lista[direction] is None:
            print("No se encuentra\n")
        else:
            aux = self.__lista[direction]
            while aux is not None and aux.get_value() != int(clave):
                aux = aux.get_sig()
                cont+=1
            if aux is not None and aux.get_value() == int(clave):
                print(f"encontrado en {cont} intentos\n")
            else:
                print("NO encontrado")
    def cant_colisiones(self,clave):
        direction = self.metodo_hash_division(clave)
        print(F"Cantidad de colisiones en la direccion {clave} es de: {self.__colisiones[direction]}")
if __name__ == '__main__':
    tabla = tabla_hash_Enc(100,5)
    tabla.insertar('46725519')
    tabla.insertar('64725519')
    """ for _ in range(0,90):
        aux = str(random.randint(46000000,46999999))
        tabla.insertar(aux)
    tabla.insertar('46725519')
    tabla.insertar('46725519')
    tabla.insertar('46725519')
    tabla.insertar('46725519')"""
    tabla.buscar('46725519')
    tabla.cant_colisiones('46725519')
    #tabla.cant_colisiones(aux)
                