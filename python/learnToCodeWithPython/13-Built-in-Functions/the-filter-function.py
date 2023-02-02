# Declare a function right_words that accepts a list of words and a number. Return a new list with the words that have
# a length equal to the number.  Do NOT use list comprehension.
#
# right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3) => ['cat', 'dog', 'ace']
# right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5) => ['heart']
# right_words([], 4) => []

def algorithm(algorithm_collection: list, algorithm_length_must_be: int) -> None:
    def right_words(collection: list, length_must_be) -> list:
        value = filter(lambda item: len(item) == length_must_be, collection)
        value = list(value)
        return value

    print("The string with the same lengths are ", right_words(algorithm_collection, algorithm_length_must_be))


algorithm(['cat', 'dog', 'bean', 'ace', 'heart'], 3)
algorithm(['cat', 'dog', 'bean', 'ace', 'heart'], 5)
algorithm([], 4)


# Declare an only_odds function. It should return a list with only the odd numbers.  Do NOT use list comprehension.
#
# only_odds([1, 3, 5, 6, 7, 8]) =>  [1, 3, 5, 7]
# only_odds([2, 4, 6, 8])       =>  []

def algorithm(algorithm_collection: list) -> None:
    def only_odds(collection: list) -> list:
        value = filter(lambda item: item % 2 != 0, collection)
        value = list(value)
        return value

    print("The list of even number is ", only_odds(algorithm_collection))


algorithm([1, 3, 5, 6, 7, 8])
algorithm([2, 4, 6, 8])
