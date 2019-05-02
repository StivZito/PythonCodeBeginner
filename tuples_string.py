#en las tuplas no se pueden modificar los valores de la misma
thistuple = ("apple","banana","cherry")
print(thistuple)

#muestra un elemento especifico de la tupla
print(thistuple[2])

#recorre la tupla
for x in thistuple:
	print(x)

#valida si un elemento esta en la tupla 
if "apple" in thistuple:
	print("yeah, cabron aqui estoy xD")

#muestra la longitud de la tupla
print(len(thistuple))

#si se puede eliminar toda la tupla
del thistuple

thistuple = ("apple","banana","cherry")

#las tuplan no se pueden editar o eliminar un registro, o agregart un registro