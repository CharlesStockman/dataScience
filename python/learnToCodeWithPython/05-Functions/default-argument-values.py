# Define a string_adder function that accepts two strings (a and b) # as arguments.  It should return a concatenated
# version of the arguments with a space in between.  If the user does not pass in  arguments, both arguments should
# default to an empty string.

def string_adder(first_string="", second_string="") -> str:
    return first_string + " " + second_string


print("Both Arguments Defined -->", string_adder("Charles", "Stockman"))
print("Last Argument Defined -->", string_adder("Charles"))
print("No Arguments Defined --> ", string_adder())
