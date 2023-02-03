# Define an encrypt_message function that accepts a string.# The input string will consist of only alphabetic
# characters.  The function should return a string where all characters have been moved "up" two spots in the
# alphabet. For example, "a" will become "c".
#
#
# encrypt_message("abc") => "cde"
# encrypt_message("xyz") => "zab"
# encrypt_message("")    => ""

def algorithm(algorithm_collection: str) -> None:
    def encrypt_message(collection: str) -> str:
        secret_message = []
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                   "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "x", "y", "z", "a", "b"]
        for item in collection:
            new_letter = letters[letters.index(item) + 2]
            secret_message.append(new_letter)
        return secret_message

    print("The message is now encrypted:", encrypt_message(algorithm_collection))


algorithm("abc")
algorithm("xyz")
algorithm("")
