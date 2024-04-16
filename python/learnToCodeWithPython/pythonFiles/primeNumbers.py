def get_first_prime_numbers(number_of_primes_returned: int) -> list:
    """
        Write a function that returns the first n prime numbers

        Input: The amount of prime numbers to be returned or the size of the list
        Output: A list of first prime numbers

        Did some research:
            6n + 1, 6n -1 it can be a prime, but produces a lot of false positives
            The list extends method can put each element of a tuple into the list as a single element

        Fact about Prime Number: Every prime number can be represented in form of 6n + 1 or 6n – 1
        except the prime numbers 2 and 3, where n is a natural number.
        See: https://www.geeksforgeeks.org/prime-numbers/

    """

    from math import sqrt

    # The program starts deciding if a number at prime at 5.
    prime_number_list = [2, 3]
    if number_of_primes_returned < 5:
        return prime_number_list[0:number_of_primes_returned]

    current_index = 0

    # Create a list of prime numbers 
    while len(prime_number_list) < number_of_primes_returned:
        current_index = current_index + 1

        # Any prime number will be found using this equation, but some false positives are presnt..
        # This is why we need to verify the prime numbers
        test_numbers = (6 * current_index - 1, 6 * current_index + 1)

        for test_number in test_numbers:
            result = True

            # Add the number ot the list if it is verified to be prime.
            for number in range(2, int(sqrt(test_number)) + 1):
                if test_number % number == 0:
                    result = False
            else:
                if result:
                    prime_number_list.append(test_number)

    return prime_number_list[0:number_of_primes_returned]


print(get_first_prime_numbers(0))
print(get_first_prime_numbers(1))
print(get_first_prime_numbers(2))
print(get_first_prime_numbers(3))
print(get_first_prime_numbers(100))
