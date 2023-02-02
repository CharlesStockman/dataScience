# Provide 3 examples of the rfind method in action.  Write the invocation along with the return value
#
# For the Second element it has a start, but the last rw first

dataString = "browserrowrowser"
print("Finding the index of the last e: ", dataString.rfind("e"))
print("Finding the index of the third rw: ", dataString.rfind("ow", 5))
print("Finding the second to last r: ", dataString.rfind("r", 5, len(dataString) - 3))
