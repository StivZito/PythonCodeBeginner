#----------------------Input para ingresar el teclado
#print("Ingrese su nombre")
#x = input()
#print("Hola, ", x)
#------------creas la lista
thislist = ["apple", "banana", "cherry"]
print(thislist)

#------------seleccionar un objeto especifoc la lista
print(thislist[2])

#------------se modificad un indice de la lista
thislist[2] = "pokemon"
print(thislist)

#------------se recorre la lista
for x in thislist:
	print(x)

#------------valida si un elemento especifico se encuentra en la lista 
if "pokemon" in thislist:
	print("eres un cabron you")

#------------len presenta el numero de elementos de la lista 
print(len(thislist))

#------------agrega elemnetos a la lista -- al final 
thislist.append("metalgarurmon")
for y in thislist:
	print(y)

#------------inserta un elemento en un indice especifoc 
thislist.insert(1,"banana")
print(thislist)

#------------remueve un elemento especifico de la lista
thislist.remove("banana")
print(thislist)

#------------elimina un elemento de la lista, si no se especifica un indice elimina lo ultimo
thislist.pop()
print(thislist)

#------------elimina un elemento especifico de la lista 
del thislist[0]
print(thislist)

#------------elimina la lista
del thislist

#------------vaciar la lista 
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#------------copia los datos de una lista a otra 
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#------------copia datos de una lista a otra la propiueda de list 
thislist = ["apple", "banana", "cherry"]
copylist = list(thislist)
print(copylist)

#------------instancia a manera de constructor
newlist = list(("ichi", "ni" , "san"))
print(newlist)