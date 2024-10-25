class Nodo:
    def __init__(self, coef,exp):
        self.__coef = coef
        self.__exp = exp
        self.__siguiente = None

    # obtenerters y Setters para los atributos privados
    def obtener_coef(self):
        return self.__coef
    
    def obtener_exp(self):
        return self.__exp

    def obtener_siguiente(self):
        return self.__siguiente

    def set_siguiente(self, siguiente):
        self.__siguiente = siguiente

class ListaOrdenadaEncadenada:
    def __init__(self):
        self.__cabeza = None
        self.__cantidad = 0

    # obtenerters para acceder a atributos privados
    def obtener_cabeza(self):
        return self.__cabeza

    def obtener_cantidad(self):
        return self.__cantidad

    def vacia(self):
        return self.__cantidad == 0

    def insertar(self, coef,exp):
        nuevo = Nodo(coef,exp)
        # Si la lista está vacía o el nuevo elemento debe ir al principio
        if self.__cabeza is None or self.__cabeza.obtener_exp() >= exp:
            nuevo.set_siguiente(self.__cabeza)
            self.__cabeza = nuevo
        else:
            # Encuentra la posición correcta para insertar el nuevo elemento
            actual = self.__cabeza
            while actual.obtener_siguiente() is not None and actual.obtener_siguiente().obtener_exp() < exp:
                actual = actual.obtener_siguiente()
            # Inserta el nuevo elemento
            nuevo.set_siguiente(actual.obtener_siguiente())
            actual.set_siguiente(nuevo)
        self.__cantidad += 1

    def suprimir(self, pos):
        if 1 > pos > self.__cantidad:
            print("Error: Posición no válida.")
            return

        # Caso especial: eliminar el primer nodo
        if pos == 1:
            self.__cabeza = self.__cabeza.obtener_siguiente()
        else:
            actual = self.__cabeza
            # Navegar hasta el nodo anterior al que se quiere eliminar
            for i in range(1, pos - 1):
                if actual is None:
                    print("Error: Posición no válida.")
                    return
                actual = actual.obtener_siguiente()

            # Verificar si se encontró el nodo en la posición deseada
            siguiente = actual.obtener_siguiente()
            if siguiente is not None:
                # Eliminar el nodo en la posición dada
                actual.set_siguiente(siguiente.obtener_siguiente())
            else:
                print("Error: Posición no válida.")
                return

        self.__cantidad -= 1

    def buscar(self, exp):
        actual = self.__cabeza
        pos = 1
        band = False
        while actual is not None and not band:
            if actual.obtener_exp() == exp:
                band = True
            else:
                actual = actual.obtener_siguiente()
                pos += 1
        if band:
            return pos
        else:
            print("Error: Elemento no encontrado.")
            return None

    def primer_elemento(self):
        if not self.vacia():
            return self.__cabeza.obtener_exp()
        print("Error: La lista está vacía.")
        return None

    def ultimo_elemento(self):
        actual = self.__cabeza
        if not self.vacia():
            while actual.obtener_siguiente() is not None:
                actual = actual.obtener_siguiente()
            return actual.obtener_exp()
        else:
            print("Error: La lista está vacía.")
            return None

    def siguiente_posicion(self, p):
        if 1 <= p < self.__cantidad:
            return p + 1
        print("Error: No hay posición siguiente.")
        return None

    def anterior_posicion(self, p):
        if 1 < p <= self.__cantidad:
            return p - 1
        print("Error: No hay posición anterior.")
        return None

    def recorrer(self):
        actual = self.__cabeza
        while actual is not None:
            if actual.obtener_coef() > 0:
                if actual.obtener_exp() == 1:
                    print(f"+ {actual.obtener_coef()}x", end=" ")
                else:
                    print(f"+ {actual.obtener_coef()}x^{actual.obtener_exp()}", end=" ")
            else:
                if actual.obtener_exp() == 1:
                    print(f"{actual.obtener_coef()}x", end=" ")
                else:
                    print(f"{actual.obtener_coef()}x^{actual.obtener_exp()}", end=" ")
                
            actual = actual.obtener_siguiente()
        print()
    def sumar(self,otro):
        p3 = ListaOrdenadaEncadenada()
        cabeza1 = self.obtener_cabeza()
        cabeza2 = otro.obtener_cabeza()
        while(cabeza1 is not None or cabeza2 is not None):
            if cabeza1 is None:
                # Copiar el resto de la lista 2
                coef = cabeza2.obtener_coef()
                exp = cabeza2.obtener_exp()
                cabeza2 = cabeza2.obtener_siguiente()
            elif cabeza2 is None:
                # Copiar el resto de la lista 1
                coef = cabeza1.obtener_coef()
                exp = cabeza1.obtener_exp()
                cabeza1 = cabeza1.obtener_siguiente()
            elif cabeza1.obtener_exp() < cabeza2.obtener_exp():
                coef = cabeza1.obtener_coef()
                exp = cabeza1.obtener_exp()
                cabeza1 = cabeza1.obtener_siguiente()
            elif cabeza1.obtener_exp() > cabeza2.obtener_exp():
                coef = cabeza2.obtener_coef()
                exp = cabeza2.obtener_exp()
                cabeza2 = cabeza2.obtener_siguiente()
            else:  # Ambos tienen el mismo exponente
                coef = cabeza1.obtener_coef() + cabeza2.obtener_coef()
                exp = cabeza1.obtener_exp()
                cabeza1 = cabeza1.obtener_siguiente()
                cabeza2 = cabeza2.obtener_siguiente()

            if coef != 0:
                p3.insertar(coef, exp)

        print("Suma de polinomios:")
        p3.recorrer()
    def resta(self,otro):
        p3 = ListaOrdenadaEncadenada()
        cabeza1 = self.obtener_cabeza()
        cabeza2 = otro.obtener_cabeza()

        while cabeza1 is not None or cabeza2 is not None:
            if cabeza1 is None:
                # Copiar el resto de la lista 2
                coef = cabeza2.obtener_coef()
                exp = cabeza2.obtener_exp()
                cabeza2 = cabeza2.obtener_siguiente()
            elif cabeza2 is None:
                # Copiar el resto de la lista 1
                coef = cabeza1.obtener_coef()
                exp = cabeza1.obtener_exp()
                cabeza1 = cabeza1.obtener_siguiente()
            elif cabeza1.obtener_exp() < cabeza2.obtener_exp():
                coef = cabeza1.obtener_coef()
                exp = cabeza1.obtener_exp()
                cabeza1 = cabeza1.obtener_siguiente()
            elif cabeza1.obtener_exp() > cabeza2.obtener_exp():
                coef = cabeza2.obtener_coef()
                exp = cabeza2.obtener_exp()
                cabeza2 = cabeza2.obtener_siguiente()
            else:  # Ambos tienen el mismo exponente
                coef = cabeza1.obtener_coef() - cabeza2.obtener_coef()
                exp = cabeza1.obtener_exp()
                cabeza1 = cabeza1.obtener_siguiente()
                cabeza2 = cabeza2.obtener_siguiente()

            if coef != 0:
                p3.insertar(coef, exp)

        print("Resta de polinomios:")
        p3.recorrer()
    def multiplicar_escalar(self,k):
        if k == 0:
            print("chistosito eh\n")
            return
        else:
            p4 = ListaOrdenadaEncadenada()
            aux = self.obtener_cabeza()
            while aux is not None:
                p4.insertar(coef = aux.obtener_coef()*k,exp = aux.obtener_exp())
                aux = aux.obtener_siguiente()
            print(f"Multiplicar por escalar {k}:")
            p4.recorrer()
if __name__ == '__main__':
    polinomio1 = ListaOrdenadaEncadenada()
    polinomio1.insertar(2, 2)
    polinomio1.insertar(1, 1)
    polinomio1.insertar(-2, 4)
    
    polinomio2 = ListaOrdenadaEncadenada()
    polinomio2.insertar(1, 2)
    polinomio2.insertar(1, 1)
    polinomio2.insertar(1, 4)
    
    polinomio1.recorrer()
    polinomio2.recorrer()

    polinomio1.sumar(polinomio2)
    polinomio1.resta(polinomio2)
    polinomio1.multiplicar_escalar(2)