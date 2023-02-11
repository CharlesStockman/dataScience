import numpy as np
import pprint

# Generate 10 rows with 20 values each
np.random.seed(0)
data = np.random.randint(0, 100, size=(10, 20))

# print the standard deviation of each row in a 2d list
std_deviation_of_rows = np.std(data,axis=0)
pprint.pprint(std_deviation_of_rows)
print("---------------------------")
for index in range(0,len(std_deviation_of_rows)):
    print("Standard Deviation for row ", index, std_deviation_of_rows[index])

print("\n")

# print the values > 90 in a numpy array
pprint.pprint(data[ data > 90])
print("------------------------------")
print("Values > 90 are ", data[data > 90])