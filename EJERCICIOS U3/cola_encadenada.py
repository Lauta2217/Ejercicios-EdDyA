class Celda:
    def __init__(self, item=0, sig=None):
        self.__item = item  # Almacena el valor del nodo
        self.__sig = sig  # Almacena la referencia al siguiente nodo (inicialmente None)

    def obtener_item(self):
        return self.__item  # Devuelve el valor almacenado en el nodo

    def cargar_item(self, item):
        self.__item = item  # Asigna un valor al nodo

    def cargar_sig(self, tope):
        self.__sig = tope  # Asigna el siguiente nodo en la lista enlazada

    def obtener_sig(self):
        return self.__sig  # Devuelve el siguiente nodo en la lista enlazada
class Cola:
    def __init__(self, pr=None, ul=None, cant=0):
        self.__pr = pr  # Puntero al primer nodo de la cola
        self.__ul = ul  # Puntero al último nodo de la cola
        self.__cant = cant  # Número de elementos en la cola

    def vacia(self):
        return self.__cant == 0  # Devuelve True si la cola está vacía
    def obtener_pr(self):
        return self.__pr
    def obtener_ul(self):
        return self.__ul
    def obtener_cant(self):
        return self.__cant
    def cargar_pr(self,dato):
        self.__pr = dato
    def cargar_ul(self,dato):
        self.__ul = dato
    def aumentar_cant(self):
        self.__cant+=1
    def disminuir_cant(self):
        self.__cant-=1
    def insertar(self, x):
        nodo = Celda(x,None)  # Crea un nuevo nodo
        if self.vacia():
            self.cargar_pr(nodo)  # Si la cola estaba vacía, el nuevo nodo es también el primero
        else:
            self.obtener_ul().cargar_sig(nodo)  # Conecta el último nodo actual con el nuevo nodo
        self.cargar_ul(nodo)  # Actualiza el puntero al último nodo
        self.aumentar_cant() # Incrementa la cantidad de elementos en la cola

    def suprimir(self):
        if self.vacia():
            print("Cola vacía")
        else:
            self.cargar_pr(self.obtener_pr().obtener_sig()) # Actualiza el puntero al primer nodo
            self.disminuir_cant()# Decrementa la cantidad de elementos en la cola
            if self.vacia():
                self.cargar_ul(None)# Si la cola queda vacía, ul debe ser None también
            
    def mostrar(self,aux):
        if aux is not None:
            print(aux.obtener_item())  # Imprime el valor del nodo actual
            self.mostrar(aux.obtener_sig())  # Llama recursivamente a la función para el siguiente nodo
cola_enc = Cola(3)
cola_enc.insertar(1)
cola_enc.insertar(2)
cola_enc.insertar(3)
cola_enc.suprimir()
cola_enc.mostrar(cola_enc.obtener_pr())