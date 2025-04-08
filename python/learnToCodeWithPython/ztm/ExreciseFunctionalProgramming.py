from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize(item):
	return item.capitalize()
print("Capitalize first Letter")
print(my_pets)
print(list(map(capitalize, my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print("Combine two list where the first entry gets the lowest and last entry gets the hightest")
print("Input -- ", my_strings)
print("Input -- ", my_numbers)
combined_list = zip(my_strings, sorted(my_numbers))
print("Output -- ", list(combined_list))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def scoreOver50(item):
	return True if item > 50 else False


print("The original list is         -- ", scores)
print("The list with scores over 50 -- ", list(filter(scoreOver50, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

print("The first list is ", scores)
print("The last  lsit is ", my_numbers)

def accumulator(total, item):
	return total + item

print(reduce(accumulator, [*scores, *my_numbers], 0))



