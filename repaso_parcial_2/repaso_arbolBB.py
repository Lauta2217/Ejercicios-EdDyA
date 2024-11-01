class Nodo:
    __valor:int
    __izquierda:object
    __derecha: object
    def __init__(self,valor,sig = None):
        self.__valor = valor
        self.__izquierda = None
        self.__derecha = None
    def get_value(self):
        return self.__valor
    def get_left(self):
        return self.__izquierda
    def get_right(self):
        return self.__derecha
    def set_left(self,izq):
        self.__izquierda = izq
    def set_right(self,derc):
        self.__derecha = derc
    def set_value(self,value):
        self.__valor = value
    def grau(self):
        if self.__izquierda is not None and self.__derecha is not None:
            return 2
        elif self.__izquierda is None and self.__derecha is None:
            return 0
        else:
            return 1

class Arbol_binario_busqueda:
    __raiz: object
    def __init__(self):
        self.__raiz = None
    def get_raiz(self):
        return self.__raiz
        
    def insertar(self,valor,actual):
        nodo = Nodo(valor) #creo el nodo con el valor ingresado
        if self.__raiz == None: # si no hay raiz 
            self.__raiz = nodo #se define como raiz el valor ingresado
            return # me vuelvo
        else:
            if actual.get_value() > valor: #si el valor del actual es mayor que el valor que quiero ingresar
                if actual.get_left() is None: #y si a la izquierda no tiene nada
                    actual.set_left(nodo) #entonces inserto ese valor a su izquierda ya que es mas pequeño
                    return # me vuelvo
                else:
                    self.insertar(valor,actual.get_left()) #si tiene algo a la izquierda entonces vuelvo a iterar, pero con ese valor que tiene a la izquierda
            elif actual.get_value() < valor: #si el valor del actual es menor que el valor que quiero ingresar
                if actual.get_right() is None: #y si a la derecha no tiene nada
                    actual.set_right(nodo) #entonces inserto ese valor a su derecha ya que es mas grande
                    return # me vuelvo
                else:
                    self.insertar(valor,actual.get_right()) #si tiene algo a la derecha entonces vuelvo a iterar, pero con ese valor que tiene a la derecha
    def eliminar(self, valor, actual):
        if actual is None: #si no hay actual
            return actual #entonces lo retorno (es lo mismo que poner return None)
        # Buscar el nodo a eliminar
        if valor < actual.get_value():  #si el valor del actual es mayor que el valor que quiero eliminar
            actual.set_left(self.eliminar(valor, actual.get_left())) # a la izquierda va a quedar lo que me retorne la funcion
        elif valor > actual.get_value(): #si el valor del actual es mayor que el valor que quiero eliminar
            actual.set_right(self.eliminar(valor, actual.get_right())) # a la derecha va a quedar lo que me retorne la funcion
        else:
            # Caso 1: Nodo sin hijos
            if actual.get_left() is None and actual.get_right() is None: #si no tiene hijos tonce lo cambio a none al nodo a eliminar
                return None
            # Caso 2: Nodo con un solo hijo
            elif actual.get_left() is None: #si no tiene un valor a su izquierda entonces retorno el de la derecha
                return actual.get_right()
            elif actual.get_right() is None: #si no tiene un valor a su derecga entonces retorno el de la izquierda
                return actual.get_left()
            # Caso 3: Nodo con dos hijos
            else: #si no tiene ni un valor a la izquierda ni un valor a la derecha
                sucesor_inorden = self.min_valor_nodo(actual.get_right()) # Busco el padre del nodo mas pequeño en el subárbol derecho
                actual.set_value(sucesor_inorden.get_left().get_value()) # Reemplazo el valor del nodo actual con el valor del sucesor
                sucesor_inorden.set_left(sucesor_inorden.get_left().get_right()) # como subi un nodo del arbol para reemplazar el eliminado entonces no puedo perder lo que tenia hacia abajo el nodo que sirve de reemplazo, por eso es este enganche
        return actual #Retorno el nodo eliminado
    def min_valor_nodo(self, nodo):
        while nodo.get_left().get_left() is not None:# Bajar por la izquierda hasta encontrar el nodo anterior al nodo más pequeño
            nodo = nodo.get_left()
        return nodo #lo retorno
    def buscar(self,valor,actual):
        if actual is not None: #si actual es none entonces no lo encontré
            if actual.get_value() == valor: # si el valor del actual es el que estoy buscando retorno
                band = True #retorno true
            elif actual.get_value() > valor: #si el valor del actual es mayor al que estoy buscando me muevo la izquierda
                    band = self.buscar(valor,actual.get_left()) # bandera va a recibir ya sea un false o un true de las llamadas recursivas desde la izquierda
            else: #si el valor del actual es menor al que estoy buscando me muevo la izquierda
                    band = self.buscar(valor,actual.get_right())# bandera va a recibir ya sea un false o un true de las llamadas recursivas desde la derecha
        else:
            band = False # retorno false

        return band  # retorno ya sea true o false
    def nivel(self,valor,actual,nivel = 0): #nivel del arbol tenemos un parametro nivel que ayuda en cada recursion a determianr el nivel del nodo
        if actual is not None: #si actual es none, entonces no encontré el valor
            if actual.get_value() == valor: #si actual es el valor que estoy buscando entonces printeo su nivel
                print(f"{valor} tiene nivel: {nivel}\n")
            elif actual.get_value() > valor:#si el valor del actual es mayor al que estoy buscando me muevo la izquierda
                    self.nivel(valor,actual.get_left(),nivel+1) #me voy para la izquierda y aumento el nivel
            else:#si el valor del actual es menor al que estoy buscando me muevo la izquierda
                    self.nivel(valor,actual.get_right(),nivel+1)  #me voy para la derecha y aumento el nivel
        else:
            return #Retorno
                
    def hoja(self,valor,actual):
        if actual is not None: #si actual es none, entonces no encontré el valor
            if actual.get_value() == valor:  #si actual es el valor que estoy buscando entonces evaluo
                if actual.get_left() is None and actual.get_right() is None:   #si no tiene nada la izq y nada a la der entonces es hoja
                    band = True #retorno true
                else: #si tiene al menos un hijo
                    band = False #retorno false
            elif actual.get_value() > valor: #si el valor del actual es mayor al que estoy buscando me muevo la izquierda
                band = self.hoja(valor,actual.get_left()) #me voy para la izquierda y recibo el valor de la recursion 
            else:#si el valor del actual es menor al que estoy buscando me muevo la izquierda
                band = self.hoja(valor,actual.get_right()) #me voy para la derecha y recibo el valor de la recursion 
        else:
            band = False
        return band #retorno band
    
    def hijo(self,hijo,supuesto_padre,actual):
        band = False
        if actual is not None: #si actual es none, entonces no encontré el valor
            if supuesto_padre == actual.get_value(): #si el actual es el supuesto padre 
                print("viendo si tiene pendejos")
                if actual.get_left() is not None: #si a la izquierda tiene algo evaluo
                    if actual.get_left().get_value() == hijo: #si lo que tiene a la izquierda es el hijo que estamos buscando
                        band = True #band true #band true
                elif actual.get_right() is not None: #sino si a la derecha tiene algo evaluo
                    if actual.get_right().get_value() == hijo: #si lo que tiene a la derecha es el hijo que estamos buscando
                        band = True #band true      #si nada de eso pasa se retorna
            elif actual.get_value() > supuesto_padre: #si el valor del actual es mayor al valor del padre que estoy buscando me muevo la izquierda
                self.hijo(hijo,supuesto_padre,actual.get_left()) #me voy para la izquierda 
            else: #si el valor del actual es menor al valor del padre que estoy buscando me muevo la derecha
                self.hijo(hijo,supuesto_padre,actual.get_right())  #me voy para la izquierda 
        else:
            band = False
        return band #retorno band
    def camino(self,inicio,fin,actual,band = False,camino = []): #se puede usar la funcion buscar, pero en el parcial hay que definirla tambien
        if actual is not None: #si actual es none, entonces no encontré el valor
            if actual.get_value() == inicio or band: #si actual es el valor de inicio del camino o la bandera que me permite manejar la condicion de que ya tengo el inicio es true entonces entro
                band = True #si solo ingresé por que el actual es igual al inicio entonces cambio la bandera para despues
                camino.append(actual.get_value())  #inicio el camino con el actual    
                if actual.get_value() == fin: #si el actual es igual al fin entonces retorno nomas
                    return
                elif actual.get_value()>fin: #si el valor del actual es mayor al valor del fin que estoy buscando me muevo la izquierda
                    self.camino(inicio,fin,actual.get_left(),band,camino) #recursion para la izquierda, pero ya le agrego los parametros bandera y camino para no perderlos
                else:#si el valor del actual es menor al valor del fin que estoy buscando me muevo la derecha
                    self.camino(inicio,fin,actual.get_right(),band,camino) #recursion para la derecha, pero ya le agrego los parametros bandera y camino para no perderlos
            elif actual.get_value()>inicio: #si el valor del actual es mayor al inicio al valor del padre que estoy buscando me muevo la izquierda
                self.camino(inicio,fin,actual.get_left())
            else: #si el valor del actual es menor al inicio al valor del padre que estoy buscando me muevo la derecha
                self.camino(inicio,fin,actual.get_right())
        else:
            return None #retorno None
        if fin in camino: #si esta el fin en el camino tonce lo encontró
             print(camino)
        else: #no hay camino
            print("No existe")
        
    def altura(self,actual):
        if actual is not  None: #si actual es none retorno 0
            altura = 1 + max(self.altura(actual.get_left()),self.altura(actual.get_right())) #la altura es 1 + la maxima altura entre la izquierda y derecha
        else:
            altura = 0
        return altura #la retorno
    
    def padre_y_hermano(self,valor,actual):
        if actual is not  None: #si el actual es none retorno none
            if actual.get_left().get_value() == valor or actual.get_right().get_value() == valor: #si el valor que tiene a la izquierda el actual es el valor que estoy buscando o lo mismo pero a la derecha entonces encontré al padre
                if actual.get_left().get_value() != valor: #si el valor del padre a la izquierda es distinto al ingresado tonce a la derecha  tiene hermano o no
                    print(f"Padre de {valor}: {actual.get_value()} y su hermano es: {actual.get_left().get_value() }")
                else: #si el valor del padre a la derecha es distinto al ingresado tonce a la izquierda tiene hermano o no
                    print(f"Padre de {valor}: {actual.get_value()} y su hermano es: {actual.get_right().get_value() }")
            elif actual.get_value() > valor: #si el valor del actual es mayor al ingresado tonce nos vamos a la izquierda
                self.padre_y_hermano(valor,actual.get_left()) # y nos fuimos a la izquierda
            else: #si el valor del actual es mayor al ingresado tonce nos vamos a la derecha
                self.padre_y_hermano(valor,actual.get_right()) # y nos fuimos a la derecha
        else:
            return None
             
    def cantidad_nodos(self,actual): #se puede hacer con inorden
        if actual is None: #si actual es none tonce retornamos 0
            cant = 0
        else:
            cant =  1 + self.cantidad_nodos(actual.get_left()) + self.cantidad_nodos(actual.get_right()) #la cantida de nodos es 1(actual) + la cantidad de nodos para la izquierda del actual + la cantidad de nodos para la derecha del actual
        return cant #retorno cant
    
    def sucesores(self,valor,actual):
        if actual is not None: #si actual es none tonce retorno none
            if actual.get_value() == valor: #si el valor del actual es el que busco
                self.inorden(actual.get_left()) # funcion que printea nodos a la derecha e izquierda del nodo ingresado por ello le mando la izquierda del que quiero
                self.inorden(actual.get_right())# funcion que printea nodos a la derecha e izquierda del nodo ingresado por ello le mando la derecha del que quiero
            elif actual.get_value() > valor: #si el actual es mayor tonce me voy la izquierda
                self.sucesores(valor,actual.get_left()) # y nos fuimos a la izquierda
            else: #si el actual es menor tonce me voy la derecha
                self.sucesores(valor,actual.get_right()) # y nos fuimos a la derecha
        else:
            return None
    def grado(self,valor,actual):
        if actual is not None:
            if actual.get_value() == valor:
                print(f"grado del valor {valor}: {actual.grau()}")
            elif actual.get_value() > valor:
                self.grado(valor,actual.get_left())
            else:
                self.grado(valor,actual.get_right())
        return
    def cont_sucesores(self,valor,actual):
        if actual is not None:
            if actual.get_value() == valor:
               print(f"cantidad de sucesores de {valor}: {self.cantidad_nodos(actual)-1}")
            elif actual.get_value() > valor:
                self.cont_sucesores(valor,actual.get_left())
            else:
                self.cont_sucesores(valor,actual.get_right())

     # Recorrido In-orden
    def inorden(self, nodo_actual): #se ocupa en todo
        if nodo_actual is not None: #si actual no es none tonce muestro
            self.inorden(nodo_actual.get_left()) #nodos a su izquierda
            print(nodo_actual.get_value(),end=" ") # los printeo
            self.inorden(nodo_actual.get_right()) # nodos a su derecha
            
    def preorden(self, nodo_actual):
        if nodo_actual is not None: #si actual no es none tonce muestro
            print(nodo_actual.get_value(), end=" ") # los printeo
            self.preorden(nodo_actual.get_left()) #nodos a su izquierda
            self.preorden(nodo_actual.get_right()) # nodos a su derecha
    # Recorrido Post-orden
    def postorden(self, nodo_actual):
        if nodo_actual is not None: #si actual no es none tonce muestro
            self.postorden(nodo_actual.get_left()) #nodos a su izquierda
            self.postorden(nodo_actual.get_right()) # nodos a su derecha
            print(nodo_actual.get_value(), end=" ") # los printeo
if __name__ == '__main__':
    arbol = Arbol_binario_busqueda()
    valores = [50,30,70,20,40,60,80,10,5,4,3]
    for valor in valores:
        arbol.insertar(valor,arbol.get_raiz())
    print(f"""
          buscar:
          80:{arbol.buscar(80,arbol.get_raiz())}
          230:{arbol.buscar(230,arbol.get_raiz())}
          """)
    arbol.nivel(80,arbol.get_raiz())
    arbol.nivel(5,arbol.get_raiz())
    arbol.nivel(50,arbol.get_raiz())
    arbol.nivel(30,arbol.get_raiz())
    arbol.nivel(3120,arbol.get_raiz())
    print(f"""
          hoja:
          50:{arbol.hoja(50,arbol.get_raiz())}
          4:{arbol.hoja(4,arbol.get_raiz())}
          """)
    print(f"""
            hijo:
            5 es hijo de 50?:{arbol.hijo(5,50,arbol.get_raiz())}
            30 es hijo de 50?:{arbol.hijo(30,50,arbol.get_raiz())}
            """)
    print(f"""
            padre ocupando la funcion hijo:
            50 es padre de 5?:{arbol.hijo(50,5,arbol.get_raiz())}
            50 es padre de 30?:{arbol.hijo(30,50,arbol.get_raiz())}
            """)
    camino = arbol.camino(50,5,arbol.get_raiz())
    print(f"camino de {50} a {5}")
    if camino is not None:
        for valor in camino:
            print(valor,end=" ")
        print()
        camino = []
    else:
        print("No existe")
    
    arbol.padre_y_hermano(30,arbol.get_raiz())
    print(f"Cantidad de nodos: {arbol.cantidad_nodos(arbol.get_raiz())}")
    print(f"Altura del arbol {arbol.altura(arbol.get_raiz())}")
    print("sucesores de 30")
    arbol.sucesores(30,arbol.get_raiz())
    print()
    print("eliminando el nodo 40")
    arbol.eliminar(40,arbol.get_raiz())
    arbol.inorden(arbol.get_raiz())
    print()
    arbol.grado(50,arbol.get_raiz())
    arbol.grado(5,arbol.get_raiz())    
    arbol.cont_sucesores(30,arbol.get_raiz())