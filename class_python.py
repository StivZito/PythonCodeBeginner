class Myclass:
	x = 5

p1 = Myclass()
print(p1.x)


class Person:
	def __init__(self, name, age):
		self.name = name
		self.age  = age

p1 = Person("Jhon",36)

print(p1.name)
print(p1.age)