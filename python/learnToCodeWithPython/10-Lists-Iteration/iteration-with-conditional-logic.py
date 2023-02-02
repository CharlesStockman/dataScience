# Define a function concatenate that accepts a list of strings.  The function should return a concatenated string which
# consists of all list elements whose length is greater than 2 characters.
#
# concatenate(["abc", "def", "ghi"])      => "abcdefghi"
# concatenate(["abc", "de", "fgh", "ic"]) => "abcfgh"
# concatenate(["ab", "cd", "ef", "gh"])   => ""

def algorithm(algorithm_collection: list) -> None:
    def concatenate(collection: list) -> str:
        value = ""
        for item in collection:
            if len(item) > 2:
                value += item
        return value

    print("The concatenation of all strings > 2 is ", concatenate(algorithm_collection))


algorithm(["abc", "def", "ghi"])
algorithm(["abc", "de", "fgh", "ic"])
algorithm(["ab", "cd", "ef", "gh"])


# Write a function super_sum that accepts a list of strings. # The function should sum the index positions of the first
# occurrence of the letter “s” in each word.# Not every word is guaranteed to have an “s”. Don’t use the sum keyword as
# it’s a built-in keyword.
#
# super_sum([]) => 0
# super_sum(["mustache"]) => 2
# super_sum(["mustache", "greatest"]) => 8
# super_sum(["mustache", "pessimist"]) => 4
# super_sum(["mustache", "greatest", "almost"]) => 12

def algorithm2(algorithm_collection: list) -> None:
    def super_sum(collection: list) -> int:
        value = 0
        for item in collection:
            index = item.index('s')
            if index != 1:
                value += index
        return value

    print("For the String the indexes of all the 's' is", super_sum(algorithm_collection))


algorithm2([])
algorithm2(["mustache"])
algorithm2(["mustache", "greatest"])
algorithm2(["mustache", "pessimist"])
algorithm2(["mustache", "greatest", "almost"])
