# Define a split_in_two function that accepts a list and a number.
# If the number is even, return the list elements from the third element to the end of the list.
# If the number is odd, return the list elements from index 0 (inclusive) to 2 (exclusive)
#
# values = ["a", "b", "c", "d", "e", "f"]
# split_in_two(values, 3) => ["a", "b"]
# split_in_two(values, 4) => ["c", "d", "e", "f"]
# split_in_two(values, 1) => ["a", "b"]
# split_in_two(values, 10) => ["c", "d", "e", "f"]

values = ["a", "b", "c", "d", "e", "f"]


def algorithm(algorithm_collection: list, number: int) -> None:
    def split_in_two(collection: list, number: int):
        result = collection[2:] if (number % 2 == 0) else collection[0:2]
        return result

    print("The number is", number, "then the value is", split_in_two(algorithm_collection, number))


algorithm(values, 3)
algorithm(values, 4)
algorithm(values, 1)
algorithm(values, 10)
