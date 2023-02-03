# Define a first_three_characters function that accepts a string argument.
# The function should return the first 3 characters of the string.
#
# EXAMPLES:
# first_three_characters("dynasty")   => "dyn"
# first_three_characters("empire")    => "emp"

import itertools as it

def algorithm(input_string: str):
    def first_three_characters(string: str):
        return string[0:3]
    print(f"The first three characters of {input_string} is {first_three_characters(input_string)}")

algorithm("dynasty")
algorithm("empire")

# Define a last_five_characters function that accepts a string argument. 
# The function should return the last 5 characters of the string.
#
# EXAMPLES:
# last_five_characters("dynasty")   => "nasty"
# last_five_characters("empire")    => "mpire"

def algorithm2(input_string: str):
    def last_five_characters(string: str):
        return string[-5:]
    print(f"The first three characters of {input_string} is {last_five_characters(input_string)}")

algorithm2("dynasty")
algorithm2("empire")

# Define a is_palindrome function that accepts a string argument. 
# The function should return True if the string is spelled 
# the same backwards as it is forwards. 
# Return False otherwise.
#
# EXAMPLES:
# is_palindrome("racecar")   => True
# is_palindrome("yummy")     => False

def algorithm3(input_string: str):
    def is_palindrome(string: str):
        result = True
        for index_tuple in it.zip_longest(range(0, len(string)), range(-1, (len(string)+1) * -1, -1 )):
            if string[index_tuple[0]] != string[index_tuple[1]]:
                result = False
                break;
        return result

    print(f"Is the string: {input_string} a palindrome -- {is_palindrome(input_string)}")

algorithm3("racecar")
algorithm3("yummy") 