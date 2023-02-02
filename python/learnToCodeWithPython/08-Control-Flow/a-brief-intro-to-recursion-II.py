# Define a factorial function that accepts a single number A factorial represents the product of all numbers up to,
# and including, that number. For example, 5 factorial is 5 * 4 * 3 * 2 * 1 = 120 Return the factorial from your
# function. You should NOT use any kind of loops. Instead, utilize recursion. Your function MUST call itself.


def factorial(number: int) -> int:
    if number == 1:
        return 1
    else:
        result = factorial(number - 1) * number
    return result


print("The value of the factorial is ", factorial(1))
print("The value of the factorial is ", factorial(2))
print("The value of the factorial is ", factorial(3))
print("The value of the factorial is ", factorial(4))
print("The value of the factorial is ", factorial(5))
