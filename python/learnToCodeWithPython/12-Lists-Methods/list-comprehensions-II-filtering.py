# Declare a function destroy_elements that accepts two lists. It should return a list of all elements from the first
# list that are NOT contained in the second list.  Use list comprehension in your solution.
#
# destroy_elements([1, 2, 3], [1, 2]) => [3]
# destroy_elements([1, 2, 3], [1, 2, 3]) => []
# destroy_elements([1, 2, 3], [4, 5]) => [1, 2, 3]

def algorithm(algorithm_list1: list, algorithm_list2: list) -> None:
    def destroy_elements(list1: list, list2: list) -> list:
        values = [value for value in list1 + list2 if not (value in list1 and value in list2)]
        return values

    print("The two list are combined and have the elements that only appear in one list ",
          destroy_elements(algorithm_list1, algorithm_list2))


algorithm([1, 2, 3], [1, 2])
algorithm([1, 2, 3], [1, 2, 3])
algorithm([1, 2, 3], [4, 5])
