import numpy as np
import random
class Nodo:
    def __init__(self,clave,sig = None):
        self.__clave = clave
        self.__sig = sig
    def obtener_valor(self):
        return self.__clave
    def obtener_sig(self):
        return self.__sig
    def set_sig(self,nodo):
        self.__sig = nodo
    def obtener_sig(self):
        return self.__sig
class tabla_hash_encadenada:
    __lista: np.array
    def __init__(self ,N = 100, promedio_colisiones = 5):
        self.__tamaño = int(N/promedio_colisiones)
        self.__lista = np.ndarray(self.__tamaño,dtype=Nodo)
        self.__colisiones = np.ndarray(self.__tamaño,dtype=int)
        for i in range(self.__tamaño):
            self.__colisiones[i] = 0
    def metodo_plegado(self,clave):
        clave_str = str(clave)
        suma = 0
        # Vamos sumando los dígitos en bloques de 2
        for i in range(0, len(clave_str), 2):
            suma += int(clave_str[i:i+2])
        # Retornamos la suma módulo del tamaño de la tabla
        return suma % self.__tamaño
    
    def obtener_colisiones(self):
        return self.__colisiones
    
    def insertar(self,clave):
        #Insertar por el final
        nodo = Nodo(clave)
        direccion = self.metodo_plegado(clave)
        if self.__lista[direccion] is None: 
            self.__lista[direccion] = nodo
            self.__colisiones[direccion]+=1
        else:
            aux = self.__lista[direccion]
            while aux.obtener_sig() is not None: #Si la clave ya existe se inserta? No, pero el cliente decide eso
                aux = aux.obtener_sig()
            aux.set_sig(nodo)
            self.__colisiones[direccion]+=1       
        
    def buscar(self,clave):
        direccion = self.metodo_plegado(clave)
        cont = 0
        if self.__lista[direccion] is not None:
            aux = self.__lista[direccion]
            while aux is not None and aux.obtener_valor() != clave:
                cont+=1
                aux = aux.obtener_sig()
            if aux is None:
                print("no se encontró")
            else:
                print(f"se encontró {aux.obtener_valor()} en {cont} intentos en la direccion: {direccion} \n")

if __name__ == '__main__':
    tabla = tabla_hash_encadenada() #para que sea primo el tamaño
    claves = ['66','467','566','735','285','87']
    for clave in claves:
        tabla.insertar(clave)
    for clave in claves:
        tabla.buscar(clave)
    """arre = []
    for _ in range(1,100):
        clave = str(random.randint(46000000,46999999))
        arre.append(clave)
        tabla.insertar(clave)
    for clave in arre:
        tabla.buscar(clave)
    suma = 0
    for i in range(len(tabla.obtener_colisiones())):
        print(f"En la direccion: {arre[i]} ocurrieron {tabla.obtener_colisiones()[i]} colisiones\n")
        suma+= tabla.obtener_colisiones()[i]
    print(f"Promedio: {suma/len(tabla.obtener_colisiones())}")"""
    