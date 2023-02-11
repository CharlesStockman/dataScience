"""
   Input: A string with 2 character ( 2-9 ) which will provide a set of numbers
            2: a b c
            3: d e f
            4: g h i
            5: j k l
            6: m n o
            7: p q r s
            8: t u v
            9: w x y z

    Output : For each number the set letter will have permutation performed on them.
"""

from types import MappingProxyType
import itertools
import re

#
#     A dictionary where the key is an integer and the value is a collection of letters
#     An example of an immutable dictionary
numberToLetterGroup = MappingProxyType(
    {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz"
    }

)


def permutations(input: str) -> list:
    """
        Input : String with two numbers from 2-9 inclusive converted to a set of 3-4 characters
        Output: Create the set of permutations of two character strings one from each set.

        >>> permutations(None)
        Traceback (most recent call last):
           ...
        ValueError: The input String cannot be empty or null

        >>> permutations("a1")
        Traceback (most recent call last):
           ...
        ValueError: The input String can only contain digits between 2 and 9

        >>> permutations("24")
        [('a', 'g'), ('a', 'h'), ('a', 'i'), ('b', 'g'), ('b', 'h'), ('b', 'i'), ('c', 'g'), ('c', 'h'), ('c', 'i')]

    """

    if input is None or len(input) == 0:
        raise ValueError("The input String cannot be empty or null")

    if re.search(r'[^23456789]', input):
        raise ValueError("The input String can only contain digits between 2 and 9")

    character_set = lambda x: numberToLetterGroup[int(x)]
    output = itertools.product(character_set(input[0]), character_set(input[-1]))
    results = [nextElement for nextElement in output]

    return results


if __name__ == '__main__':
    import sys
    import doctest

    print("count = ", sys.argv.count("-v"))
    if ( sys.argv.count("v") == 0):
        print(f"For index 2-4 the permutations are: ", permutations("24"))
    else:
        doctest.testmod()