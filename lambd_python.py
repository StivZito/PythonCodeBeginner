#pequeña funcion que toma uno o varios parametros pero solo puede tener una expresion

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b 
print(x(5,6))

x = lambda a, b, c : a + b + c 
print(x(5, 6, 2))

def myfunc(n):
	return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#lambda llamado dentro de una funcion
def myfunc(n):
	return lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))