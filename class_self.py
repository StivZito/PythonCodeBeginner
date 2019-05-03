class  Person(object):
	"""docstring for  Person"""
	def __init__(newself, name, age):
		newself.name = name
		newself.age  = age 

	def myFunc(abc):
		print("On tas " + abc.name)
		#print(abc.age)

p1 = Person("jhon",56)
p1.age =  32
del p1.age
del p1
p1.myFunc()