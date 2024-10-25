import numpy as np
class Pila_sec:
    def __init__(self,cant):
        self.__elemento = np.zeros(cant,dtype=int)
        self.__tope = 0
        self.__cant_max = cant
    def pila_llena(self):
        return self.__tope == self.__cant_max
    def insertar_elem(self,dato):
        if not self.pila_llena():
            self.__elemento[self.__tope] = dato
            self.__tope+=1
        else:
            print("PUTOOO YA ESTA LLENAAA")
    def mostrar(self):
        for i in range(self.__tope-1,-1,-1):
            print(self.__elemento[i])

"""pila_sec = Pila_sec(3)

pila_sec.insertar_elem(1)
pila_sec.insertar_elem(2)
pila_sec.insertar_elem(3)
pila_sec.insertar_elem(4)
pila_sec.mostrar()"""
        
 #2a) Uso el TAD cola encadenada, debido a que sigue la politica FIFO primero en entrar primero en salir 
 #y ademas encadenada debido a que no se sabe la cantidad que va a ingresar
 #b)
"""class Nodo:
    def __init__(self,sig = None): #sig siempre en none porque siempre insertamos al final
        self.__dato = 0
        self.__sig = sig
    def obtener_dato(self):
        return self.__dato
    def obtener_sig(self):
        return self.__sig
    def set_sig(self,dato):
        self.__sig = dato
    def aumentar_espera(self):
        self.__dato+=15"""
class Cola_enc:
    def __init__(self):
         self.__pr = None
         self.__ul = None
         self.__cant_elementos = 0
    def insertar(self):
        nuevo = Nodo()
        if self.__cant_elementos == 0:
            self.__pr = nuevo
        else:
            self.__ul.set_sig(nuevo)
        self.__ul = nuevo
        self.__cant_elementos+=1    
    def surpimir_elem(self):
        if self.__cant_elementos == 0:
            print("No hay nada que eliminar")
        else:
            x = self.__pr.obtener_dato()
            self.__pr = self.__pr.obtener_sig()
            self.__cant_elementos-=1
            return x
    def vacia(self):
        return self.__cant_elementos ==0
#d)
    def simulacion(self):
        persona_en_cola = 0
        tiepo_simulacion = 60 * 5
        i = 0
        while i < tiepo_simulacion:
            if i % 10 == 0: #cada 10m llega un cliente
                Nuevo = Nodo()
                print("Nuevo cliente!!!!!!")
                self.insertar()
                persona_en_cola+=1
            Nuevo = Nodo()
            self.insertar()
            persona_en_cola+=1
            if not self.vacia():
                self.surpimir_elem()
                persona_en_cola-=1
                aux = self.__pr
                print("gpladadad")
                while aux is not None:
                    print("Espera aumentado")
                    aux.aumentar_espera()
                    aux = aux.obtener_sig()
            i+=15
        xmax = 0
        aux = self.__pr
        while aux is not None:
            if xmax < aux.obtener_dato():
                xmax = aux.obtener_dato()
            aux = aux.obtener_sig()
        print(f"Tiempo maximo de espera de los que no fueron atendidos por gorreados es de:{xmax}\n persona_en_cola: {persona_en_cola}")
            
"""if __name__=='__main__':
    cola_enc = Cola_enc()
    cola_enc.simulacion()"""
#3)
class Nodo:
    def __init__(self,dato,sig = None): #sig siempre en nonee
        self.__dato = dato
        self.__sig = sig
    def obtener_dato(self):
        return self.__dato
    def obtener_sig(self):
        return self.__sig
    def set_sig(self,dato):
        self.__sig = dato
class Lista_enc_ord:
    def __init__(self):
        self.__cantidad_elementos = 0
        self.__cabeza = None
    def vacia(self):
        return self.__cantidad_elementos == 0
    def insertar(self,dato):
        nuevo = Nodo(dato)
        if self.vacia() or self.__cabeza.obtener_dato() >= dato: #si la lista está vacia o el dato de la cabeza es mayor o igual al que queremos ingresar entonces el nuevo lo definimos como cabeza (tambien se pone el igual porque no tiene entrar al bucle si es lo mismo xd)
            nuevo.set_sig(self.__cabeza)#el siguiente del nuevo va a ser la cabeza ya que este sera la nueva cabeza
            self.__cabeza = nuevo #se define la cabeza
        else:
            aux =  self.__cabeza
            while aux is not None and aux.obtener_dato() < dato and aux.obtener_sig() is not None: #entra si el nodo no es none y aparte su dato es menor al que queremos ingresar
                aux = aux.obtener_sig() #pasamos al siguientee hasta que alguna condicion se cumpla
            if aux is not None: #si el nodo no es none entonces ingresamos
                nuevo.set_sig(aux.obtener_sig()) #el siguiente del nuevo va a ser el siguiente del nodo en el que estamos parados
                aux.set_sig(nuevo) #el siguiente del nodo en el que estamos parados va a ser el nuevo ej: ingresa el 5 por lo tanto esto es hacer 4 9 se cambia a 4 5 9
        self.__cantidad_elementos+=1#aumentamos la cantidad de elementos
    def buscar_elem(self,dato):
        if not self.vacia(): #1ut
            aux = self.__cabeza #1ut
            pos=1 #1ut
            while aux is not None and aux.obtener_dato() < dato: #n+3 ut
                aux = aux.obtener_sig() # 2n
                pos+=1 #2ut
            #total n+7
            if aux is not None: #1ut
                print(f"EL dato se encuentra en la posicion {pos}") #1ut
                #3n + 7 + 5 = 3n + 12 complejidad lineal
    def recorrer(self):
        if self.vacia():
            print("No hay elemento en la lista\n")
        else:
            aux = self.__cabeza
            while aux is not None: #mientras el nodo no sea none va mostrando hasta llegar al final que es none
                print(aux.obtener_dato())
                aux = aux.obtener_sig()
lista_enc_ord = Lista_enc_ord()
lista_enc_ord.insertar(2)
lista_enc_ord.insertar(1)
lista_enc_ord.insertar(3)
lista_enc_ord.recorrer()
lista_enc_ord.buscar_elem(2)