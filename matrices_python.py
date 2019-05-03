cars = ["Ford", "Volvo", "Bmw"]

print(cars)

x = cars[0]

cars[0] = "Michubichi"
print(cars)

cars.append("Chevrolet")
print(cars)

cars.pop()
print(cars)

cars.append("Chevrolet")
cars.remove("Volvo")
print(cars)