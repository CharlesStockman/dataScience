# Define a nested_sum function that accepts a list of lists of numbers  The function should return the sum of the values
# The list may contain empty lists
#
# nested_sum([[1, 2, 3], [4, 5]]) => # 15
# nested_sum([[1, 2, 3], [], [], [4], [5]]) => # 15
# nested_sum([[]]) => 0

def algorithm(algorithm_collection: list) -> None:
    def nested_sum(collection: list) -> int:
        value = 0
        for inner_list in collection:
            for number in inner_list:
                value = value + number
        return value

    print("The total of the number in the multidimensional array is", nested_sum(algorithm_collection))


algorithm([[1, 2, 3], [4, 5]])
algorithm([[1, 2, 3], [], [], [4], [5]])
algorithm([[]])


# Define a fancy_concatenate function that accepts a list of lists of strings   The function should return a
# concatenated stringThe strings in a list should only be concatenated if the length of the list is 3
#
# fancy_concatenate([["A, "B", "C"]]) => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]]) => "ABCDEF"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]]) => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E"]]) => "ABC"
# fancy_concatenate([["A", "B"], ["C", "D"]]) => ""

def algorithm2(algorithm_collection: list) -> None:
    def fancy_concatenate(collection: list) -> int:
        value = ""
        for inner_list in collection:
            if len(inner_list) != 3:
                continue

            for string in inner_list:
                value = value + string
        return value

    print("The string made of list with size 3 is ", fancy_concatenate(algorithm_collection))


algorithm2([["A", "B", "C"]])
algorithm2([["A", "B", "C"], ["D", "E", "F"]])
algorithm2([["A", "B", "C"], ["D", "E", "F", "G"]])
algorithm2([["A", "B", "C"], ["D", "E"]])
algorithm2([["A", "B"], ["C", "D"]])
