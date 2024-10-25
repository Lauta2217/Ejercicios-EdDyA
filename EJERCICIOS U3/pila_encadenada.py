class Celda:
    def __init__(self,item, sig):
        self.__item = item
        self.__sig = sig
    def obtener_item(self):
        return self.__item
    def cargar_item(self,itemm):
        self.__item = itemm
    def cargar_sig(self,tope):
        self.__sig = tope
    def obtener_sig(self):
        return self.__sig
class Pila_enc:
    def __init__(self,tope=None,cant=0):
        self.__cant = cant
        self.__tope = tope
    def vacia(self):
        return self.__cant == 0
    def obtener_tope(self):
        return self.__tope
    def cargar_tope(self,dato):
        self.__tope = dato
    def obtener_cant(self):
        return self.__cant
    def aumentar_cant(self):
        self.__cant+=1
    def disminuir_cant(self):
        self.__cant-=1
    
    def insertar(self,x):
        nueva_celda = Celda(x,self.obtener_tope())
        self.cargar_tope(nueva_celda)
        self.aumentar_cant()
            
    def suprimir(self):
        if self.vacia():
            return None
        else:
            self.cargar_tope(self.obtener_tope().obtener_sig()) 
            self.disminuir_cant()
    def mostrar(self,aux):
        if aux is not None:
            print(aux.obtener_item())
            self.mostrar(aux.obtener_sig())
        else:
            return
pila_enc = Pila_enc()
pila_enc.insertar(1)
pila_enc.insertar(2)
pila_enc.insertar(3)
pila_enc.suprimir()
pila_enc.mostrar(pila_enc.obtener_tope())
