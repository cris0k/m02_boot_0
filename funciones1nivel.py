def normal(x):
    return x

def cuadrado(y):
    return y * y

def cubo(x):
    return x**3

def sumaTodos(limitTo, f):
    resultado = 0
    for i in range(limitTo + 1):
        resultado += f(i)
        
    return resultado

if __name__ == "__main__": # Como hemos importado sumaTodos a otro sitio, nos ejecuta tambien estos print,
                        #Para que no lo haga le tenemos que poner esta condicion para que solo lo ejecute
                        #cuando estemos en el programa principal.
    print(sumaTodos(100,normal))
    print(sumaTodos(3, cuadrado))