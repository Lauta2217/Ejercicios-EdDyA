class polinomio:
    def __init__(self,terminos):
        self.__terminos = terminos
        
    def mostrar(self):
        i = 1
        polinomio = []
        for coef,exp in self.__terminos:
            if coef > -1:
                if exp == 0:
                    polinomio.append(f"+ {coef}") 
                elif exp == 1:
                    polinomio.append(f"+ {coef}x") 
                else:
                    polinomio.append(f"+ {coef}x^{exp}") 
            elif coef <=-1:
                if exp == 0:
                    polinomio.append(f"{coef}") 
                elif exp == 1:
                    polinomio.append(f"{coef}x") 
                else:
                    polinomio.append(f"{coef}x^{exp}") 
            i+=1
        resultado = " ".join(polinomio)
        print(resultado)
        
    def simplificar(self):
        simplificado = {}
        for coef, exp in self.__terminos:
            if exp in simplificado:
                simplificado[exp] += coef
            else:
                simplificado[exp] = coef
        self.__terminos = [(coef, exp) for exp, coef in simplificado.items() if coef != 0]
        self.__terminos.sort(key=lambda t: t[1], reverse=True)  # Ordenamos nuevamente para asegurar el orden
        
    def suma(self,p2):
        resultado = p1.__terminos + p2.__terminos
        p3 = polinomio(resultado)
        return p3

    def resta(self,p2):
        terminos_negados = []
        for coef,exp in p2.__terminos:
            terminos_negados.append((-coef,exp))
        total = p1.__terminos + terminos_negados
        return polinomio(total)

    def multiplicar_escalar(self,k):
        terminos_multiplicados = []
        for coef,exp in self.__terminos:
            terminos_multiplicados.append((coef * k,exp))
        return polinomio(terminos_multiplicados)
    
p1 = polinomio([(5,3),(3,2),(-2,1),(2,0)])
p1.mostrar()
p2 = polinomio([(3,2),(2,1),(2,0)])

print("SUMA")
p3 = p1.suma(p2)
p3.simplificar()
p3.mostrar()

print("RESTA")
p3 = p1.resta(p2)
p3.simplificar()
p3.mostrar()


print("multiplicar por escalar")
p3 = p1.multiplicar_escalar(2)
p3.simplificar()
p3.mostrar()

"""[(coef, exp) for coef, exp in p.terminos] esa linea es la clave"""