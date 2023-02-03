# Define an only_evens function that accepts a list of numbers. # It should return a new list consisting of only the
# even numbers from the original list.
#
# only_evens([4, 8, 15, 16, 23, 42]) => [4, 8, 16, 42]
# only_evens([1, 3, 5]) => []
# only_evens([])        => []

def algorithm(algorithm_collection: list) -> None:
    def only_evens(collection: list) -> list:
        result = []
        for item in collection:
            if item % 2 == 0:
                result.append(item)
        return result

    print("The new list now contains only events", only_evens(algorithm_collection))


algorithm([4, 8, 15, 16, 23, 42])
algorithm([1, 3, 5])
algorithm([])


# Write a factors function that accepts a positive whole number# It should return a list of all of the number's factors
# in ascending order.  HINT: Could the range function be helpful here? Or maybe a while loop?
#
# factors(1)  => [1]
# factors(2)  => [1, 2]
# factors(10) => [1, 2, 5, 10]
# factors(64) => [1, 2, 4, 8, 16, 32, 64]

def algorithm(algorithm_number: int) -> None:
    def factors(number: int) -> list:
        values = []
        for item in range(1, number + 1):
            if number % item == 0:
                values.append(item)
        return values

    print("The factors for the number are ", factors(algorithm_number))


algorithm(1)
algorithm(2)
algorithm(10)
algorithm(64)
