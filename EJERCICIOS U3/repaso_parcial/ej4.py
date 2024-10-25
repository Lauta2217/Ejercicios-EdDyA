"""lifo: ultimo en entrar primero en salir es decir se ocupa pila"""
from pila_secuencial_default import Pila
class Hanoi:
    def __init__(self, fichas, A, B, C):
        self.__pilas = [A, B, C]
        self.__fichas = fichas
        self.__movimientos = 0
    def obtener_pilas(self):
        return self.__pilas
    def aumentar_movimientos(self):
        self.__movimientos += 1
    def juego_terminado(self):
        if self.obtener_pilas()[0].vacia() and self.obtener_pilas()[1].vacia():
            print("Juego terminado!!!")
            self.mostrar_estado()
            print(f"Número de movimientos hechos: {self.__movimientos}")
            print(f"Número de movimientos mínimos: {(2**self.__fichas) - 1}")
            return False
        else:
            return True
    
    def jugando(self):
        band = True
        while band:
            print("Estado de las fichas:")
            self.mostrar_estado()
            origen = int(input("Ingrese pila de la cual va a mover 1, 2 o 3: "))
            destino = int(input("Ingrese pila a la cual quiere mover 1, 2 o 3: "))
            
            if origen == destino:
                print("No se puede mover y sacar a la misma pila xd")
            else:
                ficha_origen = self.obtener_pilas()[origen - 1].obtener_items()[self.obtener_pilas()[origen - 1].obtener_tope()-1]
                ficha_destino = self.obtener_pilas()[destino - 1].obtener_items()[self.obtener_pilas()[destino - 1].obtener_tope()-1]
                
                if ficha_origen == 0:
                    print("La pila de origen no tiene fichas")
                elif ficha_destino == 0 or ficha_origen < ficha_destino:
                    self.obtener_pilas()[destino - 1].insertar(ficha_origen)
                    self.obtener_pilas()[origen - 1].suprimir()
                    self.aumentar_movimientos()
                else:
                    print("No se puede colocar la ficha grande sobre una más chica")
            
            band = self.juego_terminado()
    
    def mostrar_estado(self):
        for altura in range(self.__fichas - 1, -1, -1):
            for pila in self.obtener_pilas():
                if pila.obtener_items()[altura] != 0:
                    print(f"{pila.obtener_items()[altura]:^5}", end=" ")
                else:
                    print("  |  ", end=" ")
            print()
        print("-" * 30)
        for i in range(1, len(self.obtener_pilas()) + 1):
            print(f"Pila {i}|", end=" ")
        print("\n" + "-" * 30)

# Ejecución del juego
if __name__ == '__main__':
    fichas = int(input("Ingrese número de fichas para jugar: "))
    A = Pila(fichas)
    for i in range(fichas, 0, -1):
        A.insertar(i)
    B = Pila(fichas)
    C = Pila(fichas)
    juego = Hanoi(fichas, A, B, C)
    juego.jugando()