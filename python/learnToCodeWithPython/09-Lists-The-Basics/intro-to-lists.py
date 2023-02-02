# Create an empty list and assign it to the variable "empty".
empty = list()
print("The size of empty is", len(empty))

# Create a list with a single Boolean — True — and assign it to the variable "active".
activeList = [True]
print("The size of the activeListy ", len(activeList))

# Create a list with 5 integers of your choice and assign it to the variable "favorite_numbers".
favorite_numbers = [1, 2, 3, 4, 5]
print("The size of favorite number is ", len(favorite_numbers))

# Create a list with 3 strings  — "red", "green", "blue" — and assign it to the variable "colors".
colors = ["red", "green", "blue"]
print("The size of favorite colors is ", len(colors))


# Declare an is_long function that accepts a single list as an
# argument # It should return True if the list has more than 5 
# elements, and False otherwise

def is_long(my_list: list) -> bool:
    value = True if (len(my_list) > 5) else False
    return value


print("A list with more than 5 values", is_long([0, 1, 2, 3, 4, 5]))
print("A list with more than 5 values", is_long([0, 1, 2]))
