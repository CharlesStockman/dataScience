# Define a vowel_count function that accepts a string argument.
# The function should return the count of vowels in the string.
# The 5 vowels are "a", "e", "i", "o", and "u".
# You can assume the string will be in all lowercase.
#
# EXAMPLES:
# vowel_count("estate")     => 3
# vowel_count("helicopter") => 4
# vowel_count("ssh")        => 0

def algorithm(algorithm_string: str) -> None:
    def vowel_count(string: str) -> int:
        result = string.count("a") + string.count("e") + string.count("i") + string.count("o") + string.count("u")
        return result

    print("The number of vowels is for", algorithm_string, ":", vowel_count(algorithm_string))


algorithm("estate")
algorithm("helicopter")
algorithm("ssh")


# Define a find_my_letter function that accepts two arguments: a string and a character
# The function should return the first index position of the character in the string
# The function should return a -1 if the character does not exist in the string
#
# EXAMPLES:
# find_my_letter("dangerous", "a")    => 1
# find_my_letter("bazooka", "z")      => 2
# find_my_letter("lollipop", "z")     => -1

def algorithm2(input_string : str, input_letter : str):
    def find_my_letter(string:str, input_letter: str):
        return string.find(input_letter)
    print(f"The string is {input_string} and letter to search for is {input_letter} \
        and the location is {find_my_letter(input_string, input_letter)}")
    
algorithm2("dangerous", "a")    
algorithm2("bazooka", "z")     
algorithm2("lollipop", "z")  