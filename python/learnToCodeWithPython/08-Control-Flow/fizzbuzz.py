# Define a fizzbuzz function that accepts a single number as an argument. The function should
# print every number from 1 to that argument. There are a couple caveats.
# ----------------------------------------------------------
# If the number is divisible by 3, print "Fizz" instead of the number.
# If the number is divisible by 5, print "Buzz" instead of the number.
# If the number is divisible by both 3 and 5, print "FizzBuzz" instead of the number.
# If the number is not divisible by either 3 or 5, just print the number.

def fizzbuzz(number: int) -> None:
    for x in range(1, number + 1):
        divisible_by_3 = x % 3
        divisible_by_5 = x % 5

        if divisible_by_3 == 0 and divisible_by_5 == 0:
            value = "FizzBuzz"
        elif divisible_by_3 == 0:
            value = "Fizz"
        elif divisible_by_5 == 0:
            value = "Buzz"
        else:
            value = x

        print(value)


fizzbuzz(30)
