# Declare a count_of_a function that accepts a list of strings.# It should return a list with counts of how many “a”
# characters appear per string.  Do NOT use list comprehension.
#
# count_of_a(["alligator", "aardvark", "albatross"]) => [2, 3, 2]
# count_of_a(["plywood"]) => [0]
# count_of_a([]) => []

def algorithm(algorithm_collection: list) -> None:
    def count_of_a(collection: list) -> list:
        value = map(lambda item: item.count("a"), collection)
        value = list(value)
        return value

    print("The counts of number of times 'a' appears is ", count_of_a(algorithm_collection))


algorithm(["alligator", "aardvark", "albatross"])
algorithm(["plywood"])
algorithm([])
