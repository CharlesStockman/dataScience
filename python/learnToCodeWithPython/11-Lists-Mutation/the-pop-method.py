# Declare a push_or_pop function that accepts a list of numbers.  # Build up and return a new list by iterating
# over the list of numbers.  If a number is greater than 5, add it to the end of the new list # If a number is less
# than or equal to 5, remove the last element added to the new list,  Assume the order of numbers in the argument will
# never require removing from an empty list
#
# push_or_pop([10]) => [10]
# push_or_pop([10, 4]) => []
# push_or_pop([10, 20, 30]) => [10, 20, 30]
# push_or_pop([10, 20, 2, 30]) => [10, 30]

def algorithm(algorithm_collection: list) -> None:
    def push_or_pop(collection: list) -> list:
        value = []
        for item in collection:
            if item > 5:
                value.append(item)
            else:
                value.pop()
        return value

    print("The list after appending or popping an element is ", push_or_pop(algorithm_collection))


algorithm([10])
algorithm([10, 4])
algorithm([10, 20, 30])
algorithm([10, 20, 2, 30])
