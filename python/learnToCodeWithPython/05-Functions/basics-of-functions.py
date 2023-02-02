# Define an easy_money function that accepts no parameters and always returns the value 100.
# Define best_food_ever function that accepts no parameters and always returns the string “Sushi”.
# Define a convert_to_currency function that accepts a single parameter (an integer). 
# The function should convert the argument to a string, prefix it with a dollar sign, and return the result.
# 
# EXAMPLES:
# convert_to_currency(15)    => "$15"
# convert_to_currency(8)     => "$8"


def easy_money() -> float:
    return 100


def best_food_ever() -> str:
    return "Sushi"


def algorithm(amount_of_money: float) -> None:
    def convert_to_currency(money_amount: float) -> str:
        amount_converted_to_string = "$" + str(money_amount)
        return amount_converted_to_string

    print("Amount of money is ", amount_of_money, " converted to a string is ",
          convert_to_currency(amount_of_money))


algorithm(15)
algorithm(8)
