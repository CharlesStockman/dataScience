# Declare a sum_from function that accepts two numbers as arguments.  The second number will always be greater than
# the first number.  The function should return the sum of all numbers from the first number to the second number
# (inclusive).
#
# sum_from(1, 2)   # 1 + 2 => 3
# sum_from(1, 5)   # 1 + 2 + 3 + 4 + 5 => 15
# sum_from(3, 8)   # 3 + 4 + 5 + 6 + 7 + 8 => 33
# sum_from(9, 12)  # 9 + 10 + 11 + 12 => 42

def algorithm(algorithm_first: int, last: int) -> None:
    def sum_from(first: int, last: int) -> int:
        value = 0
        for number in range(first, last + 1):
            value += number
        return value

    print("The value of first to last is ", sum_from(algorithm_first, last))


algorithm(1, 2)
algorithm(1, 5)
algorithm(3, 8)
algorithm(9, 12)
