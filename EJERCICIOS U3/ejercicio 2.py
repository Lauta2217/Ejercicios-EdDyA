from pila_encadenada import Pilaa
if __name__ == '__main__':
    pila = Pilaa()
    numero = 8.25
    binario = ""
    numero_entero = int(numero)
    numero_coma = numero - numero_entero
    while numero_entero > 0:
        residuo = numero_entero % 2
        numero_entero = numero_entero // 2
        binario = str(residuo) + binario
    
    precision=10
    binario_fraccionario = ""
    while numero_coma > 0 and len(binario_fraccionario) < precision:
        numero_coma *= 2
        bit = int(numero_coma)
        pila.insertar(bit)
        numero_coma-= bit
    print(binario)
    pila.mostrar(pila.recupera_tope())