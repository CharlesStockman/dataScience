# musical.py

# Declare a Musical class that accepts a name parameter. 
# In the initialization process for an object, assign the name parameter to a name attribute on the object.
# Instantiate a Musical object with the name “Rent” and assign it to an “rent" variable.
# Instantiate another object from the class with the name “Book of Mormon" and assign it to a “mormon” variable.
# Instantiate a third object from the class with the name “Chicago" and assign it to a “chicago” variable.
class Musical:
    def __init__(self, name: str):
        self.name = name


rent = Musical("Rent")
print("name of the musical object is", rent.name)

mormon = Musical("Book of Mormon")
print("name of the musical object is", mormon.name)

chicago = Musical("Chicago")
print("name of the musical object is", chicago.name)


# Declare a Shape class that accepts a parameter sides.
# In the initialization process for an object, assign the parameter sides to a sides attribute on the object.
# Instantiate a Shape object with 3 sides and assign it to a “triangle" variable.
# Instantiate a Shape object with 4 sides and assign it to a “square" variable.
# Instantiate a Shape object with 10 sides and assign it to a “decagon" variable.
class Shape:
    def __init__(self, sides: int):
        self.sides = sides


triangle = Shape(3)
print("A triangle has number of sides:", triangle.sides)

square = Shape(4)
print("A square has number of sides:", square.sides)

decagon = Shape(10)
print("A decagon has number of sides:", decagon.sides)


# skyscraper.py Declare a Skyscraper class that accepts name and year parameters. In the initialization process for
# an object, assign the name parameter to a name attribute and the year parameter to a year attribute. Instantiate a
# Skyscraper object with the name “Empire State Building”  and the year 1931. Assign it to a “empire" variable.
# Instantiate a Skyscraper object with the name “One World Trade Center” and the year 2014. Assign it to a “wtc"
# variable.
class Skyscraper:
    def __init__(self, name: str, year: str):
        self.name = name
        self.year = year


empire = Skyscraper("Empire Status Building", "1931")
print(f"The {empire.name} was built in {empire.year}")

wtc = Skyscraper("World Trade Center", "2014")
print(f"The {wtc.name} was built in {wtc.year}")
