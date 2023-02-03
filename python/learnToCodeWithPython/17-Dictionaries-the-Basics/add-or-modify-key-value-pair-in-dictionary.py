# Define a to_dictionary function that accepts a list argument. # The function should return a dictionary where the
# keys are the strings # and the values are their original index positions in the list.
#
# detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
# to_dictionary(detectives) => {'Sherlock Holmes': 0, 
#                               'Hercule Poirot': 1, 
#                               'Nancy Drew': 2}


def algorithm(algorithm_collection: list) -> None:
    def to_dictionary(collection: list) -> dict:
        result = dict()
        for index, string in enumerate(collection):
            result[string] = index
        return result

    print(f"The created dictionary is {to_dictionary(algorithm_collection)} ")


algorithm(["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"])
