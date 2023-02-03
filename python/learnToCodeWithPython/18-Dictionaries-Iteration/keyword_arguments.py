# Declare a plenty_of_arguments function that accepts two parameters (a and b) and an additional **kwargs parameter.
#
# The function should return True if the sum of a, b, and the # values of the kwargs dictionary is greater than 100.
# It should return False otherwise.
#
# plenty_of_arguments(20, 30) => False
# plenty_of_arguments(a = 50, b = 75) => True
# plenty_of_arguments(a = 50, b = 25, c = 50) => True
# plenty_of_arguments(a = 25, b = 25, c = 25, d = 25) => False
# plenty_of_arguments(a = 25, b = 25, c = 25, d = 26) => True

def algorithm(algorithm_a: int, algorithm_b: int, **algorithm_kargs: int) -> None:
    def plenty_of_arguments(a: int, b: int, **kargs: map) -> bool:
        value = a + b + sum(kargs.values())
        return value > 100

    print("Is the values greater then 100 ", plenty_of_arguments(algorithm_a, algorithm_b, **algorithm_kargs))


algorithm(20, 30)
algorithm(algorithm_a=50, algorithm_b=75)
algorithm(algorithm_a=50, algorithm_b=25, c=50)
algorithm(algorithm_a=25, algorithm_b=25, c=25, d=25)
algorithm(algorithm_a=25, algorithm_b=25, c=25, d=26)
