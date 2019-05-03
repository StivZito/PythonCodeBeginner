a = 33
b = 200
if b > a:
	print("b es mayor que a")

c = 33
d = 33
if c > d:
	print("c es mayor que d")
elif c == d:
	print("c y d son iguales")

e = 200
f = 33
if e > f:
	print("e es mayor que f")
elif e == f:
	print("e y f son iguales")
else:
	print("e es mayor que f")

if f > e:
	print("f es mayor que e")
else:
	print("f no es mayor que e")


if e > f: print("e es mayor que f")

print("A") if e > f else print("B")

print("A") if a > b else print("=") if a == b else print("B")

if a > b and e > f:
	print("patamon")
else:
	print("pokemon")

if a < b or e < f:print("alguna salio")