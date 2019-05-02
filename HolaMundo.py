#-------------------El tipico hola Mundo
#Me llaman el documentador
#print("Hola Mundo!")


#-------------------Aqui vemos que con 3 doble comas inicias comentarios largos en abre y cierre
#"""Aqui estamos utilizando 
#   lo que seria del mundo y de nuestras vida para esos 
#   comentarios madre mia , mas largos que el dia lunes """
#if 5 > 2:
#	print("metalgarurmon")


#-------------------jugando con las variables string
#x = "Madre mia "
#y = "Willy"
#z = x + y
#print(z)


#-------------------jugando con las variables numericas
#x = 3
#y = 5
#z = x + y
#print(z)


#-------------------tipos de variables
#para verificar cualquier tipo de objeto en python utilizaremos la funcion type()
#x = 1   #int
#y = 2.8 #decimal
#z = 1j  #complex o complejo 

#print(type(x))
#print(type(y))
#print(type(z))


#-------------------convertidores o cast de python
#int()
#float
#str
#
#x = int(1)   # x will be 1
#y = float(2.8)   # y will be 2.8
#z = str(3.0)  # z will be '3.0'


#-------------------funciones de cadena
#obtener un caracter especifico de una cadena, 0 es el primera posicion
a = "Hello, World!"
print(a[1])

#para obtener los caracteres se debe poner de que a que posicion
b = "Hello, World!"
print(b[2:5])

#para eliminar los espacios en blanco de cadena, usar fucion strip()
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#El método len () devuelve la longitud de una cadena:
a = "Hello, World!"
print(len(a))

#El método lower () devuelve la cadena en minúsculas:
a = "Hello, World!"
print(a.lower())

#El método upper () devuelve la cadena en mayúsculas:
a = "Hello, World!"
print(a.upper())

#El método split () divide la cadena en subcadenas si encuentra instancias del separador:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']