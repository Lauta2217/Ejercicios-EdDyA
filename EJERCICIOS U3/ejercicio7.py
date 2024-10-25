from cola_encadenadapara7 import Cola
import time
import random
tiempo_espera_atendidos = 0
cant_atendidos = 0
cant_NOatendidos = 0
tiempo_espera_Noatendidos = 0
tiempo_simulacion = 20
num_cliente = 0
max_espera = 0

class Cliente:
    def __init__(self,idd):
        self.tiempo_espera = 0
        self.idd = idd
        self.atendido = False
    def atendido(self):
        self.atendido = True
    def aumentar_tiempo_espera(self):
        self.tiempo_espera+=1
                
def asignar_cajero(cliente,cajeros):
    numeros = [0,1,2]
    if cajeros[0].vacia() and cajeros[1].vacia() and cajeros[2].vacia():
        #print("Eligiendo random")
        cajeros[random.choice(numeros)].insertar(cliente)
    elif not cajeros[0].vacia() and not cajeros[1].vacia() and not cajeros[2].vacia():
        #print("Eligiendo menor")
        cantidad = [cajeros[0].obtener_cant(),cajeros[1].obtener_cant(),cajeros[2].obtener_cant()]
        if cantidad[0] == cantidad[1] == cantidad[2]:
            #print(f"todos iguales elijo random {random.choice(numeros)}")
            cajeros[random.choice(numeros)].insertar(cliente)
        else:
            cajeros[cantidad.index(min(cantidad))].insertar(cliente)
    else:
        # Si hay cajeros disponibles (pero no todos están ocupados)
        for i in range(3):
            if cajeros[i].vacia():
                cajeros[i].insertar(cliente)
            
def aumentar_espera(aux):
    if aux is not None:
        aux.obtener_item().aumentar_tiempo_espera()
        #print(f"Para el cliente { aux.obtener_item().idd} la espera es de: { aux.obtener_item().tiempo_espera}\n")
        aumentar_espera(aux.obtener_sig())
        
def atender(cajero,i):
    global cant_atendidos,tiempo_espera_atendidos
    tiempos = [5,3,4]
    if cajero.vacia():
        return
    primero = cajero.obtener_pr()
    aumentar_espera(primero.obtener_sig())
    if cajero.tiempo > 0:
        cajero.tiempo-=1
    else:
        tiempo_espera_atendidos+= primero.obtener_item().tiempo_espera
        print(f"cliente{primero.obtener_item().idd} atendido\n")
        cajero.suprimir()
        cajero.tiempo = tiempos[i]
        cant_atendidos+=1
    time.sleep(0.5)
    
def contar(aux):
    global tiempo_espera_Noatendidos, max_espera
    if aux is not None:
        if max_espera < aux.obtener_item().tiempo_espera:
            max_espera = aux.obtener_item().tiempo_espera
        tiempo_espera_Noatendidos+= aux.obtener_item().tiempo_espera
        contar(aux.obtener_sig())
    else:
        return
def banco(Cajeros):
    global tiempo_simulacion, num_cliente,cant_NOatendidos
    tiempo_actual = 0
    while tiempo_simulacion > tiempo_actual:
        if tiempo_actual % 2 == 0:
            try:
                cliente1 = Cliente(num_cliente+1)
                cliente2 = Cliente(num_cliente+2)
                num_cliente +=2
            except:
                print("Algo pasó")
            else:
                print("\nTodo salio bien pa\n")
            asignar_cajero(cliente1,Cajeros)
            asignar_cajero(cliente2,Cajeros)
            #asignar_cajero(cliente3,Cajeros)
        for i in range(3):
            atender(Cajeros[i],i)
        tiempo_actual+=1
        time.sleep(1.5)
    for i in range(3):
        primero = Cajeros[i].obtener_pr()
        cant_NOatendidos += Cajeros[i].obtener_cant()
        contar(primero)
def informar():
    global tiempo_espera_atendidos, cant_atendidos, cant_NOatendidos, tiempo_espera_Noatendidos,num_cliente 
    print(f"""Tiempo de espera maximo de los clientes en la cola: {max_espera}\n
              Cantidad de clientes atendidos: {cant_atendidos}\n
              Cantidad de clientes sin atender: {cant_NOatendidos}\n
              Promedio de espera de los clientes atendidos: {round(tiempo_espera_atendidos/cant_atendidos):.2f}\n
              Promedio de espera de los clientes  que no fueron atendidos: {round(tiempo_espera_Noatendidos/cant_NOatendidos):.2f}\n
              cantida de clientes:{num_cliente}
          """)
if __name__=='__main__':
    Cajero_1 = Cola(5)
    Cajero_2 = Cola(3)
    Cajero_3 = Cola(4)
    Cajeros = [Cajero_1,Cajero_2,Cajero_3]
    banco(Cajeros)
    informar()