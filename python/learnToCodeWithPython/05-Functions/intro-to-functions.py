# Define easy_money function that accepts no parameters and always returns the value 100.
def easy_money():
    return 100


print("The value that easy_money returns is", easy_money())


# Define best_food_ever function that accepts no parameters and always returns the string "Sushi"
def best_food_ever():
    return "Sushi"


print("The best food ever is", best_food_ever())


# Define a convert_to_currency function that accepts a single parameter (an integer). The function should convert
# the argument to a string, prefix it with a dollar sign, and return the result. Example:
# convert_to_currency(15) => "$15"
def convert_to_currency(amount):
    return "$" + str(amount)


print("If I pass into convert_to_currency the value, then the result is", convert_to_currency(40))
