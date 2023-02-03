# Create an empty dictionary and assign it to the variable empty.
empty = {}
print(f"The length of an empty dictionary is {len(empty)}")

# Create a dictionary with three key-value pairs. # The keys should be strings and the values should be integer values.
# Assign the dictionary to a my_dict variable.
my_dict = {"one": 1, "two": 2, "three": 3}
print(f"The dictionary is {my_dict}")

# A dictionary’s keys can be any immutable data structure. # Create a dictionary with two key-value pairs and assign
# it to a winning_lottery_numbers variable. # Both of the keys should be tuples. # One of the values should be True,
# the other value should be False.
winning_lottery_numbers = {}
winning_key = ("lottery_numbers_1", 2, 10)
losing_key = ("lottery_numbers_2", 3, 5)
winning_lottery_numbers[winning_key] = True
winning_lottery_numbers[losing_key] = False

print(f"The winning lottery hash table is {winning_lottery_numbers}")
