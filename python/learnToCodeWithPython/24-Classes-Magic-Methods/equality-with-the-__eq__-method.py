# Part A: Instantiation

# Define a BusTrip class that is initialized with a destination, a bus company, and a price for the trip. 
# Preserve the arguments as attributes on the object. The choice of whether to use protected attributes is up to you.

# Part C: Equality

# Implement equality logic between two different BusTrip objects.
# Two BusTrips object are considered equal if:
#   -- they have the same destination
#   -- their price is within 3 dollars of each other
# HINT: Use Python’s abs function to calculate the absolute value of a number.

class BusTrip:
    def __init__(self, destination, company, price):
        self.destination = destination
        self.company = company
        self.price = price

    def __eq__(self, other):
        result = False
        price_difference_within_three_dollars = abs(self.price - other.price) <= 3.0
        if self.destination == other.destination and price_difference_within_three_dollars:
            result = True
        return result


# Sample Execution
boston1 = BusTrip(destination="Boston", company="Greyhound", price=24.99)
boston2 = BusTrip(destination="Boston", company="Megabus", price=22.99)
boston3 = BusTrip(destination="Boston", company="Megabus", price=49.99)
philly = BusTrip(destination="Philadelphia", company="Peter Pan", price=12.99)

print(boston1 == philly)  # False - different destinations
print(boston1 == boston2)  # True - same destination and insignificant price difference
print(boston1 == boston3)  # False - large price difference
