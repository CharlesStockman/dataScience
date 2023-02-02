# Define a vowel_count function that accepts a string argument.
# The function should return the count of vowels in the string.
# The 5 vowels are "a", "e", "i", "o", and "u".
# You can assume the string will be in all lowercase.
#
# EXAMPLES:
# vowel_count("estate")     => 3
# vowel_count("helicopter") => 4
# vowel_count("ssh")        =>

def algorithm(algorithm_string: str) -> None:
    def vowel_count(string: str) -> int:
        result = string.count("a") + string.count("e") + string.count("i") + string.count("o") + string.count("u")
        return result

    print("The number of vowels is for", algorithm_string, ":", vowel_count(algorithm_string))


algorithm("estate")
algorithm("helicopter")
algorithm("ssh")
