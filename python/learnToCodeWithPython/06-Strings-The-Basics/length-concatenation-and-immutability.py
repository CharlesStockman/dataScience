# Define a long_word function that accepts a string. # The function should return a Boolean that reflects whether
# the string has more than 7 characters.
# 
# EXAMPLES:
# long_word("Python") => False
# long_word("magnificent") => True

def long_word(user_input: str) -> bool:
    result = len(user_input) > 7
    return result


print("Is Python a long word? ", long_word("Python"))
print("Is Magnificent a long world? ", long_word("magnificent"))


# Define a first_longer_than_second function that accepts two string arguments. The function should return a True
# if the first string is longer than the second and False otherwise (including if they are equal in length).
#
# EXAMPLES:
# first_longer_than_second("Python", "Ruby")   => True
# first_longer_than_second("cat", "mouse")     => False
# first_longer_than_second("Steven", "Segal") => False

def first_longer_than_second(str1: str, str2: str) -> bool:
    result = len(str1) > len(str2)
    return result


print(
    "Is Python longer than Ruby?",
    first_longer_than_second("Python", "Ruby"))

print(
    "Is Cat longer than mouse? ",
    first_longer_than_second("cat", "mouse"))

print(
    "Is Steven longer than Segal? ",
    first_longer_than_second("Steven", "Segal"))
