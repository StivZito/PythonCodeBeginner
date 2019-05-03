class Person:
	"""docstring for Person"""
	def __init__(self, name, age):
		self.name = name
		self.age  = age

	def myFunc(self):
		print("Hola mi nombre es " + self.name)


p1 = Person("John",36)
p1.myFunc()