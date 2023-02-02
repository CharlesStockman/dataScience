# Define an up_and_down function that accepts a string argument
# If the string consists of all uppercase letters, return a new string
# consisting of all lowercase letters. If the string consists of all
# lowercase letters, return a new string consisting of all uppercase
# characters. If the string has a mix of uppercase and lowercase
# characters, return a new string where the casing of each letter is swapped.
# 
# up_and_down("HELLO") => "hello"
# up_and_down("genius") => "GENIUS"
# up_and_down("ESPreSso") => "espREsSO"
#
# Interesting for string.upper I had to add the == True since it was always evaluating to true and
# causing the program to fail


def algorithm(algorithm_string: str) -> None:
    def up_and_down(string: str) -> str:
        if string.upper():
            value = string.lower()
        elif string.lower():
            value = string.upper()
        else:
            value = string.swapcase()
        return value

    print("Original String", algorithm_string, " New String", up_and_down(algorithm_string))


algorithm("HELLO")
algorithm("genius")
algorithm("ESPreSso")
