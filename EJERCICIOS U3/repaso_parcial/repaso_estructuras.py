import numpy as np
"""pila secuencial"""
class Pila_sec:
    def __init__(self,xmax):    
        self.__elementos = np.empty(xmax) #se crea el array con el tamaño dado
        self.__tope = 0 #Nos va a permitir saber la cantida de elementos y en la posicion en la cual se inserta
        self.__max = xmax #Maximo de elementos que se puede tener
        
    def vacia(self):
        return self.__tope == 0 #significa que no hay elementos en la pila
    
    def insertar(self,dato):
        if self.__tope < self.__max: #si la cantiad de elementos en la pila es menor a la maxima cantidad entonces entra
            self.__elementos[self.__tope] = dato #El tope sirve como posicion para insertar asi que lo usamos de indice
            self.__tope+=1 #aumentamos el tope para insertar en la proxima posicion y aumentar la cantidad de elementos
            print(f"Se insertó el elemento: {dato}\n")
        else:
            print("Lista llena, no se pueden insertar más elementos\n")
    def suprimir(self):
        if self.vacia() is False: #si hay elementos en la pila entra, es lo mismo que poner self.__tope > 0
            self.__elementos[self.__tope-1] = 0 #debido a que el tope siempre está una posicion mas adelante del ultimo componente se le resta uno
            self.__tope-=1 #restamos el tope para indicar que se eliminó un elemento y que esa posicion está disponible para insertar
        else:
            print("No hay elementos en la lista para suprimir\n")
    def recorrer(self):
        for i in range(self.__tope-1,-1,-1): #iniciamos en el tope-1 debido a que siempre está una posicion mas adelante del ultimo elementos, dejamos de iterar cuando i=-1 debido a que solo hay elementos hasta i=0 y vamos decrementando el tope para iterar
            print(round(self.__elementos[i])) #round porque me lo muestra como float
        
"""pila_sec = Pila_sec(2)
pila_sec.suprimir()
pila_sec.insertar(1)
pila_sec.insertar(2)
pila_sec.insertar(3)
pila_sec.suprimir()
pila_sec.insertar(3)
pila_sec.recorrer()   """ 

"""Pila encadenada"""
class Nodo:
    def __init__(self,dato,sig = None): #sig siempre en none porque siempre insertamos al final
        self.__dato = dato
        self.__sig = sig
    def obtener_dato(self):
        return self.__dato
    def obtener_sig(self):
        return self.__sig
    def set_sig(self,dato):
        self.__sig = dato
class Pila_enc:
    def __init__(self):
        self.__cant_elementos = 0
        self.__tope = None
   
    def vacia(self):
        return self.__cant_elementos == 0
    
    def insertar(self,dato):
        nuevo = Nodo(dato,self.__tope) #se le asigna el tope a cada elemento que entra porque al suprimir o recuperar se hace en orden lineal y permite cumplir con la politica LIFO
        self.__tope = nuevo
        self.__cant_elementos+=1 #aumentamos la cantidad de elementos
    def suprimir(self):
        if self.vacia():
            print("No hay elementos en la pila para suprimir\n")
        else:
            self.__tope = self.__tope.obtener_sig() #gracias a que cada elemento que entraba le asignabamos como siguiente el tope, ahora podemos suprimir asignando al tope el siguiente del que vamos a suprimir (es decir que el nuevo ultimo elemento va a ser el siguiente del que es el ultimo)
            self.__cant_elementos-=1 #disminuimos la cantidad de elementos
    def recorrer(self):
        aux = self.__tope
        while aux is not None:
            print(aux.obtener_dato())
            aux = aux.obtener_sig()

"""pila_enc = Pila_enc()
pila_enc.suprimir()
pila_enc.insertar(1)
pila_enc.insertar(2)
pila_enc.insertar(3)
pila_enc.suprimir()
pila_enc.insertar(3)
pila_enc.recorrer()  """

"""cola secuencial"""
class Cola_sec:
    def __init__(self,xmax):
        self.__elementos = np.empty(xmax) # creamos un array del tamaño ingresado
        self.__pr = 0 #primer elemento del array
        self.__ul = 0 #ultimo elemento del array
        self.__max_elementos = xmax #maxima cantida de elementos que pueden haber
        self.__cant_elementos = 0 #cantidad de elementos en la cola
    def vacia(self):
        return self.__cant_elementos == 0
    def modificar_pr(self):
        self.__pr = (self.__pr + 1) % self.__max_elementos # realiza el movimiento circular para que no hayan espacios libres y no poder isnertar (solo se modifica al suprimir y recorrer)
    def modificar_ul(self):
        self.__ul = (self.__ul + 1) % self.__max_elementos # realiza el movimiento circular(solo al insertar)
    def insertar(self,dato):
        if self.__cant_elementos < self.__max_elementos: #si la cantidad de elementos es menor a la cantidad maxima entonces entra
            self.__elementos[self.__ul] = dato #ingresamos siempre por la ultima posicion disponible
            self.modificar_ul() #se hace le movimiento cirular para poder obtener la siguiente posicion a insertar
            self.__cant_elementos +=1 #aumentamos la cantidad de elementos
        else:
            print("Cola llena\n")
    def suprimir(self):
        if self.vacia():
            print("Lista vacia no se puede suprimir nada\n")
        else:
            self.modificar_pr() #esto lo que haria es disminuir la primera componente que indica el primer elemento, si esta en la posicion 0 y suprimimos el elemento el pr va a pasar a ser 1 o lo equivalente a la siguiente posicion
            self.__cant_elementos-=1 #disminuimos la cantidad de elementos
    def recorrer(self):
        if self.vacia():
            print("No hay elementos en la cola\n")
        else:
            i = self.__pr #obtenemos la primera posicion
            j = 0 # esto no permite iterar por la cantidad de elementos
            while j < self.__cant_elementos:
                print(round(self.__elementos[i]))
                j+=1
                i = (i+1) % self.__max_elementos #movimiento cirular para obtener la siguiente posicion
       
"""cola_sec = Cola_sec(3)
cola_sec.suprimir()
cola_sec.insertar(1)
cola_sec.insertar(2)
cola_sec.insertar(3)
cola_sec.suprimir()
cola_sec.insertar(4)
cola_sec.recorrer()    """

"""cola encadenada"""
class Nodo:
    def __init__(self,dato,sig = None):
        self.__dato = dato
        self.__sig = sig
    def obtener_dato(self):
        return self.__dato
    def obtener_sig(self):
        return self.__sig
    def set_sig(self,dato):
        self.__sig = dato
class Cola_enc:
    def __init__(self):
        self.__cant_elementos = 0 #para contar la cantidad de elementos que hay
        self.__pr = None #al principio no hay ningun primer elemento
        self.__ul = None #al principio no hay ningun ultimo elemento
    def vacia(self):
        return self.__cant_elementos == 0
    def insertar(self,dato):
        nuevo = Nodo(dato) #creamos el nuevo elemento a ingresar
        if self.vacia(): #si no hay elementos entonces es el primer elemento
            self.__pr = nuevo
        else:
            self.__ul.set_sig(nuevo) #si hay elementos entonces va a ser el siguiente a ese
        self.__ul = nuevo #se ingresa como ultimo el nuevo dato siempre
        self.__cant_elementos+=1 #aumentamos la cantidad de elementos
    def suprimir(self):
        if self.vacia():
            print("No se puede suprimir nada, la cola está vacia\n")
        else:
            self.__pr = self.__pr.obtener_sig() #como la cola sigue la politica FIFO entonces solo eliminamos el primer elemento, entonces el primero ahora va a ser el que le sigue al que vamos eliminar
            self.__cant_elementos-=1
            if self.vacia(): 
                self.__ul = None #si eliminamos el ultimo dato que quedaba en la lista, entonces el ultimo queda en none nuevamente
    def recorrer(self):
        if self.vacia():
            print("Lista vacia\n")
        else:
            aux = self.__pr #como es la politica FIFO entonces empezamos a recorrer desde el primero
            while aux is not None:
                print(aux.obtener_dato())
                aux = aux.obtener_sig()

"""cola_enc = Cola_enc()
cola_enc.suprimir()
cola_enc.insertar(1)
cola_enc.insertar(2)
cola_enc.insertar(3)
cola_enc.suprimir()
cola_enc.insertar(1)
cola_enc.recorrer() """

"""lista secuencial"""
class Lista_sec:
    def __init__(self,xmax):
        self.__elementos = np.zeros(xmax,dtype=int) #creamos un array con el tamaño indicado
        self.__cant_elementos = 0 #cant de elementos
        self.__max_elementos = xmax #cantidad maxima de elementos que puede haber
    
    def vacia(self):
        return self.__cant_elementos == 0
    
    def insertar(self,dato,pos): #en las listas se ingresa por posicion
        if self.__cant_elementos == self.__max_elementos: #esto compara si la cantidad de elementos ya es igual a la maxima cantidad que puede haber
            print("Lista llena\n")
        else: #
            if 1 <= pos <= self.__cant_elementos+1: #primero compara si la posicion no es 0 y luego si la posicion es menor o igual a la cantidad maxima de elementos
                for i in range(self.__cant_elementos,pos-1,-1): #recorremos desde la ultima posicion ingresada, hasta la pos anterior a la que se quiere ingresar y decrementando la ultima posicion
                    #print(f"la i es:{i}, la posicion-1 es:{pos-1}")
                    self.__elementos[i] = self.__elementos[i-1] #shifteo a la derecha, es decir mueve todos los elementos una posicion a la derecha asi queda disponible la que queremos
                    #print(f"Se movio el elemento:{self.__elementos[i-1]} que estaba en la posicion {i-1} a la posicion {i}")
                    #print("ELEMENTOS ANTES DE INSERTAR:\n")
                    #self.recorrer()
                self.__elementos[pos-1] = dato # ingresa el elemento en la posicion dada
                #print("ELEMENTOS DESPUES DE INSERTAR:\n")
                #self.recorrer()
                self.__cant_elementos +=1 #aumenta la cantida de elementos
            else:
                print("Posicion invalida\n")
    def suprimir(self,pos):
        if self.vacia():
            print("Lista vacia\n")
        else:
            if 1 <= pos <= self.__cant_elementos: #primero compara si la posicion no es 0 y luego si la posicion es menor o igual a la cantidad de elementos
                for i in range(pos-1,self.__cant_elementos-1): # recorremos desde la posicion anterior a la ingresada hasta la cantida de elementos-1
                    self.__elementos[i] = self.__elementos[i+1] #shifteo a la izquierda,es decir mueve todos los elementos una posicion a la izquierda asi se elimina la ingresada
                self.__elementos[self.__cant_elementos-1] = 0 #en el espacio libre se coloca 0
                self.__cant_elementos -=1
    def recuperar(self,pos):
        if 1<= pos <= self.__cant_elementos: #primero compara si la posicion no es 0 y luego si la posicion es menor o igual a la cantidad de elementos
            print(f"dato:{self.__elementos[pos-1]}") # muestra el elemento restandole uno a la posicion ingresada porque es array
        else:
            print("Posicion invalida\n")
    def buscar(self,dato): #busqueda binaria
        band = False
        i = 0
        while i < self.__cant_elementos and not band: #mientas i sea menor a la cantida de elementos y no se haya encontrado el buscado
            if self.__elementos[i] == dato: #si el elemento se encuentra se cambia la bandera para que deje de iterar
                band = True
            else:
                i+=1 #si no se encuentra en la posicion i entonces se pasa al asiguiente
        if band: #si lo encontró muestra la posicion mas uno
            print(f"posicion en la que se encontró el dato:{i+1}")
        else:
            print("No se encontró\n")
    def primer_elemento(self):
        if self.__cant_elementos > 0: #si hay elementos entonces es el de la pos 0
            print(self.__elementos[0])
    def ultimo_elemento(self):
        if self.__cant_elementos > 0: #si hay elementos entonces es el de la ultima posicion menos 1 ya que al ingresar el ultimo elemento se aumentó
            print(self.__elementos[self.__cant_elementos-1])
    def siguiente(self,pos):
        if 1<= pos < self.__cant_elementos: #si la posicion es mayor que 0 o igual a 1 y menor a la cantidad de elementos que hay, esto porque el ultimo no tiene siguiente
            print(f"posicion siguiente: {pos+1}\n")
        else:
            print("La posicion ingresada no tiene una siguiente\n")
    def anterior(self,pos):
        if 1< pos <= self.__cant_elementos: #si la posicion es mayor que 1, ya que la posicion 1 no tiene anterior y menor o igual a la cantidad de elementos que hay
            print(f"posicion anterior: {pos-1}\n")
        else:
            print("La posicion ingresada no tiene una anterior\n")
    def recorrer(self):
        if self.vacia():
            print("Lista vacia\n")
        else:
            for i in range(self.__cant_elementos):#recorremos la cantidad de elementos 
                print(self.__elementos[i])
"""lista_sec = Lista_sec(3)
lista_sec.insertar(1,2)
lista_sec.buscar(1)
lista_sec.insertar(2,1)
lista_sec.insertar(3,2)
lista_sec.insertar(5,3)
lista_sec.suprimir(1)
lista_sec.recuperar(4)
lista_sec.buscar(2)
lista_sec.buscar(4)
lista_sec.primer_elemento()
lista_sec.ultimo_elemento()
lista_sec.siguiente(1)
lista_sec.siguiente(3)
lista_sec.anterior(2)
lista_sec.anterior(1)"""

"""lista encadenada"""
class Nodo:
    def __init__(self,dato,sig = None): #el siguiente siempre se inicializa en None
        self.__dato = dato
        self.__sig = sig
    def obtener_dato(self):
        return self.__dato
    def obtener_sig(self):
        return self.__sig
    def set_sig(self,dato):
        self.__sig = dato
class Lista_enc:
    def __init__(self):
        self.__cabeza = None #en un principio no hay elementos por eso la cabeza none..
        self.__cantidad_elementos = 0 #.. y la cantidad en 0
    def vacia(self):
        return self.__cantidad_elementos == 0
    def insertar(self,dato,pos):
        if 1 > pos > self.__cantidad_elementos+1: #si la posicion es 0 y es mayor a la cantidad de elementos+1 que hay tonce tamos mal, por ende si es menor a la cantidad de elementos +1 tamos joya
            print("Posicion invalida\n")
        else:
            nuevo = Nodo(dato)
            if pos == 1 and self.vacia(): #si no hay elementos y aparte quiere ingresar en la primera posicion entonces va directo a la cebeza
                nuevo.set_sig(self.__cabeza)
                self.__cabeza = nuevo
            else:
                aux = self.__cabeza
                for _ in range(1,pos-1): #nos movemos una posicion anterior a la que queremos agregar
                    if aux is not None: #ej: si pide ingresar en la posicion 7, pero solo hay elementos hasta en la 5 entonces la 6 es None y por ende la posicion 7 corresponde a invalida
                        aux = aux.obtener_sig()
                    else:
                        print("La posicion ingresada es invalida\n")
                if aux is not None: #lo mismo que el ejemplo si el dato de la posicion anterior en la que queremos ingresar es None entonces no podemos ingresar en esa pos
                    nuevo.set_sig(aux.obtener_sig()) #si se puede entonces hacemos la conexion
                    aux.set_sig(nuevo)
                else:
                        print("La posicion ingresada es invalida\n")
            self.__cantidad_elementos+=1 #aumentamos la cantidad de elementos

    def suprimir(self,pos):
        if 1 > pos > self.__cantidad_elementos: #si la posicion es 0 y es mayor a la cantidad de elementos+1 que hay tonce tamos mal, por ende si es menor a la cantidad de elementos +1 tamos joya
             print("Posicion invalida\n")
        else:
            if pos == 1: #si es el primer elemento como caso especial eliminamos la cabeza sin tener que llegar al for
                self.__cabeza= self.__cabeza.obtener_sig()
            else:
                aux = self.__cabeza
                for _ in range(1,pos-1):
                    if aux is not None: #ej: si pide suprimir en la posicion 7, pero solo hay elementos hasta en la 5 entonces la 6 es None y por ende la posicion 7 corresponde a invalida
                        aux = aux.obtener_sig()
                    else:
                        print("Posicion invalida\n")
                if aux is not None and aux.obtener_sig() is not None: #si el elemento de la posicion anterior a la ingresada es None entonces no se elimina nada y si el que le sigue tambien es None entonces la posicion ingresada a eliminar no tiene nada
                    aux.set_sig(aux.obtener_sig().obtener_sig()) #ej: si nos paramos en el nodo 1 su siguiente es el nodo 2 y el siguiente del nodo 2 es el nodo 3 entonces el siguiente del nodo 1 ahora es el nodo 3
                else:
                    print("Posicion invalida\n")
            self.__cantidad_elementos-=1

    def recuperar(self,pos):
        if 1 > pos > self.__cantidad_elementos: #si la posicion es 0 y es mayor a la cantidad de elementos+1 que hay tonce tamos mal, por ende si es menor a la cantidad de elementos +1 tamos joya
            print("posicion invalida\n")
        else:
            aux = self.__cabeza
            for _ in range(1,pos):
                if aux is not None: #ej: si pide pbtener el elemento de  la posicion 7, pero solo hay elementos hasta en la 5 entonces la 6 es None y por ende la posicion 7 corresponde a invalida
                    aux = aux.obtener_sig()
                else:
                    print("Posicion invalida\n")
            
            if aux is not None: # si el elemento es None lo muestra
                print(f"Elemento de la posicion {pos} es: {aux.obtener_dato()}")
            else:
                    print("Posicion invalida\n")
    def buscar(self,dato):
        aux = self.__cabeza
        pos = 1
        band = False
        while aux is not None and not band: #si hay elementos y la bandaera es False
            if aux.obtener_dato() == dato:
                band = True #si encuentra el dato la bandera cambia
            else:#sino
                aux = aux.obtener_sig()#se pasa al siguiente elemento
                pos+=1#se aumenta la posicion
        if band:# si se encontró muestra
            print(f"Elemento: {dato} en la posicion: {pos}")
        else:
                print("Posicion invalida\n")
    def primer_elemento(self):
        if not self.vacia(): #si hay elementos vacia entonces es la cabeza
            print(f"primer elemento: {self.__cabeza.obtener_dato()}")
    def ultimo_elemento(self):
        if not self.vacia(): #si hay elementos entonces busca
            aux = self.__cabeza
            while aux.obtener_sig() is not None: #si el siguiente no es None entra, esto porque el siguiente del ultimo es None en ese caso que no entre al while es porque ya tenemos el ultimo
                aux = aux.obtener_sig()
            print(f"ultimo elemento: {aux.obtener_dato()}")
    def siguiente(self,pos):
        if 1 <= pos < self.__cantidad_elementos: #si la posicion no es menor a 1 y es menor a la cantidad de elementos tonces tiene siguiente
            print(f"Siguiente posicion: {pos+1}")
        else:
            print("La posicion ingresada no tiene una siguiente\n")
    def anterior(self,pos):
        if 1 < pos <= self.__cantidad_elementos: #si la posicion no es menor o igual a 1 y no se pasa de la cantidad de elementos tonces tiene siguiente
            print(f"Siguiente posicion: {pos-1}")
        else:
            print("La posicion ingresada no tiene una anterior\n")
    def recorrer(self):
        if self.vacia():
            print("No hay elemento en la lista\n")
        else:
            aux = self.__cabeza
            while aux is not None:
                print(aux.obtener_dato())
                aux = aux.obtener_sig()
    
"""lista_enc = Lista_enc()
lista_enc.insertar(1,1)
lista_enc.insertar(2,2)
lista_enc.insertar(3,2)
lista_enc.recuperar(3)
lista_enc.recuperar(1)
lista_enc.buscar(2)
lista_enc.buscar(3)
lista_enc.primer_elemento()
lista_enc.ultimo_elemento()
lista_enc.siguiente(1)
lista_enc.siguiente(3)
lista_enc.anterior(2)
lista_enc.anterior(1)
lista_enc.recorrer()"""

"""lista secuencial ordenada por contenido"""
class Lista_sec_ord:
    def __init__(self,xmax):
        self.__elementos = np.empty(xmax,dtype=int) #crea el array del tamaño ingresado
        self.__cant_elementos = 0 #al principio no hay elementos
        self.__max_elementos = xmax #cantidad maxima de elementoss

    def vacia(self):
        return self.__cant_elementos== 0
    def insertar(self,dato):    
        if self.__cant_elementos == self.__max_elementos: #si está llena no se puede insertar mas nada
            print("Lista llena\n")
        else:
            pos = 0
            while pos < self.__cant_elementos and self.__elementos[pos] <= dato: #evalua si la posicion es menor a la cantidad de elementos y el dato de esa posicion es menor o igual al dato
                                                                                #si el dato de la posicion no es menor o igual al dato entonces ya tenemos la posicion para guardar el nuevo dato ordenado 
                pos+=1
            for i in range(self.__cant_elementos,pos,-1): #recorremos desde la cantidad de elementos, hasta la posicion en la cual se debe ingresar el dato y decrementando en 1
                self.__elementos[i] = self.__elementos[i-1] #shifteo a la derecha 
            self.__elementos[pos] = dato #ingresa el dato en la posicion
            self.__cant_elementos+=1
 
    def suprimir(self,pos):
        if self.vacia():
            print("Lista vacia\n")
        else:
            if 1 <= pos <= self.__cant_elementos: #evalua si la posicion es mayor que 1 y menor o igual a la cantidad de elementos que hay
                for i in range(pos-1,self.__cant_elementos-1): #recorremos desde la posicion anterior a eliminar, hasta la cantidad de elementos -1
                    self.__elementos[i] = self.__elementos[i+1] #shifteo a la izquierda
                self.__elementos[self.__cant_elementos-1] =0 # colocamos 0 en la posicion que suprimimos
                self.__cant_elementos-=1 #para no ingresar a esa posicion xd
    def recuperar(self,pos):
        if 1<= pos <= self.__cant_elementos: #evalua si la posicion es mayor que 1 y menor o igual a la cantidad de elementos que hay
            print(f"dato:{self.__elementos[pos-1]}")
        else:
            print("Posicion invalida\n")
    def buscar(self,dato):#como es una lista secuencial y ordenada usamos la bendita busqueda binaria
        band = False
        inicio = 0
        fin = self.__cant_elementos - 1  # __Ult representa el número de elementos, por eso restamos 1 para obtener el último índice
        while inicio <= fin and not band: #mientras el inicio sea menor o igual al fin y no se haya encontrado el dato inngresa
            medio = (inicio + fin) // 2 #se saca la mitad de la lista
            if self.__elementos[medio] == dato: #si se encuentra en la mitad 
                medio += 1 #aumentamos en 1 la posicion donde se encontró para mostrar
                band = True #para que no entre al while de nuevo
            elif self.__elementos[medio] < dato: # si el elemento del medio es menor al dato entonces vamos achicando hacia la derecha
                inicio = medio + 1
            else:
                fin = medio - 1 # si el elemento del medio es menor al dato entonces vamos achicando hacia izquierda
        if band:
            print(f"Elemento en la posicion:{medio}")
    def primer_elemento(self):
        if self.__cant_elementos > 0: #si hay elementos entonces es el primero
            print(self.__elementos[0])
    def ultimo_elemento(self):
        if self.__cant_elementos > 0: #si hay elementos es el ultimo, es decir cantidad de elementos -1
            print(self.__elementos[self.__cant_elementos-1])
    def siguiente(self,pos):
        if 1<= pos < self.__cant_elementos: #si la posicion es mayor o igual a 1 y menor a la cantidad de elementos tonces tiene siguiente
            print(f"posicion siguiente: {pos+1}\n")
        else:
            print("La posicion ingresada no tiene una siguiente\n")
    def anterior(self,pos):
        if 1< pos <= self.__cant_elementos: #si la posicion es mayor a 1 y menor o igual cantidad de elementos tonces tiene anterior
            print(f"posicion anterior: {pos-1}\n")
        else:
            print("La posicion ingresada no tiene una anterior\n")
    def recorrer(self):
        if self.vacia():
            print("Lista vacia\n")
        else:
            for i in range(self.__cant_elementos):
                print(self.__elementos[i])
"""lista_sec_ord = Lista_sec_ord(3)
lista_sec_ord.insertar(2)
lista_sec_ord.insertar(3)
lista_sec_ord.insertar(1)
lista_sec_ord.insertar(5)
lista_sec_ord.recuperar(3)
lista_sec_ord.recuperar(4)
lista_sec_ord.buscar(2)
lista_sec_ord.buscar(4)
lista_sec_ord.primer_elemento()
lista_sec_ord.ultimo_elemento()
lista_sec_ord.siguiente(1)
lista_sec_ord.siguiente(3)
lista_sec_ord.anterior(2)
lista_sec_ord.anterior(1)
lista_sec_ord.recorrer()"""

"""lista encadenada ordenada por contenido"""
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
        self.__cabeza = None
        self.__cantidad_elementos = 0
   
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
    def suprimir(self,pos):
        if 1 > pos > self.__cantidad_elementos: #si la posicion es 0 y es mayor a la cantidad de elementos+1 que hay tonce tamos mal, por ende si es menor a la cantidad de elementos +1 tamos joya
             print("Posicion invalida\n")
        else:
            if pos == 1: #caso especial que la posicion a eliminar sea la primera entonces la cabeza va a ser el elemento siguiente a la cabeza actual
                self.__cabeza = self.__cabeza.obtener_sig()
            else:
                aux = self.__cabeza
                for _ in range(1,pos-1): #nos movemos una posicion anterior a la ingresada para hacer las conexiones
                    if aux is not None: # si el nodo actual no es none entonces todavia hay elementos
                        aux = aux.obtener_sig()
                    else:
                        print("Posicion invalida\n")
                if aux is not None and aux.obtener_sig() is not None: #si el nodo de la posicion anterior a la ingresada es None entonces no se elimina nada y si el que le sigue tambien es None entonces la posicion ingresada a eliminar no tiene nada
                    aux.set_sig(aux.obtener_sig().obtener_sig()) #ej: si nos paramos en el nodo 1 su siguiente es el nodo 2 y el siguiente del nodo 2 es el nodo 3 entonces el siguiente del nodo 1 ahora es el nodo 3
                else:
                    print("Posicion invalida\n")
            self.__cantidad_elementos-=1 #disminuimos la cantidad de elementos

    def recuperar(self,pos):
        if 1 > pos > self.__cantidad_elementos: #si la posicion  es 0 o  mayor a la cantidad de elementos entonces es invalida
            print("posicion invalida\n")
        else:
            aux = self.__cabeza
            for _ in range(1,pos): #nos movemos hasta la posicion ingresada por eso no se le resta 1
                if aux is not None: # si el nodo actual no es none entonces no hemos llegado al final
                    aux = aux.obtener_sig()
                else:
                    print("Posicion invalida\n")
            
            if aux is not None: #si el actual es none entonces la posicion ingresada es mayor a la cantidad de elementos
                print(f"Elemento de la posicion {pos} es: {aux.obtener_dato()}")
            else:
                    print("Posicion invalida\n")
    def buscar(self,dato):
        aux = self.__cabeza
        pos = 0
        band = False
        while aux is not None and not band: #mientras el nodo no sea none y no se haya encontrado el dato entonces entra
            if aux.obtener_dato() == dato: #si el dato del nodo es el buscado cambiamos la bandera para que corte la iteracion
                band = True
            else:
                aux = aux.obtener_sig() #sino pasamos al siguiente
                pos+=1 #aumentamos la posicion para mostrar despues
        if band:
            print(f"Elemento: {dato} en la posicion: {pos}")
        else:
                print("No se encuentra el dato\n")
    def primer_elemento(self):
        if not self.vacia(): #si la lista tiene elementos entonces es la cabeza
            print(f"primer elemento: {self.__cabeza.obtener_dato()}")
    def ultimo_elemento(self):
        if not self.vacia(): #si la lista tiene elementos entonces recorremos hasta el final
            aux = self.__cabeza
            while aux.obtener_sig() is not None:
                aux = aux.obtener_sig()
            print(f"ultimo elemento: {aux.obtener_dato()}")
    def siguiente(self,pos):
        if 1 <= pos < self.__cantidad_elementos: #si la posicion es 0 entonces no es valida y si es mayor a la cantidad de elementos entonces no tiene siguiente
            print(f"Siguiente posicion: {pos+1}")
        else:
            print("La posicion ingresada no tiene una siguiente\n")
    def anterior(self,pos):
        if 1 < pos <= self.__cantidad_elementos: #si la posicion es 1 no tiene anterior y si es mayor que la cantidad de elementos no tiene anterior
            print(f"Siguiente posicion: {pos-1}")
        else:
            print("La posicion ingresada no tiene una anterior\n")
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
lista_enc_ord.insertar(4)
lista_enc_ord.insertar(5)
lista_enc_ord.insertar(1)
lista_enc_ord.insertar(215)
lista_enc_ord.insertar(2)
"""lista_enc_ord.recuperar(3)
lista_enc_ord.recuperar(1)
lista_enc_ord.buscar(2)
lista_enc_ord.buscar(3)
lista_enc_ord.primer_elemento()
lista_enc_ord.ultimo_elemento()
lista_enc_ord.siguiente(1)
lista_enc_ord.siguiente(3)
lista_enc_ord.anterior(2)
lista_enc_ord.anterior(1)"""
lista_enc_ord.recorrer()

