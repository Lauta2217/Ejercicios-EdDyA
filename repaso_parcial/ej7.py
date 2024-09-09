from cola_encadenada import Cola
import random
class Cliente:
    def __init__(self):
        self.__tiempo_espera = 0
    def aumentar_espera(self,dato):
        self.__tiempo_espera+=dato
    def obtener_tiempo_espera(self):
        return self.__tiempo_espera
class Banco:
    def __init__(self,C1,C2,C3,tiempo_simulacion):
        self.__cajeros = [C1,C2,C3]
        self.__tiempo_simulacion = tiempo_simulacion
        self.__cant_clientes_atendidos = 0
        self.__cant_clientes_noatendidos = 0
        self.__espera_clientes_atendidos = 0
        self.__espera_clientes_noatendidos = 0
        self.__max_espera = []
    def obtener_cajeros(self):
        return self.__cajeros
    def obtener_tiempo_simulacion(self):
        return self.__tiempo_simulacion
    def agregar_tiempo(self,dato):
        self.__max_espera.append(dato)
        
    def aumentar_cant_clientes_atendidos(self):
        self.__cant_clientes_atendidos+=1
    def obtener_cant_clientes_atendidos(self):
        return self.__cant_clientes_atendidos
    def aumentar_espera_clientes_atendidos(self,dato):
        self.__espera_clientes_atendidos+=dato
    def obtener_tiempo_espera_atendidos(self):
        return self.__espera_clientes_atendidos
    
    def aumentar_cant_clientes_noatendidos(self,dato):
        self.__cant_clientes_noatendidos+=dato
    def obtener_cant_clientes_noatendidos(self):
        return self.__cant_clientes_noatendidos
    def aumentar_espera_clientes_noatendidos(self,dato):
        self.__espera_clientes_noatendidos+=dato
    def obtener_tiempo_espera_noatendidos(self):
        return self.__espera_clientes_noatendidos
    def obtener_max(self):
        return self.__max_espera
        
    def asignar_cajero(self,cliente):
        if self.__cajeros[0].obtener_cant() == self.__cajeros[1].obtener_cant() == self.__cajeros[2].obtener_cant():
            cajero = random.choice(self.__cajeros)
            cajero.insertar(cliente)
        else:
            cantidad = [self.__cajeros[0].obtener_cant(),self.__cajeros[1].obtener_cant(),self.__cajeros[2].obtener_cant()]
            self.__cajeros[cantidad.index(min(cantidad))].insertar(cliente)
    def eliminar_cliente(self,index):
        self.aumentar_espera_clientes_atendidos(self.obtener_cajeros()[index].obtener_pr().obtener_item().obtener_tiempo_espera())
        self.obtener_cajeros()[index].suprimir()
        print(f"SE ELIMINÓ UN CLIENTE DEL CAJERO {index+1}\n")
        self.aumentar_cant_clientes_atendidos()
    def atender(self):
        t = 0
        while(t < self.obtener_tiempo_simulacion()):
            if t % 2 == 0:
                cliente = Cliente()
                self.asignar_cajero(cliente)
            
            for i in range(5):
                if i % 2 == 0:
                    cliente = Cliente()
                    self.asignar_cajero(cliente)
                if i == 4:
                    self.eliminar_cliente(0)
                elif i == 2:
                    self.eliminar_cliente(1)
                elif i == 3:
                    self.eliminar_cliente(2)
            t+=5
            for cajero in self.obtener_cajeros():
                if not cajero.vacia():
                    aux = cajero.obtener_pr()
                    while aux is not None:
                        aux.obtener_item().aumentar_espera(5)
                        aux = aux.obtener_sig()
                        
        for cajero in self.obtener_cajeros():
            if not cajero.vacia():
                aux = cajero.obtener_pr()
                self.aumentar_cant_clientes_noatendidos(cajero.obtener_cant())
                while aux is not None:
                    self.obtener_max().append(aux.obtener_item().obtener_tiempo_espera())
                    self.aumentar_espera_clientes_noatendidos(aux.obtener_item().obtener_tiempo_espera())
                    aux = aux.obtener_sig()
        self.mostrar()
    def mostrar(self):
        print(f"El tiempo máximo de espera de los clientes en la cola es de: {max(self.obtener_max())} ")
        print(f"Cantidad de clientes atendidos: {self.obtener_cant_clientes_atendidos()}")
        print(f"Cantidad de clientes que quedaron sin atender: {self.obtener_cant_clientes_noatendidos()}")
        if self.obtener_cant_clientes_atendidos() > 0:
            print(f"Promedio de espera de los atendidos: {(self.obtener_tiempo_espera_atendidos()/self.obtener_cant_clientes_atendidos()):.2f}")
        else:
            print("No hay clientes atendidos\n")
        if self.obtener_cant_clientes_noatendidos() > 0:
            print(f"Promedio de espera de los que quedaron sin atender: {(self.obtener_tiempo_espera_noatendidos()/self.obtener_cant_clientes_noatendidos()):.2f}")
        else:
            print("No hay clientes noatendidos\n")

if __name__ == '__main__':
    C1 = Cola()
    C2 = Cola()
    C3 = Cola()
    banco = Banco(C1,C2,C3,10)
    banco.atender()