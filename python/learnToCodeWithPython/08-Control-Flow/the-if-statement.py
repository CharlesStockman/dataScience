# Define an even_or_odd function that accepts a single integer.
# If the integer is even, the function should return the string “even”.
# If the integer is odd, the function should return the string “odd”.
#
# even_or_odd(2) => "even"
# even_or_odd(0) => "even"
# even_or_odd(13) => "odd"
# even_or_odd(9) => "odd"

def algorithm(algorithm_number: int) -> None:
    def even_or_odd(number: int) -> str:
        result = "odd"
        if number % 2 == 0:
            result = "even"
        return result

    print("The number", str(algorithm_number).strip(), " is ", even_or_odd(algorithm_number))


algorithm(2)
algorithm(0)
algorithm(13)
algorithm(9)
