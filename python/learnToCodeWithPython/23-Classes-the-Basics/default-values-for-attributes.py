# zombie.py

# Declare a Zombie class that accepts health and brains_eaten parameters. 

# In the initialization process for an object, assign the two parameters to two attributes with the same name.
# If the instantiation does not pass a health parameter, it should be assigned a default value of 100.
# If the instantiation does not pass a brains_eaten parameter, it should be assigned a default value of 5.

# Instantiate a Zombie object with 80 health and 5 brains eaten. Assign it to a “bob” variable.
# Instantiate a Zombie object with  3 brains eaten. Assign it to a “sally” variable.
# Instantiate a Zombie object with no custom parameters. Assign it to a “benjamin” variable.

# Practice instantiating the objects with both positional and keyword arguments.

class Zombie:
    def __init__(self, health: int = 100, brains_eaten: int = 5):
        self.health = health
        self.brains_eaten = brains_eaten


bob = Zombie(health=80, brains_eaten=5)
print(f"Bob has a health of {bob.health} and has eaten {bob.brains_eaten} brains")

sally = Zombie(brains_eaten=3)
print(f"Sally has a health of {sally.health} and has eaten {sally.brains_eaten} brains")

benjamin = Zombie()
print(f"Ben has a health of {benjamin.health} and has eaten {benjamin.brains_eaten} brains")
