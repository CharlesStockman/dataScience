# Declare an invert function that accepts a dictionary object. # The function should return a new dictionary where the
# keys and values from the original dictionary are inverted. # Each key should now be a value, and each value should be
# a key. # Assume both the keys and values of the dictionary are immutable.
#
# my_dict = {
#   "A": "B", 
#   "C": "D",
#   "E": "F"
# }
#
# invert(my_dict) => {'B': 'A', 'D': 'C', 'F': 'E'}

def algorithm(algorithm_my_dict: dict) -> None:
    def invert(invert_map: dict) -> dict:
        result = dict()
        for key, value in invert_map.items():
            result[value] = key
        return result

    print("The inverse map is ", invert(algorithm_my_dict))


algorithm({"A": "B", "C": "D", "E": "F"})


# Declare a count_of_value function that accepts a dictionary and an integer. It should return a count of the number of
# times the integer appears # as a value among the dictionary’s values.
#
# my_dict = { "a" : 5, "b" : 3, "c" : 5 }
#
# count_of_value(my_dict, 5) => 2
# count_of_value(my_dict, 3) => 1

def algorithm(algorithm_map: dict, algorithm_map_value_to_count: int) -> None:
    def count_of_value(count_map: dict, map_value_to_count: int) -> int:
        result = 0
        for _, value in count_map.items():
            if value == map_value_to_count:
                result += 1
        return result

    print("The number of time", algorithm_map_value_to_count, "is called",
          count_of_value(algorithm_map, algorithm_map_value_to_count))


my_dict = {"a": 5, "b": 3, "c": 5}
algorithm(my_dict, 5)
algorithm(my_dict, 3)


# Declare a sum_of_values that accepts a dictionary and a list of strings.
# The dictionary will have keys of strings and values of numbers.
#
# The function should return the sum of values for dictionary 
# keys that are also found in the list.
#
# NOTE: sum is a reserved keyword in Python. Don’t use it as a variable name.
#
# my_dict = { "a": 5, "b": 3, "c": 10 }
#
# sum_of_values(my_dict, ["a"])  => 5
# sum_of_values(my_dict, ["a", "c"])  => 15
# sum_of_values(my_dict, ["a", "c", "b"])  => 18
# sum_of_values(my_dict, ["z"])  => 0


def algorithm(algorithm_map: dict, algorithm_input_keys: list) -> None:
    def sum_of_values(sum_map: dict, input_keys: list) -> int:
        result = 0
        for key in input_keys:
            value = sum_map.get(key, 0)
            result += value
        return result

    print("Sum of the input keys are ", sum_of_values(algorithm_map, algorithm_input_keys))


my_dict2 = {"a": 5, "b": 3, "c": 10}
algorithm(my_dict2, ["a"])
algorithm(my_dict2, ["a", "c"])
algorithm(my_dict2, ["a", "c", "b"])
algorithm(my_dict2, ["z"])
