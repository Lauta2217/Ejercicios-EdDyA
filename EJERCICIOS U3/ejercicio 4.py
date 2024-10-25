from pila_secuencial_paraej4 import Pila
movimientos = 0
def juego_terminado(pilas,cant):
    global movimientos
    if pilas[0].vacia() and pilas[1].vacia():
        print(f"Juego terminado!!!\n cantidad de movimientos realizados: {movimientos}\n cantidad de movimientos minimos que podrias haber realizado:{(2**cant)-1}")
        mostrar_estado(pilas,cant)
def mover_fichas(pilas):
    global movimientos
    origen = int(input("Ingrese pila de la cual quiere sacar la ficha\n"))-1
    destino = int(input("Ingrese pila a la cual quiere mover la ficha\n"))-1
    try:
        if pilas[origen].obtener_tope() < pilas[destino].obtener_tope() or pilas[destino].vacia() and not pilas[origen].vacia():
            pilas[destino].insertar(pilas[origen].obtener_tope())
            pilas[origen].suprimir()
            movimientos+=1
        else:
            print("Movimiento invalido. Imposible colocar una ficha mas grande arriba de una más chica\n")
    except IndexError:
        print("Numero de pila ingresado es incorrecto\n")
    
"""def mostrar_estado(pilas):
    for i,pila in enumerate(pilas, start=1):
        print(f"Pila {i}: {pila}")
    print("-" * 30)"""
def mostrar_estado(pilas,cant):
        for altura in range(cant - 1, -1, -1):  # Iterar desde la parte superior de la pila hacia abajo
            for pila in pilas:
                if altura < len(pila.items) and pila.items[altura] != 0:
                    print(f"{pila.items[altura]:^5}", end=" ")  # Mostrar el elemento en su posición
                else:
                    print("  |  ", end=" ")  # Mostrar una barra para indicar posiciones vacías
            print()  # Nueva línea para la siguiente altura

        print("-" * 30)
        for i in range(1, len(pilas) + 1):
            print(f"Pila {i:^5}", end=" ")  # Mostrar los números de las pilas debajo de ellas
        print("\n" + "-" * 30)
    
def hanoi(cant):
    pila_1 = Pila(cant)
    pila_2 = Pila(cant)
    pila_3 = Pila(cant)
    pilas = [pila_1,pila_2,pila_3]
    movimientos = 0
    for i in range(cant,0,-1):
        pila_1.insertar(i)
    print(f"Estado inicial de las pilas\n")
    mostrar_estado(pilas,cant)
    op = int(input("""Ingrese opcion: 
                 1_Mover fichas
                 2_Consultar estado de las fichas
                 """))
    while op!=0:
        if op == 1:
            mover_fichas(pilas)
            juego_terminado(pilas,cant)
        elif op == 2:
            mostrar_estado(pilas,cant)
        else: print("Numero ingresado no corresponde")
        op = int(input("""Ingrese opcion: 
                 1_Mover fichas
                 2_Consultar estado de las fichas
                 """))
if __name__ == '__main__':
    cant = int(input("ingrese cantidad de fichas con las que va a jugar\n"))
    hanoi(cant)