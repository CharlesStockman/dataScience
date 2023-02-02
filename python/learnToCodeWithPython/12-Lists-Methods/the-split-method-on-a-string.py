# Define a word_lengths function that accepts a string. # It should return a list with the lengths of each word.
#
# word_lengths("Mary Poppins was a nanny") => [4, 7, 3, 1, 5]
# word_lengths("Somebody stole my donut") => [8, 5, 2, 5]

def algorithm(algorithm_string: str) -> None:
    def word_lengths(string: str) -> list:
        values = []
        for item in string.split(" "):
            values.append(len(item))
        return values

    print("The length of all the word in the string are ", word_lengths(algorithm_string))


algorithm("Mary Poppins was a nanny")
algorithm("Somebody stole my donut")
