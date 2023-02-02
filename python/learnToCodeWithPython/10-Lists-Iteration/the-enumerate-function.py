# Define an in_list function that accepts a list of strings and a separate string. Return the index where the string
# exists in the list. If the string does not exist, return -1.  Do NOT use the find or index methods.
#
# strings = ["enchanted", "sparks fly", "long live"]
# in_list(strings, "enchanted")  ==> 0
# in_list(strings, "sparks fly") ==> 1
# in_list(strings, "fifteen")    ==> -1
# in_list(strings, "love story") ==> -1


strings = ["enchanted", "sparks fly", "long live"]


def algorithm(algorithm_strings: list, search_str: str) -> None:
    def in_list(in_list_strings: list, in_list_search_str: str) -> int:
        value = -1
        for index, string in enumerate(in_list_strings):
            if string == in_list_search_str:
                value = index
        return value

    print("The searchStr was found at position:", in_list(algorithm_strings, search_str))


algorithm(strings, "enchanted")
algorithm(strings, "sparks fly")
algorithm(strings, "fifteen")
algorithm(strings, "love story")


# Define a sum_of_values_and_indices function that accepts a list # of numbers.   It should return the sum of all
# elements along with their index values.
#
# sum_of_values_and_indices([1, 2, 3])    => (1 + 0) + (2 + 1) + (3 + 2) => 9
# sum_of_values_and_indices([0, 0, 0, 0]) => 6
# sum_of_values_and_indices([])           => 0

def algorithm2(algorithm_collection: list) -> None:
    def sum_of_values_and_indices(collection: list) -> int:
        value = 0
        for (index, number) in enumerate(collection):
            value += (index + number)
        return value

    print("The value of the all index + all values is: " + str(sum_of_values_and_indices(algorithm_collection)))


algorithm2([1, 2, 3])
algorithm2([0, 0, 0, 0])
algorithm2([])
