class Person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname  = lname

	def printname(self):
		print(self.firstname, self.lastname)

x = Person("Jhon","Snow")
x.printname()

class Studen(Person):
	def __init__(self, fname, lname, year):
		Person.__init__(self, fname, lname)
		self.graduationyear = 2019

	def printnameStu(self):
		print(self.firstname, self.lastname)


x = Studen("Mike","Patas Largas",2022)
x.printnameStu()