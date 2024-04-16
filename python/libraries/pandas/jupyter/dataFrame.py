"""
1. Print the items in people as comma seperated values
2. Sort people so that they are ordered by age, and print
3. Sort people so that they are ordered by age first, and then their names,
   i.e. Bob and Charlie should be next to each other due to their ages with
   Bob first due to his name.

   These are the four questions, and I am tired using the basic technology to solve them, so
   I have decided to use dataframe since
"""
import logging
import pandas as pd

data_frame_as_string = lambda data_frame: data_frame.to_string()

logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def create_data_frame() -> pd.DataFrame:
    """
        Create a data frame which will be used the exercises
    """

    # Data To be inserted into the data frame.
    people = [{'name': 'Charlie', 'age': 35},
              {'name': 'Alice', 'age': 30},
              {'name': 'Eve', 'age': 20},
              {'name': 'Gail', 'age': 30},
              {'name': 'Dennis', 'age': 25},
              {'name': 'Bob', 'age': 35},
              {'name': 'Fred', 'age': 25}, ]

    # Initialize the data Frame
    #   Capitalize the first letter of each column
    #   @todo -- Experiment with capitalizing the Title by manipulating the dataframe
    #
    data_frame = pd.DataFrame(people)
    data_frame.rename(columns={'name': 'Name', 'age': 'Age'}, inplace=True)

    logging.debug("The original data_frame is \n %s", data_frame_as_string(data_frame))

    return data_frame


def display_names_of_people() -> list:
    """
           Print the items in people as comma seperated values

           >>> display_names_of_people()
           ['Charlie', 'Alice', 'Eve', 'Gail', 'Dennis', 'Bob', 'Fred']

    """

    logging.debug("--- Entered display_names_of_people ---")
    data_frame = create_data_frame()

    return data_frame['Name'].to_list()


def sort_by_age() -> None:
    """
        Sort people so that they are ordered by age, and print

        >>> sort_by_age()

    """

    logging.debug("\n--- Entered sort_by_age ---")

    data_frame = create_data_frame()

    data_frame.sort_values(by=['Age'], inplace=True)
    logging.debug("The data frame ordered by age is \n %s", data_frame_as_string(data_frame))


def sort_by_age_and_name() -> None:
    """
        3. Sort people so that they are ordered by age first, and then their names,
        i.e. Bob and Charlie should be next to each other due to their ages with
        Bob first due to his name.

        >>> sort_by_age_and_name()

    """

    logging.debug("\n--- Entered Sort by age and name ---")

    data_frame = create_data_frame()
    data_frame.sort_values(by=['Age', 'Name'], inplace=True)
    logging.debug("The data frame ordered by Age is \n %s ", data_frame_as_string(data_frame))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
