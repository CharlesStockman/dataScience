# Part A: Instantiation

# Define a BusTrip class that is initialized with a destination, a bus company, and a price for the trip. 
# Preserve the arguments as attributes on the object. The choice of whether to use protected attributes is up to you.

# Part B: String Representation

# The string representation of a BusTrip object must be a string in the form of:
# You paid 24.99 to Greyhound to go to Boston.
# In this example, “Boston” is the destination, “Greyhound” is the bus company, and 24.99 is the price. 
# These are all fed in as arguments when a BusTrip object is initialized.

class BusTrip:
    def __init__(self, destination, company, price):
        self.destination = destination
        self.company = company
        self.price = price

    def __str__(self):
        return f'You Paid {self.price} to {self.company} to go to {self.destination}'


boston1 = BusTrip(destination="Boston", company="Greyhound", price=24.99)
boston2 = BusTrip(destination="Boston", company="Megabus", price=22.99)
boston3 = BusTrip(destination="Boston", company="Megabus", price=49.99)
philly = BusTrip(destination="Philadelphia", company="Peter Pan", price=12.99)

print(boston1)
print(boston2)
print(boston3)
