def calcular_factorial(numero):
    stack = []
    def factorial(n):
        if n == 0:
            return 1
        else:
            print(f"Factorial({n}) -> Apilando: Factorial({n-1})")
            stack.append(n)
            resultado = n * factorial(n-1)
            print(f"Desapilando: Factorial({n}) = {n} * Factorial({n-1}) = {resultado}")
            stack.pop()
            return resultado
    resultado_Final = factorial(numero)
    print(f"Factorial de {numero}! es {resultado_Final}")
        
if __name__ == "__main__":
    numero = int(input("Ingrese numero a obtener su factorial\n"))
    calcular_factorial(numero)