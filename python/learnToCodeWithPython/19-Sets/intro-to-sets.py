# Declare a set with 3 of your favorite movies as strings.# Assign it to a movies variable.
movies = {"Star Wars", "Empire Strikes Back", "Return of the Jedi", "Star Wars"}
print("The type of movides is ", type(movies))
print("The movies are ", movies)

# Create an empty set and assign it to an empty variable
# empty = set()
print("The empty set is ", empty)

# Define a remove_duplicates function that accepts a single list as an argument.# The function should return a list
# with all of the duplicates from the original list removed. The order of elements in the returned list is irrelevant.
#
# remove_duplicates([1, 2, 1, 2]) => [1, 2] or [2, 1]
# remove_duplicates([1, 2, 3, 4]) => [1, 2, 3, 4] in some order
remove_duplicates = [1, 2, 1, 2]
remove_duplicates = list(set(remove_duplicates))
print(remove_duplicates)

remove_duplicates = [1, 2, 3, 4]
remove_duplicates = list(set(remove_duplicates))
print(remove_duplicates)
