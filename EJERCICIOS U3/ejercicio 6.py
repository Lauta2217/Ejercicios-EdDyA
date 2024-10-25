from cola_encadenada import Cola
import time
class Trabajo:
    def __init__(self,tiempo_res,idd,tiempo_es = 0):
        self.tiempo_restante = tiempo_res
        self.tiempo_espera = tiempo_es
        self.impreso = False
        self.idd = idd
    def __str__(self):
        return f"Tiempo restante:{self.tiempo_restante}"
    def obtener_restante(self):
        return self.tiempo_restante
    def reducir_tiempo_restante(self,i):
        self.tiempo_restante-=i
        time.sleep(1)
    def aumentar_tiempo_espera(self,i):
        self.tiempo_espera+=i
    def obtener_espera(self):
        return self.tiempo_espera
def aumentar_espera(aux):
    if aux is not None:
        print(f"Para el trabajo{aux.obtener_item().idd} aumento la espera")
        aux.obtener_item().tiempo_espera+=1
        aumentar_espera(aux.obtener_sig())
    else:
        return
def impresion(Impresora):
    tiempo_espera_total  = 0
    cant = 0
    Trabajo = Impresora.obtener_pr()
    band = False
    band2 = False
    while not Impresora.vacia() and not band2:
        for i in range(5):
            aux = Trabajo
            if Trabajo.obtener_item().tiempo_restante == 0:
                if Trabajo.obtener_sig() != None:
                    Trabajo.obtener_sig().obtener_item().reducir_tiempo_restante(1)
                    print(f"Imprimiendo el trabajo {Trabajo.obtener_sig().obtener_item().idd}")
                    if aux.obtener_sig() != None:
                        if aux.obtener_sig().obtener_item().tiempo_restante != 0:
                            aux = aux.obtener_sig()
                            aumentar_espera(aux)
                else:
                    break
            else:
                Trabajo.obtener_item().reducir_tiempo_restante(1)
                print(f"Imprimiendo el trabajo {Trabajo.obtener_item().idd}")
                if aux.obtener_sig() != None:
                    if aux.obtener_sig().obtener_item().tiempo_restante != 0:
                        aux = aux.obtener_sig()
                        aumentar_espera(aux)
            band = True
        time.sleep(5)
     
        
            
        if Trabajo.obtener_item().tiempo_restante == 0:
            print("Es 0 el tiempo")
            cant+=1
            print(f"Para el trabajo {Trabajo.obtener_item().idd} el tiempo de espera fue de: {Trabajo.obtener_item().tiempo_espera}")
            tiempo_espera_total += Trabajo.obtener_item().tiempo_espera
            if Trabajo.obtener_sig() != None:
                Trabajo = Trabajo.obtener_sig()
            else:
                band2 = True
            Impresora.suprimir()
            aux = Impresora.obtener_pr()            
        elif Trabajo.obtener_item().tiempo_restante != 0 and band:
            Trabajo2 = Trabajo.obtener_item()
            Impresora.insertar(Trabajo2)
            Trabajo = Trabajo.obtener_sig()
    print(f"Cantida de trabajos hechos:{cant} tiempo de espera promedio{tiempo_espera_total/cant}")
if __name__== '__main__':
    Impresora = Cola()
    tra1 = Trabajo(tiempo_res = 4,idd = 1)
    tra2 = Trabajo(tiempo_res = 8, idd = 2)
    Impresora.insertar(tra1)
    Impresora.insertar(tra2)
    Impresora.recorrer(aux = Impresora.obtener_pr())
    impresion(Impresora)