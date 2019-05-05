mytuple = ("appel","banana","cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


mystr = "banana"
myit2 = iter(mystr)

print(next(myit2))
print(next(myit2))
print(next(myit2))
print(next(myit2))
print(next(myit2))
print(next(myit2))


strFruta = "banana"
for i in strFruta:
	print(i)