import itertools
from typing import Optional, Tuple, Any


def find_euclidean_distance(points: list) -> int:
    """
    Input: list of 8 points where the list is even
    Output: The Euclidean Distance of all the points
    """

    euclidean_distance = 0
    for two_point_group in get_two_points(points):
        euclidean_distance = euclidean_distance + \
                             (two_point_group[1][0] - two_point_group[0][0]) ** 2 + \
                             (two_point_group[1][1] - two_point_group[0][1]) ** 2
    return euclidean_distance


def get_two_points(input: list) -> list:
    """
        A example of a generator
        Input: A collection of points in a list
        Output The next two points are returned.
    """
    for index in range(0, len(input) - 1):
        yield input[index:index + 2]


def find_list_with_shortest_euclidean_distnace(points_list: list) -> Optional[Tuple[Any, ...]]:
    permutations = itertools.permutations(points_list)
    min_euclidean_distance = float('inf')
    selected_permutation = None

    for permutation in permutations:
        current_distance = find_euclidean_distance(permutation)
        if current_distance < min_euclidean_distance:
            min_euclidean_distance = current_distance
            selected_permutation = permutation

    return selected_permutation


coords = [(0, 0), (10, 5), (10, 10), (5, 10), (3, 3), (3, 7), (12, 3), (10, 11)]
print(find_euclidean_distance(coords))
print(find_list_with_shortest_euclidean_distnace(coords))
