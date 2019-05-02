#creando el diccionario
thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year" : 1964
}

print(thisdict)

#obteniendo el valor de una clave 
x = thisdict["model"]
print(x)

#con get tambie nse puede potener el valor de una clave 
z = thisdict.get("brand")
print(z)

#agregando una nueva clave y valor 
thisdict["year"] = 2018
print(thisdict)

#recorriendo las claves
for x in thisdict:
	print(x)

#recorriendo los valores 
for y in thisdict:
	print(thisdict[y])

#otra forma de recorrer los valores 
for z in thisdict.values():
	print(z)

#recorriendo clave y valor
for a, b in thisdict.items():
	print(a, b)

#vlidando si esta dentro del diccionario 
if "model" in thisdict:
	print("aqui estamos papa!")

#impresion de longitud de diccionario
print(len(thisdict))

#añadismo otros valor y clave
thisdict["color"] = "red"
print(thisdict)

#elimina el elemnto model 
thisdict.pop("model")
print(thisdict)


thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year" : 1964
}
thisdict["color"]= "yellow"
print(thisdict)

#elimina la ultima clave
thisdict.popitem()
print(thisdict)


thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year" : 1964
}
thisdict["color"]= "yellow"

#elimina el elemento esficio
del thisdict["model"]
print(thisdict)

#elimina el elemento completamente 
del thisdict
#print(thisdict) #error porque no existe ya el registrp


thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year" : 1964
}

#vacia el elemento 
thisdict.clear()
print(thisdict)

#copia los elementos a otro diccionario
thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year" : 1964
}
newdict = thisdict.copy()
print(newdict)