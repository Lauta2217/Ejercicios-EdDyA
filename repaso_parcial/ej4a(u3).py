from lista_encadenada import ListaEncadenada
class Celda:
    def __init__(self,valor,fila,columna):
        self.__valor = valor
        self.__fila = fila
        self.__columna = columna
    def obtener_valor(self):
        return self.__valor
    def obtener_fila(self):
        return self.__fila
    def obtener_columna(self):
        return self.__columna
    
def suma(M1,M2):
    Matriz_3 = ListaEncadenada()
    cabeza1 = M1.obtener_cabeza()
    cabeza2 = M2.obtener_cabeza()
    pos = 1
    while(cabeza1 is not None or cabeza2 is not None):
        if ((cabeza1.obtener_dato().obtener_fila(),cabeza1.obtener_dato().obtener_columna()) < (cabeza2.obtener_dato().obtener_fila(),cabeza2.obtener_dato().obtener_columna())):
            celda = Celda(valor = cabeza1.obtener_dato().obtener_valor(),fila=cabeza1.obtener_dato().obtener_fila(), columna = cabeza1.obtener_dato().obtener_columna())
            Matriz_3.insertar(celda,pos)    
            pos+=1
            cabeza1 = cabeza1.obtener_siguiente()    
        elif ((cabeza1.obtener_dato().obtener_fila(),cabeza1.obtener_dato().obtener_columna()) > (cabeza2.obtener_dato().obtener_fila(),cabeza2.obtener_dato().obtener_columna())):
            celda = Celda(valor = cabeza2.obtener_dato().obtener_valor(),fila=cabeza2.obtener_dato().obtener_fila(), columna = cabeza2.obtener_dato().obtener_columna())
            Matriz_3.insertar(celda,pos)
            pos+=1
            cabeza2 = cabeza2.obtener_siguiente()
    
        else:
            celda = Celda(valor = cabeza1.obtener_dato().obtener_valor() + cabeza2.obtener_dato().obtener_valor(),fila=cabeza1.obtener_dato().obtener_fila(), columna = cabeza1.obtener_dato().obtener_columna())
            Matriz_3.insertar(celda,pos)
            pos+=1    
            cabeza1 = cabeza1.obtener_siguiente()
            cabeza2 = cabeza2.obtener_siguiente()
    aux = Matriz_3.obtener_cabeza()
    while aux is not None:
        print(f"Fila:{aux.obtener_dato().obtener_fila()} Columna: {aux.obtener_dato().obtener_columna()} valor: {aux.obtener_dato().obtener_valor()}\n")
        aux = aux.obtener_siguiente()
if __name__ =='__main__':
    Celda1 = Celda(1,1,1)
    Celda2 = Celda(1,1,2)
    Celda3 = Celda(1,2,1)
    Celda4 = Celda(1,2,2)
    Matriz_1 = ListaEncadenada()
    Matriz_2 = ListaEncadenada()
    
    Matriz_1.insertar(Celda1,1)
    Matriz_1.insertar(Celda2,1)
    Matriz_1.insertar(Celda3,3)
    Matriz_1.insertar(Celda4,4)
    
    Matriz_2.insertar(Celda1,1)
    Matriz_2.insertar(Celda2,1)
    Matriz_2.insertar(Celda3,2)
    Matriz_2.insertar(Celda4,3)
    suma(Matriz_1,Matriz_2)