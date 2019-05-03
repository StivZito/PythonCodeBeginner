def my_function():
	print("mi primera funcion")

my_function()

def my_function_name(fname):
	print(fname + " Refsnes")

my_function_name("Emil")
my_function_name("Tobias")
my_function_name("Linus")


def my_function_country(country = "Norway"):
	print("Yo soy de " + country )

my_function_country("Sweeden")
my_function_country("India")
my_function_country()
my_function_country("Brazil")

def my_function_loo(food):
	for x in food:
		print(x)

fruits = ["apple", "banana", "cherry"]

my_function_loo(fruits)

def my_function_return(x):
	return 5 * x

print(my_function_return(3))
print(my_function_return(5))
print(my_function_return(9))

def tri_recursion(k):
	if (k>0):
		result = k + tri_recursion(k-1)
		print(result)
	else:
		result=0

	return result

print("\n\n ejemplo de recursion")
tri_recursion(6)


