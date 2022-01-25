from funciones1nivel import sumaTodos 

#doble = lambda x : x**3 tambien se le puede poner nombre y solo utilizar el nombre

print(sumaTodos(3,lambda x: x*2))
print(sumaTodos(100,lambda x: x**3))