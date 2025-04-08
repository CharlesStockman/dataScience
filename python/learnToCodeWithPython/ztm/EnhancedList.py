#
# Create a list when the that will allow the usser to access all list funcitons
# but the length funciton will always return 1000
#

class EnhancedList(list):
	def __len__(self):
		return 1000

enhanced_list = EnhancedList()
print("Number of elements in the list -- ",len(enhanced_list))

print("Appending 1,2,3 to the Enhanced List")
enhanced_list.append(1)
enhanced_list.append(2)
enhanced_list.append(3)

print("New Size of list -- ",len(enhanced_list))
print("Contents of list -- ",enhanced_list)
print("The first element using slices -- ", enhanced_list[0:1])
print("The first element using indexing -- ", enhanced_list[0])
print("Is EnhancedList a subclass of list ", issubclass(EnhancedList, list))
