# Define a Car class that accepts a maker (string), model (string),
# and year (number) attributes and assigns them to respective
# attributes

# Define a Dealership class. Each Dealership object should instantiate with a "cars" attribute set to an empty list.

# A Dealership object should have accept_delivery instance method that accepts a Car object and adds it to the
# Dealership's internal "cars" list

# Indexing into a Dealership with a number should access a specific Car object in the Dealership.

# An index position in a Dealership should also be overrideable with a new Car object (see examples below)

import collections

#
# Define the class Car and instantiate some Cars
#
Car = collections.namedtuple("Car", "maker, model, year")

f150 = Car(maker="Ford", model="F-150", year=2019)
camry = Car(maker="Toyota", model="Camry", year=2020)
porsche = Car(maker="Porsche", model="911 Carrera", year=2021)

print("Cars used in the program")
print("\t", f150)
print("\t", camry)
print("\t", porsche)


#
# Define the Dealership and add the cars to it
#
class Dealership:
    def __init__(self):
        self.cars = []

    def accept_delivery(self, car):
        self.cars.append(car)

    def __getitem__(self, index):
        return self.cars[index]

    def __setitem__(self, index, value):
        self.cars[index] = value


dealership = Dealership()
print("The Dealership has been created and the number of cars is ", len(dealership.cars))

dealership.accept_delivery(f150)
dealership.accept_delivery(camry)

print("The total cars at the dealership are ", len(dealership.cars))

print(dealership[0].year)

dealership[0] = porsche
print("The first card in the dealership has been upgraded to a ", dealership[0])

for car in dealership:
    print(car.maker)
