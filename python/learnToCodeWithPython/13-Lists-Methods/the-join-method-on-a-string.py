# Define a cleanup function that accepts a list of strings.  The function should return the strings joined together
# by a space.  There's one BIG problem -- some strings are empty or only consist of spaces!  These should NOT be
# included in the final string
#
# cleanup(["cat", "er", "pillar"]) => "cat er pillar"
# cleanup(["cat", " ", "er", "", "pillar"]) => "cat er pillar"
# cleanup(["", "", " "]) => ""

def algorithm(collection: list) -> None:
    def cleanup(collection: list) -> str:
        for index, item in enumerate(collection):
            if not item.strip():
                del (collection[index])
        value = " ".join(collection)
        return value

    print("The words joined together form:", cleanup(collection))


algorithm(["cat", "er", "pillar"])
algorithm(["cat", " ", "er", "", "pillar"])
algorithm(["", "", " "])
