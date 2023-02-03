# Declare a common_elements function that accepts a dictionary.  It should return a list with all elements that are found
# as both a key and a value in the dictionary.
#
# HINT: Use the in operation to check for inclusion in a view or list object
#
# my_dict = {
#   "A": "K",
#   "B": "D",
#   "C": "A",
#   "D": "Z"
# }
#
# common_elements(my_dict) => ["A", "D"]

def algorithm(map: dict) -> None:
    def common_elements(map: dict) -> list:
        result = list()
        values_list = map.values()
        for key in map.keys():
            if key in values_list:
                result.append(key)
        return result

    print(f"The list of letters that are both a key and a pattern ", common_elements(map))


my_dict = {"A": "K", "B": "D", "C": "A", "D": "Z"}
algorithm(my_dict)
