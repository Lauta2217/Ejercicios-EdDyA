from cola_encadenadapara7 import Cola
import random

class Cliente:
    def __init__(self,idd):
        self.tiempo_espera = 0
        self.idd = idd
        self.atendido = False
    def atendido(self):
        self.atendido = True
    def aumentar_tiempo_espera(self):
        self.tiempo_espera+=1
        
class Banco:
    def __init__(self, tiempo_simulacion):
        self.tiempo_simulacion = tiempo_simulacion
        self.num_cliente = 1
        self.cant_atendidos = 0
        self.cant_NOatendidos = 0
        self.tiempo_espera_atendidos = 0
        self.tiempo_espera_Noatendidos = 0
        self.max_espera = 0
        self.cajeros = [Cola(5), Cola(3), Cola(4)]
        
    def asignar_cajero(self,cliente):
        numeros = [0,1,2]
        if self.cajeros[0].vacia() and self.cajeros[1].vacia() and self.cajeros[2].vacia():
            #print("Eligiendo random")
            self.cajeros[random.choice(numeros)].insertar(cliente)
        elif not self.cajeros[0].vacia() and not self.cajeros[1].vacia() and not self.cajeros[2].vacia():
            #print("Eligiendo menor")
            cantidad = [self.cajeros[0].obtener_cant(),self.cajeros[1].obtener_cant(),self.cajeros[2].obtener_cant()]
            if cantidad[0] == cantidad[1] == cantidad[2]:
                #print(f"todos iguales elijo random {random.choice(numeros)}")
                self.cajeros[random.choice(numeros)].insertar(cliente)
            else:
                self.cajeros[cantidad.index(min(cantidad))].insertar(cliente)
        else:
            # Si hay cajeros disponibles (pero no todos están ocupados)
            for i in range(3):
                if self.cajeros[i].vacia():
                    self.cajeros[i].insertar(cliente)
                
    def aumentar_espera(self,aux):
        if aux is not None:
            aux.obtener_item().aumentar_tiempo_espera()
            #print(f"Para el cliente { aux.obtener_item().idd} la espera es de: { aux.obtener_item().tiempo_espera}\n")
            self.aumentar_espera(aux.obtener_sig())
            
    def atender(self,cajero,i):
        tiempos = [5,3,4]
        if cajero.vacia():
            return
        primero = cajero.obtener_pr()
        self.aumentar_espera(primero.obtener_sig())
        if cajero.tiempo > 0:
            cajero.tiempo-=1
        else:
            self.tiempo_espera_atendidos+= primero.obtener_item().tiempo_espera
            print(f"cliente{primero.obtener_item().idd} atendido\n")
            cajero.suprimir()
            cajero.tiempo = tiempos[i]
            self.cant_atendidos+=1
        
    def contar(self,aux):
        if aux is not None:
            cliente = aux.obtener_item()
            if not cliente.atendido:
                self.cant_NOatendidos += 1
                self.tiempo_espera_Noatendidos += cliente.tiempo_espera
                self.max_espera = max(self.max_espera, cliente.tiempo_espera)
            self.contar(aux.obtener_sig())
        else:
            return
    def simulacion_banco(self):
        tiempo_actual = 0
        while self.tiempo_simulacion > tiempo_actual:
            if tiempo_actual % 2 == 0:
                try:
                    cliente1 = Cliente(self.num_cliente)
                    self.num_cliente +=1
                    cliente2 = Cliente(self.num_cliente)
                    self.num_cliente +=1
                    
                except:
                    print("Algo pasó")
                else:
                    print("\nTodo salio bien pa\n")
                    self.asignar_cajero(cliente1)
                    self.asignar_cajero(cliente2)
            for i in range(3):
                self.atender(self.cajeros[i],i)
            tiempo_actual+=1
        for i in range(3):
            primero = self.cajeros[i].obtener_pr()
            self.contar(primero)
    def informar(self):
        print(f"""Tiempo de espera maximo de los clientes en la cola: {self.max_espera}\n
                Cantidad de clientes atendidos: {self.cant_atendidos}\n
                Cantidad de clientes sin atender: {self.cant_NOatendidos}\n
                Promedio de espera de los clientes atendidos: {round(self.tiempo_espera_atendidos/self.cant_atendidos):.2f}\n
                Promedio de espera de los clientes que no fueron atendidos: {round(self.tiempo_espera_Noatendidos/self.cant_NOatendidos):.2f}\n
                cantida de clientes:{self.num_cliente}
            """)
if __name__=='__main__':
    banco = Banco(19)
    banco.simulacion_banco()
    banco.informar()