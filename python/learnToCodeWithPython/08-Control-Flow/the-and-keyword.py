# Define a divisible_by_three_and_four function that accepts a number argument.  It should return True if the number is
# evenly divisible by both 3 and 4 . It should return False otherwise.

# divisible_by_three_and_four(3) => False
# divisible_by_three_and_four(4) => False
# divisible_by_three_and_four(12) => True
# divisible_by_three_and_four(18) => False
# divisible_by_three_and_four(24) => true

def algorithm(algorithm_number: int) -> None:
    def divisible_by_three_and_four(number: int) -> bool:
        return True if (number % 3 == 0 and number % 4 == 0) else False

    print(algorithm_number, "is divisible by 3 and 4", divisible_by_three_and_four(algorithm_number))


algorithm(3)
algorithm(4)
algorithm(12)
algorithm(18)
algorithm(24)


# Declare a string_theory function that accepts a string as an argument.
# It should return True if the string has more than 3 characters and starts with a capital “S”.
# It should return False otherwise.
#
# string_theory("Sansa") => True
# string_theory("Story") => True
# string_theory("See") => False
# string_theory("Fable") => False

def algorithm(string: str) -> None:
    def string_theory(string: str) -> bool:
        return True if (len(string) > 3 and string[0] == "S") else False

    print("Original String is ", string, "new String is ", string_theory(string))


algorithm("Sansa")
algorithm("Story")
algorithm("See")
algorithm("Fable")
