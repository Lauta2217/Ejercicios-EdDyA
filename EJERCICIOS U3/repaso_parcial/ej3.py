"""lifo: ultimo en entrar primero en salir es decir se ocupa pila"""
from pila_secuencial_default import Pila
def factorial(n,stack):
    if n == 0:
        return 1
    else:
        stack.insertar(n)
        stack.mostrar()
        resultado = n * factorial(n-1,stack)
        stack.suprimir()
        stack.mostrar()
        return resultado
        
if __name__=="__main__":
    n = int(input("Ingrese numero para obtener su factorial\n"))
    stack = Pila(n+1)
    print(f"{n}! = {factorial(n,stack)}")
    
    
   