class Celda:
    def __init__(self, item=0, sig=None):
        self.item = item  # Almacena el valor del nodo
        self.sig = sig  # Almacena la referencia al siguiente nodo (inicialmente None)

    def obtener_item(self):
        return self.item  # Devuelve el valor almacenado en el nodo

    def cargar_item(self, xitem):
        self.item = xitem  # Asigna un valor al nodo

    def cargar_sig(self, xtope):
        self.sig = xtope  # Asigna el siguiente nodo en la lista enlazada

    def obtener_sig(self):
        return self.sig  # Devuelve el siguiente nodo en la lista enlazada
class Cola:
    def __init__(self,tiempo, pr=None, ul=None, cant=0):
        self.pr = pr  # Puntero al primer nodo de la cola
        self.ul = ul  # Puntero al último nodo de la cola
        self.cant = cant  # Número de elementos en la cola
        self.tiempo = tiempo

    def vacia(self):
        return self.cant == 0  # Devuelve True si la cola está vacía

    def insertar(self, x):
        ps1 = Celda()  # Crea un nuevo nodo
        ps1.cargar_item(x)  # Asigna el valor al nuevo nodo
        ps1.cargar_sig(None)  # El nuevo nodo será el último, así que su siguiente es None
        
        if self.ul is None:
            self.pr = ps1  # Si la cola estaba vacía, el nuevo nodo es también el primero
        else:
            self.ul.cargar_sig(ps1)  # Conecta el último nodo actual con el nuevo nodo
        
        self.ul = ps1  # Actualiza el puntero al último nodo
        self.cant += 1  # Incrementa la cantidad de elementos en la cola
        return self.ul.obtener_item()  # Devuelve el valor del nodo insertado

    def suprimir(self):
        if self.vacia():
            print("Cola vacía")
            return 0
        else:
            aux = self.pr  # Almacena el nodo que va a ser eliminado
            x = self.pr.obtener_item()  # Obtiene el valor del primer nodo
            self.pr = self.pr.obtener_sig()  # Actualiza el puntero al primer nodo
            self.cant -= 1  # Decrementa la cantidad de elementos en la cola
            
            if self.cant == 0:
                self.ul = None  # Si la cola queda vacía, ul debe ser None también
            
            return x  # Devuelve el valor eliminado
    def obtener_pr(self):
        return self.pr
    
    def obtener_cant(self):
        return self.cant

    def recorrer(self,aux):
        if aux is not None:
            print(aux.obtener_item())  # Imprime el valor del nodo actual
            self.recorrer(aux.obtener_sig())  # Llama recursivamente a la función para el siguiente nodo
