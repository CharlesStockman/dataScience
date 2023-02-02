# Declare a length_match function that accepts a list of strings and an integer. It should return a count of the number
# of strings whose length is equal to the number.
#
# length_match(["cat", "dog", "kangaroo", "mouse"], 3)) => 2
# length_match(["cat", "dog", "kangaroo", "mouse"], 5)) => 1
# length_match(["cat", "dog", "kangaroo", "mouse"], 4)) => 0
# length_match([], 5)) => 0

def algorithm(algorithm_collection: list, algorithm_length_of_string: int) -> None:
    def length_match(collection: list, length_of_string: int) -> int:
        value = 0
        for item in collection:
            if len(item) != length_of_string:
                continue
            value += 1
        return value

    print("The number of string matching the specified length is",
          length_match(algorithm_collection, algorithm_length_of_string))


algorithm(["cat", "dog", "kangaroo", "mouse"], 3)
algorithm(["cat", "dog", "kangaroo", "mouse"], 5)
algorithm(["cat", "dog", "kangaroo", "mouse"], 4)
algorithm([], 5)
