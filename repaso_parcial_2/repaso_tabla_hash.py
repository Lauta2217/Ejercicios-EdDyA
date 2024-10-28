import numpy as np
import random
class Tabla_Hash_direccionamiento_abierto: # ej1
    __lista: np.array
    __tamaño: int
    def __init__(self,claves = 100):
        self.__tamaño = claves
        self.__lista = np.empty(self.__tamaño,dtype=object)
    
    def metodo_hash_division(self,clave):
        return int(clave) % self.__tamaño
    
    def metodo_hash_extraccion(self,clave):
        return int(clave[-3:])
    
    def metodo_hash_plegado(self,clave):
        clave_str = str(clave)
        suma = 0
        # Vamos sumando los dígitos en bloques de 2
        for i in range(0, len(clave_str), 2):
            suma += int(clave_str[i:i+2])
        # Retornamos la suma módulo del tamaño de la tabla
        return suma % self.__M
    
    def metodo_hash_cuadrado_medio(self,clave):
        cuadrado = str(int(clave )** 2)
        # Extraemos los dígitos centrales
        mid_index = len(cuadrado) // 2
        if len(cuadrado) > 2:
            resultado = int(cuadrado[mid_index - 1: mid_index + 1])
        else:
            resultado = int(cuadrado)
        return resultado % self.__M
    
    def metodo_hash_alfanumerico(self,clave):
        suma = 0
        for char in str(clave):
            suma += ord(char)  # ord() devuelve el valor ASCII de un carácter
        return suma % self.__M
    
    def insertar(self,clave):
        cont = 0
        direction = self.metodo_hash_division(clave)
        while self.__lista[direction] is not None and cont != self.__tamaño:
            direction = (direction+1) % self.__tamaño
            cont+=1
        if cont != self.__tamaño:
            self.__lista[direction] = clave
            print(f"clave en direccion{direction}")
        else:
            print("lleno")
            
    def buscar(self,clave):
        cont = 1
        direction = self.metodo_hash_division(clave)
        band = False
        while self.__lista[direction] is not None and not band:
            if self.__lista[direction] == clave:
                band = True
                
            else:
                direction = (direction+1) % self.__tamaño
                cont+=1       
        if band:
            print(f"clave {clave} encontrada en {cont+1} comparaciones")
        else:
            print("No encontrada")
            
            
"""if __name__ == '__main__':
    tabla = Tabla_Hash_direccionamiento_abierto()
    
    for _ in range(0,99):
        aux = str(random.randint(46000000,46999999))
        tabla.insertar(aux)
    tabla.insertar('46725519')
    tabla.buscar(aux)"""
class Nodo:
    __valor:str
    __sig:object
    def __init__(self,valor,sig = None):
        self.__valor = valor
        self.__sig = sig
    def get_sig(self):
        return self.__sig
    def set_sig(self,sig):
        self.__sig = sig
    def get_value(self):
        return self.__valor
class Tabla_Hash_encadenamiento: #encadenamientp ej1
    __lista: np.array
    __tamaño: int
    def __init__(self,claves = 100):
        self.__tamaño = claves
        self.__lista = np.empty(self.__tamaño,dtype=object)
        self.__colisiones = np.zeros(self.__tamaño,dtype=object)
        
    def metodo_hash_plegado(self,clave):
        clave_str = str(clave)
        suma = 0
        # Vamos sumando los dígitos en bloques de 2
        for i in range(0, len(clave_str), 2):
            suma += int(clave_str[i:i+2])
        # Retornamos la suma módulo del tamaño de la tabla
        return suma % self.__tamaño
    
    def insertar(self,clave):
        direction = self.metodo_hash_plegado(clave)
        if self.__lista[direction] is None:
            nodo = Nodo(clave)
            self.__lista[direction] = nodo
        else:
            nodo = Nodo(clave,self.__lista[direction])
            self.__lista[direction] = nodo
            self.__colisiones[direction]+=1
    def buscar(self,clave):
        direction = self.metodo_hash_plegado(clave)
        if self.__lista[direction] is not None:
            actual = self.__lista[direction]
            band = False
            while actual is not None and not band:
                if actual.get_value() == clave:
                    band = True
                else:
                    actual = actual.get_sig()   
            if band:
                print("Encontrado")     
            else:
                print("No encontrado")     
    def cant_colisiones(self,clave):
        direction = self.metodo_hash_plegado(clave)
        if self.__colisiones[direction] is not None:
            print(f"cantidad de colisiones en la direccion {direction} es de {self.__colisiones[direction]}")
        else:
            print("Direccion no existente")
if __name__ == '__main__':
    tabla = Tabla_Hash_encadenamiento()
    for _ in range(0,90):
        aux = str(random.randint(46000000,46999999))
        tabla.insertar(aux)
    tabla.insertar('46725519')
    tabla.insertar('46725519')
    tabla.insertar('46725519')
    tabla.insertar('46725519')
    tabla.buscar('3233232')
    tabla.cant_colisiones('46725519')
    tabla.cant_colisiones(aux)