#creacion del set
thisset = {"ichi", "ni", "san"}
print(thisset)

#preguntamos por un elemento x dentro del set 
print("ni" in thisset)

#añadir un elemento en el set 
thisset.add("yon")

#añadir mas de un elemento al set 
thisset.update(["go","rok","nana","hachi"])

#recorrer el set 
for x in thisset:
	print(x)

#longitud del set
print(len(thisset))

#eliminar un elemento especifico del set 
thisset.remove("go") #si el elemento no existe, se produce un error
print(thisset)

#descartar un elemento especifico del set 
thisset.discard("nana") #si el elemento no exsite, produce error
print(thisset)

#elimina el ultimo registro del set 
x = thisset.pop() #elimina siempre el ultimo no se sabe cual porque estan desordenados 
print(x)
print(thisset)

#vacia el set
thisset.clear()
print(thisset)

#elimina el set 
thisset = {"ichi", "ni", "san"}
del thisset

#constructor del set 
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)