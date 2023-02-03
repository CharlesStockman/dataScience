# Declare a delete_all function that accepts a list of strings and a target string.  Remove all occurrences of the
# target string from the list and return it
#
# delete_all([1, 3, 5], 3) => [1, 5]
# delete_all([5, 3, 5], 5) => [3]
# delete_all([4, 4, 4], 4) => []
# delete_all([4, 4, 4], 6) => [4, 4, 4]
#

def algorithm(algorithm_collection: list, algorithm_item_to_be_removed: int) -> None:
    def delete_all(collection: list, item_to_be_removed: int) -> list:
        indexes_to_be_deleted = []
        for index, item in enumerate(collection):
            if item == item_to_be_removed:
                indexes_to_be_deleted.append(index)

        for index in indexes_to_be_deleted[::-1]:
            del collection[index]
        return collection

    print("The list without the string is", delete_all(algorithm_collection, algorithm_item_to_be_removed))


algorithm([1, 3, 5], 3)
algorithm([5, 3, 5], 5)
algorithm([4, 4, 4], 4)
algorithm([4, 4, 4], 6)
