class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

    def __repr__(self):
        return f"Name:{self.name} and age:{self.age})"

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1 Add nother Cat

class Casey(Cat):
    def sing(self,sounds):
       return f"{sounds}" 

casey = Casey('casey', 5)

print(f"My cat is {casey} and he makes the sound -- {casey.sing('Purr')}")

#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [ Simon('Simon', 3), Sally('Salley', 4), Casey('Casey', 5) ] 
print(my_cats)

#3 Instantiate the Pet class with all your cats use variable my_pets
pets = Pets(my_cats)

#4 Output all of the cats walking using the my_pets instance
pets.walk()
